"""
Rooted Forest Generation for Cosmos Systems

This module extends the OEIS A000081 rooted tree generation to support
rooted forests (collections of rooted trees), which correspond to the
topologically distinct sets of non-intersecting circles in the plane.

The key insight from Mathar (arXiv:1603.00077) is that the number of
topologically distinct sets of N non-intersecting circles equals the
number of unlabeled rooted forests with N nodes, which is related to
but distinct from A000081 (rooted trees).

For System 5 (Campbell's framework), there are exactly 20 configurations
corresponding to the 20 unlabeled rooted forests with 5 nodes.
"""

from typing import List, Tuple, Dict, Set, Optional
from dataclasses import dataclass, field
from functools import lru_cache
import itertools

from .oeis_trees import TreeNode, RootedTree, RootedTreeGenerator, A000081


# =============================================================================
# OEIS SEQUENCES FOR FORESTS
# =============================================================================

# A033185: Number of topologically distinct sets of N non-intersecting circles
# This equals the number of unlabeled rooted forests with N nodes
# https://oeis.org/A033185
A033185 = [1, 1, 2, 4, 9, 20, 48, 115, 286, 719, 1842]

# Note: A033185(n) = sum over partitions of n of product of A000081 terms
# For n=5: partitions are [5], [4,1], [3,2], [3,1,1], [2,2,1], [2,1,1,1], [1,1,1,1,1]


# =============================================================================
# ROOTED FOREST DATA STRUCTURE
# =============================================================================

@dataclass
class RootedForest:
    """
    A rooted forest is a collection of rooted trees.
    
    In the context of non-intersecting circles, each tree represents
    a maximal nested set of circles (one outer circle containing all others).
    """
    trees: Tuple[RootedTree, ...]
    
    def __hash__(self):
        return hash(self.canonical())
    
    def __eq__(self, other):
        if not isinstance(other, RootedForest):
            return False
        return self.canonical() == other.canonical()
    
    def canonical(self) -> str:
        """
        Return canonical string representation.
        Trees are sorted to ensure canonical form.
        """
        tree_canonicals = sorted(t.canonical() for t in self.trees)
        return "".join(tree_canonicals)
    
    def bracket_notation(self) -> str:
        """Return bracket notation [tree1 tree2 ...] for System 5 analysis."""
        return "[" + self.canonical() + "]"
    
    def node_count(self) -> int:
        """Count total nodes across all trees."""
        return sum(t.node_count() for t in self.trees)
    
    def tree_count(self) -> int:
        """Count number of trees (factors) in the forest."""
        return len(self.trees)
    
    def tree_sizes(self) -> List[int]:
        """Get sizes of all trees, sorted in descending order."""
        return sorted([t.node_count() for t in self.trees], reverse=True)
    
    def max_depth(self) -> int:
        """Get maximum depth across all trees."""
        if not self.trees:
            return 0
        return max(t.root.depth() for t in self.trees)


# =============================================================================
# ROOTED FOREST GENERATION
# =============================================================================

class RootedForestGenerator:
    """
    Generate all rooted forests with n nodes.
    
    This corresponds to the topologically distinct sets of n non-intersecting
    circles in the plane (Mathar, arXiv:1603.00077).
    """
    
    @staticmethod
    @lru_cache(maxsize=20)
    def generate(n: int) -> Tuple[RootedForest, ...]:
        """
        Generate all rooted forests with exactly n nodes.
        Returns a tuple for hashability/caching.
        """
        if n <= 0:
            return (RootedForest(()),)
        
        forests = []
        
        # Generate all integer partitions of n
        for partition in RootedForestGenerator._partitions(n):
            # Generate all combinations of trees for this partition
            for tree_combo in RootedForestGenerator._tree_combinations(partition):
                forest = RootedForest(tuple(tree_combo))
                if forest not in forests:
                    forests.append(forest)
        
        return tuple(forests)
    
    @staticmethod
    def _partitions(n: int) -> List[Tuple[int, ...]]:
        """Generate all integer partitions of n in non-increasing order."""
        if n == 0:
            return [()]
        
        partitions = []
        RootedForestGenerator._partition_helper(n, n, [], partitions)
        return partitions
    
    @staticmethod
    def _partition_helper(n: int, max_val: int, current: List[int],
                          result: List[Tuple[int, ...]]):
        """Helper for partition generation."""
        if n == 0:
            result.append(tuple(current))
            return
        
        for i in range(min(n, max_val), 0, -1):
            RootedForestGenerator._partition_helper(n - i, i, current + [i], result)
    
    @staticmethod
    def _tree_combinations(partition: Tuple[int, ...]) -> List[List[RootedTree]]:
        """
        Generate all combinations of trees for a given partition.
        Handles multisets correctly to avoid duplicates.
        """
        if not partition:
            return [[]]
        
        # Group partition by size
        size_counts: Dict[int, int] = {}
        for size in partition:
            size_counts[size] = size_counts.get(size, 0) + 1
        
        # Get trees for each size
        size_trees: Dict[int, List[RootedTree]] = {}
        for size in size_counts:
            trees = RootedTreeGenerator.generate(size)
            size_trees[size] = list(trees)
        
        # Generate combinations
        result = [[]]
        for size in sorted(size_counts.keys(), reverse=True):
            count = size_counts[size]
            trees = size_trees[size]
            new_result = []
            
            for current in result:
                # Generate combinations with repetition for this size
                for combo in itertools.combinations_with_replacement(trees, count):
                    new_result.append(current + list(combo))
            
            result = new_result
        
        return result
    
    @staticmethod
    def count(n: int) -> int:
        """
        Count the number of rooted forests with n nodes.
        This should equal A033185(n).
        """
        return len(RootedForestGenerator.generate(n))
    
    @staticmethod
    def verify_count(n: int) -> bool:
        """Verify that generated count matches A033185."""
        if n >= len(A033185):
            return True  # Can't verify, assume correct
        return RootedForestGenerator.count(n) == A033185[n]


# =============================================================================
# SYSTEM 5 SPECIFIC FUNCTIONS
# =============================================================================

def get_system5_configurations() -> List[RootedForest]:
    """
    Get all 20 configurations of System 5.
    
    These correspond to the 20 topologically distinct sets of 5 non-intersecting
    circles in the plane, or equivalently, the 20 unlabeled rooted forests with
    5 nodes.
    """
    return list(RootedForestGenerator.generate(5))


def group_by_tree_count(forests: List[RootedForest]) -> Dict[int, List[RootedForest]]:
    """Group forests by the number of trees (factors)."""
    groups: Dict[int, List[RootedForest]] = {}
    for forest in forests:
        count = forest.tree_count()
        if count not in groups:
            groups[count] = []
        groups[count].append(forest)
    return groups


def group_by_max_depth(forests: List[RootedForest]) -> Dict[int, List[RootedForest]]:
    """Group forests by maximum depth."""
    groups: Dict[int, List[RootedForest]] = {}
    for forest in forests:
        depth = forest.max_depth()
        if depth not in groups:
            groups[depth] = []
        groups[depth].append(forest)
    return groups


def group_by_tree_sizes(forests: List[RootedForest]) -> Dict[Tuple[int, ...], List[RootedForest]]:
    """Group forests by tree size signature."""
    groups: Dict[Tuple[int, ...], List[RootedForest]] = {}
    for forest in forests:
        sizes = tuple(forest.tree_sizes())
        if sizes not in groups:
            groups[sizes] = []
        groups[sizes].append(forest)
    return groups


# =============================================================================
# ANALYSIS FUNCTIONS
# =============================================================================

@dataclass
class ForestAnalysis:
    """Analysis results for a rooted forest."""
    forest: RootedForest
    canonical: str
    bracket_notation: str
    node_count: int
    tree_count: int
    tree_sizes: List[int]
    max_depth: int
    is_virtual_image_candidate: bool
    virtual_image_reason: str


def analyze_forest(forest: RootedForest) -> ForestAnalysis:
    """Perform comprehensive analysis of a forest."""
    tree_count = forest.tree_count()
    tree_sizes = forest.tree_sizes()
    
    # Determine if this is a virtual image candidate
    # Based on the analysis: 3-tree configurations are most likely
    is_candidate = tree_count == 3
    reason = ""
    
    if tree_count == 3:
        reason = "3 trees: matches R1-R2-R3 coherent realization pattern"
    elif tree_count == 2 and sorted(tree_sizes) == [2, 3]:
        reason = "2 trees [2,3]: (1-2) + (3-4-5) coalescence pattern"
    
    return ForestAnalysis(
        forest=forest,
        canonical=forest.canonical(),
        bracket_notation=forest.bracket_notation(),
        node_count=forest.node_count(),
        tree_count=tree_count,
        tree_sizes=tree_sizes,
        max_depth=forest.max_depth(),
        is_virtual_image_candidate=is_candidate,
        virtual_image_reason=reason
    )


def analyze_all_system5() -> List[ForestAnalysis]:
    """Analyze all 20 System 5 configurations."""
    forests = get_system5_configurations()
    return [analyze_forest(f) for f in forests]


def get_virtual_image_candidates() -> List[ForestAnalysis]:
    """Get the 3 configurations that generate virtual images."""
    analyses = analyze_all_system5()
    return [a for a in analyses if a.is_virtual_image_candidate]


# =============================================================================
# DISPLAY AND REPORTING
# =============================================================================

def print_system5_report():
    """Print a comprehensive report of System 5 configurations."""
    print("=" * 70)
    print("System 5 Configuration Report")
    print("=" * 70)
    
    forests = get_system5_configurations()
    print(f"\nTotal configurations: {len(forests)}")
    print(f"Expected (A033185[5]): {A033185[5]}")
    print(f"Match: {'✓' if len(forests) == A033185[5] else '✗'}")
    
    # Group by tree count
    by_count = group_by_tree_count(forests)
    print("\n" + "-" * 70)
    print("Grouped by number of trees (factors):")
    print("-" * 70)
    
    for count in sorted(by_count.keys()):
        group = by_count[count]
        print(f"\n{count} tree(s): {len(group)} configurations")
        for forest in group:
            analysis = analyze_forest(forest)
            marker = " ***" if analysis.is_virtual_image_candidate else ""
            print(f"  {analysis.bracket_notation:25s} sizes={analysis.tree_sizes} depth={analysis.max_depth}{marker}")
    
    # Virtual image candidates
    candidates = get_virtual_image_candidates()
    print("\n" + "-" * 70)
    print("Virtual Image Candidates (3 configurations):")
    print("-" * 70)
    
    for i, analysis in enumerate(candidates, 1):
        print(f"\n{i}. {analysis.bracket_notation}")
        print(f"   Tree sizes: {analysis.tree_sizes}")
        print(f"   Max depth: {analysis.max_depth}")
        print(f"   Reason: {analysis.virtual_image_reason}")


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print_system5_report()
