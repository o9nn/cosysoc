"""
OEIS A000081/A000055 Tree Generation for Cosmos Systems

This module implements rooted tree generation (A000081) and the flip transform
for clustering into unrooted equivalence classes (A000055).

The key insight is that System n has exactly A000081(n+1) terms, grouped into
A000055(n+1) clusters via the flip transform.
"""

from typing import List, Dict, Tuple, Optional, Set
from dataclasses import dataclass, field
from functools import lru_cache
import itertools


# =============================================================================
# OEIS SEQUENCES
# =============================================================================

# A000081: Number of rooted trees with n unlabeled nodes
# https://oeis.org/A000081
A000081 = [0, 1, 1, 2, 4, 9, 20, 48, 115, 286, 719, 1842, 4766, 12486]

# A000055: Number of unrooted trees with n unlabeled nodes  
# https://oeis.org/A000055
A000055 = [1, 1, 1, 1, 2, 3, 6, 11, 23, 47, 106, 235, 551, 1301]


# =============================================================================
# SYSTEM DEFINITIONS
# =============================================================================

@dataclass
class SystemDefinition:
    """Definition of a system level with OEIS-aligned term counts."""
    level: int
    name: str
    description: str
    node_count: int  # n+1 for System n
    term_count: int  # A000081(n+1)
    cluster_count: int  # A000055(n+1)


def get_system_definitions() -> List[SystemDefinition]:
    """Get all system definitions with correct OEIS alignment."""
    return [
        SystemDefinition(0, "System 0", "The Void - root only", 1, 1, 1),
        SystemDefinition(1, "System 1", "Universal Wholeness", 2, 1, 1),
        SystemDefinition(2, "System 2", "Fundamental Dyad", 3, 2, 1),
        SystemDefinition(3, "System 3", "Four Relations", 4, 4, 2),
        SystemDefinition(4, "System 4", "Enneagram", 5, 9, 3),
        SystemDefinition(5, "System 5", "Pentachoron", 6, 20, 6),
        SystemDefinition(6, "System 6", "Activity of Enneagrams", 7, 48, 11),
        SystemDefinition(7, "System 7", "Enneagram of Enneagrams", 8, 115, 23),
        SystemDefinition(8, "System 8", "Nested Complementarity", 9, 286, 47),
        SystemDefinition(9, "System 9", "Deep Nesting", 10, 719, 106),
        SystemDefinition(10, "System 10", "Full Recursive Elaboration", 11, 1842, 235),
    ]


def term_count_for_level(level: int) -> int:
    """Get the number of terms for a system level (A000081(n+1))."""
    if level < 0 or level > 10:
        raise ValueError(f"System level must be 0-10, got {level}")
    return A000081[level + 1]


def cluster_count_for_level(level: int) -> int:
    """Get the number of clusters for a system level (A000055(n+1))."""
    if level < 0 or level > 10:
        raise ValueError(f"System level must be 0-10, got {level}")
    return A000055[level + 1]


# =============================================================================
# ROOTED TREE DATA STRUCTURE
# =============================================================================

@dataclass
class TreeNode:
    """A node in a rooted tree."""
    children: Tuple['TreeNode', ...] = field(default_factory=tuple)
    
    def __hash__(self):
        return hash(self.canonical())
    
    def __eq__(self, other):
        if not isinstance(other, TreeNode):
            return False
        return self.canonical() == other.canonical()
    
    def canonical(self) -> str:
        """
        Return canonical string representation using nested parentheses.
        Children are sorted to ensure canonical form.
        """
        if not self.children:
            return "()"
        child_canonicals = sorted(child.canonical() for child in self.children)
        return "(" + "".join(child_canonicals) + ")"
    
    def node_count(self) -> int:
        """Count total nodes in this tree."""
        return 1 + sum(child.node_count() for child in self.children)
    
    def depth(self) -> int:
        """Get the depth of this tree."""
        if not self.children:
            return 0
        return 1 + max(child.depth() for child in self.children)
    
    def all_nodes(self) -> List['TreeNode']:
        """Get all nodes in the tree including self."""
        nodes = [self]
        for child in self.children:
            nodes.extend(child.all_nodes())
        return nodes


@dataclass
class RootedTree:
    """A rooted tree with a designated root node."""
    root: TreeNode
    
    def __hash__(self):
        return hash(self.canonical())
    
    def __eq__(self, other):
        if not isinstance(other, RootedTree):
            return False
        return self.canonical() == other.canonical()
    
    def canonical(self) -> str:
        """Return canonical string representation."""
        return self.root.canonical()
    
    def node_count(self) -> int:
        """Count total nodes."""
        return self.root.node_count()


# =============================================================================
# ROOTED TREE GENERATION (A000081)
# =============================================================================

class RootedTreeGenerator:
    """Generate all rooted trees with n nodes (A000081)."""
    
    @staticmethod
    @lru_cache(maxsize=20)
    def generate(n: int) -> Tuple[RootedTree, ...]:
        """
        Generate all rooted trees with exactly n nodes.
        Returns a tuple for hashability/caching.
        """
        if n <= 0:
            return ()
        if n == 1:
            return (RootedTree(TreeNode()),)
        
        trees = []
        
        # Generate all partitions of (n-1) for child subtrees
        for partition in RootedTreeGenerator._partitions(n - 1):
            # Generate all combinations of subtrees for this partition
            for subtrees in RootedTreeGenerator._subtree_combinations(partition):
                root = TreeNode(tuple(subtrees))
                tree = RootedTree(root)
                if tree not in trees:
                    trees.append(tree)
        
        return tuple(trees)
    
    @staticmethod
    def _partitions(n: int) -> List[Tuple[int, ...]]:
        """Generate all integer partitions of n in non-increasing order."""
        if n == 0:
            return [()]
        
        partitions = []
        RootedTreeGenerator._partition_helper(n, n, [], partitions)
        return partitions
    
    @staticmethod
    def _partition_helper(n: int, max_val: int, current: List[int], 
                          result: List[Tuple[int, ...]]):
        """Helper for partition generation."""
        if n == 0:
            result.append(tuple(current))
            return
        
        for i in range(min(n, max_val), 0, -1):
            RootedTreeGenerator._partition_helper(n - i, i, current + [i], result)
    
    @staticmethod
    def _subtree_combinations(partition: Tuple[int, ...]) -> List[List[TreeNode]]:
        """
        Generate all combinations of subtrees for a given partition.
        Handles multisets correctly to avoid duplicates.
        """
        if not partition:
            return [[]]
        
        # Group partition by size
        size_counts: Dict[int, int] = {}
        for size in partition:
            size_counts[size] = size_counts.get(size, 0) + 1
        
        # Get trees for each size
        size_trees: Dict[int, List[TreeNode]] = {}
        for size in size_counts:
            trees = RootedTreeGenerator.generate(size)
            size_trees[size] = [t.root for t in trees]
        
        # Generate combinations
        result = [[]]
        for size, count in sorted(size_counts.items()):
            trees = size_trees[size]
            new_result = []
            
            for current in result:
                # Generate combinations with repetition for this size
                for combo in itertools.combinations_with_replacement(trees, count):
                    new_result.append(current + list(combo))
            
            result = new_result
        
        return result


# =============================================================================
# FLIP TRANSFORM (A000055)
# =============================================================================

class FlipTransform:
    """
    Group rooted trees into unrooted equivalence classes via the flip transform.
    Two rooted trees are equivalent if one can be re-rooted to match the other.
    """
    
    @staticmethod
    def group_into_clusters(trees: Tuple[RootedTree, ...]) -> List[List[RootedTree]]:
        """
        Group rooted trees into clusters of equivalent unrooted trees.
        Returns list of clusters, where each cluster contains equivalent rooted trees.
        """
        if not trees:
            return []
        
        clusters: List[List[RootedTree]] = []
        assigned: Set[str] = set()
        
        for tree in trees:
            canonical = tree.canonical()
            if canonical in assigned:
                continue
            
            # Find all re-rootings of this tree
            cluster = FlipTransform._find_all_rerootings(tree)
            
            # Mark all as assigned
            for t in cluster:
                assigned.add(t.canonical())
            
            clusters.append(cluster)
        
        return clusters
    
    @staticmethod
    def _find_all_rerootings(tree: RootedTree) -> List[RootedTree]:
        """Find all distinct re-rootings of a tree."""
        rerootings = []
        seen: Set[str] = set()
        
        # Get all nodes
        all_nodes = tree.root.all_nodes()
        
        # For each node, try re-rooting at that node
        for i, _ in enumerate(all_nodes):
            rerooted = FlipTransform._reroot_at_index(tree, i)
            canonical = rerooted.canonical()
            
            if canonical not in seen:
                seen.add(canonical)
                rerootings.append(rerooted)
        
        return rerootings
    
    @staticmethod
    def _reroot_at_index(tree: RootedTree, index: int) -> RootedTree:
        """
        Re-root the tree at the node with given index.
        This is a simplified implementation that works for small trees.
        """
        if index == 0:
            return tree
        
        # For a proper implementation, we need to:
        # 1. Find the path from root to target node
        # 2. Reverse the parent-child relationships along this path
        # 3. Return the new tree
        
        # Simplified: rebuild tree structure with new root
        # This is computationally expensive but correct for small trees
        
        all_nodes = tree.root.all_nodes()
        if index >= len(all_nodes):
            return tree
        
        # Build adjacency representation
        edges = FlipTransform._get_edges(tree.root, None)
        
        # Rebuild tree from new root
        new_root = FlipTransform._build_from_edges(edges, index, set())
        
        return RootedTree(new_root)
    
    @staticmethod
    def _get_edges(node: TreeNode, parent_idx: Optional[int], 
                   current_idx: int = 0) -> List[Tuple[int, int]]:
        """Get all edges as pairs of node indices."""
        edges = []
        child_idx = current_idx + 1
        
        for child in node.children:
            edges.append((current_idx, child_idx))
            child_edges = FlipTransform._get_edges(child, current_idx, child_idx)
            edges.extend(child_edges)
            child_idx += child.node_count()
        
        return edges
    
    @staticmethod
    def _build_from_edges(edges: List[Tuple[int, int]], root_idx: int,
                          visited: Set[int]) -> TreeNode:
        """Build a tree from edges starting at given root."""
        visited.add(root_idx)
        
        # Find all neighbors
        neighbors = []
        for a, b in edges:
            if a == root_idx and b not in visited:
                neighbors.append(b)
            elif b == root_idx and a not in visited:
                neighbors.append(a)
        
        # Recursively build children
        children = []
        for neighbor in sorted(neighbors):
            child = FlipTransform._build_from_edges(edges, neighbor, visited)
            children.append(child)
        
        return TreeNode(tuple(children))
    
    @staticmethod
    def verify(max_n: int = 6) -> bool:
        """
        Verify that generated counts match OEIS sequences.
        Returns True if all verifications pass.
        """
        for n in range(1, max_n + 1):
            trees = RootedTreeGenerator.generate(n)
            clusters = FlipTransform.group_into_clusters(trees)
            
            if len(trees) != A000081[n]:
                print(f"FAIL: n={n}, generated {len(trees)} trees, expected {A000081[n]}")
                return False
            
            if len(clusters) != A000055[n]:
                print(f"FAIL: n={n}, generated {len(clusters)} clusters, expected {A000055[n]}")
                return False
        
        print(f"PASS: All verifications passed for n=1 to {max_n}")
        return True


# =============================================================================
# SYSTEM TREE MAPPING
# =============================================================================

class SystemTreeMapping:
    """Map system levels to their rooted tree representations."""
    
    @staticmethod
    def get_system_trees(level: int) -> Tuple[RootedTree, ...]:
        """Get all rooted trees for a system level."""
        node_count = level + 1
        return RootedTreeGenerator.generate(node_count)
    
    @staticmethod
    def get_system_clusters(level: int) -> List[List[RootedTree]]:
        """Get all clusters for a system level."""
        trees = SystemTreeMapping.get_system_trees(level)
        return FlipTransform.group_into_clusters(trees)
    
    @staticmethod
    def get_summary(level: int) -> Dict:
        """Get a summary of trees and clusters for a system level."""
        trees = SystemTreeMapping.get_system_trees(level)
        clusters = FlipTransform.group_into_clusters(trees)
        
        return {
            'level': level,
            'node_count': level + 1,
            'term_count': len(trees),
            'cluster_count': len(clusters),
            'tree_canonicals': [t.canonical() for t in trees],
            'cluster_sizes': [len(c) for c in clusters],
            'expected_terms': A000081[level + 1],
            'expected_clusters': A000055[level + 1],
            'verified': len(trees) == A000081[level + 1] and len(clusters) == A000055[level + 1]
        }


# =============================================================================
# MATULA NUMBER ENCODING
# =============================================================================

def nth_prime(n: int) -> int:
    """Get the nth prime number (1-indexed)."""
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    if n <= len(primes):
        return primes[n - 1]
    
    # Generate more primes if needed
    candidate = primes[-1] + 2
    while len(primes) < n:
        is_prime = True
        for p in primes:
            if p * p > candidate:
                break
            if candidate % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
        candidate += 2
    
    return primes[n - 1]


def tree_to_matula(node: TreeNode) -> int:
    """
    Convert a rooted tree to its Matula number.
    
    M(empty) = 1
    M(single node) = 2
    M(tree with children T1, T2, ..., Tk) = prime(M(T1)) × prime(M(T2)) × ... × prime(M(Tk))
    """
    if not node.children:
        return 2  # Single node
    
    result = 1
    for child in node.children:
        child_matula = tree_to_matula(child)
        result *= nth_prime(child_matula)
    
    return result


# =============================================================================
# DEMONSTRATION
# =============================================================================

def demonstrate():
    """Demonstrate the OEIS tree generation and clustering."""
    print("OEIS A000081/A000055 Tree Generation for Cosmos Systems")
    print("=" * 60)
    
    # Verify implementation
    print("\nVerification:")
    FlipTransform.verify(6)
    
    # Show system summaries
    print("\n" + "=" * 60)
    print("System Summaries:")
    print("=" * 60)
    
    print(f"\n{'System':<10} {'Nodes':<8} {'Terms':<10} {'Clusters':<10} {'Verified':<10}")
    print("-" * 48)
    
    for level in range(7):
        summary = SystemTreeMapping.get_summary(level)
        print(f"{level:<10} {summary['node_count']:<8} {summary['term_count']:<10} "
              f"{summary['cluster_count']:<10} {'✓' if summary['verified'] else '✗':<10}")
    
    # Show detailed trees for System 3 and 4
    for level in [3, 4]:
        print(f"\n{'=' * 60}")
        print(f"System {level} Detail:")
        print("=" * 60)
        
        trees = SystemTreeMapping.get_system_trees(level)
        clusters = SystemTreeMapping.get_system_clusters(level)
        
        print(f"\nRooted Trees ({len(trees)} total):")
        for i, tree in enumerate(trees):
            matula = tree_to_matula(tree.root)
            print(f"  {i+1}. {tree.canonical():<20} Matula: {matula}")
        
        print(f"\nClusters ({len(clusters)} total):")
        for i, cluster in enumerate(clusters):
            print(f"  Cluster {i+1} ({len(cluster)} trees):")
            for tree in cluster:
                print(f"    {tree.canonical()}")


if __name__ == "__main__":
    demonstrate()
