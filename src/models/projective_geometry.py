"""
Projective Geometry and Mathematical Structures for Cosmos Systems

This module implements the mathematical formalization of Systems 0-5 using:
- Projective geometry (Pascal's triangle, simplex elements)
- Topological surfaces (nested parentheses partitions)
- Matula numbers (prime factorization of rooted trees)
- Simplex polytopes (dimensional progression)
- Nested tuple expressions (recursive structure encoding)
"""

from dataclasses import dataclass, field
from typing import List, Tuple, Dict, Set, Optional, Generator
from functools import lru_cache
import math


# =============================================================================
# MATULA NUMBERS - Prime factorization encoding of rooted trees
# =============================================================================

def is_prime(n: int) -> bool:
    """Check if n is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def nth_prime(n: int) -> int:
    """Return the nth prime number (1-indexed: nth_prime(1) = 2)."""
    if n < 1:
        raise ValueError("n must be >= 1")
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num


def prime_index(p: int) -> int:
    """Return the index of prime p (1-indexed: prime_index(2) = 1)."""
    if not is_prime(p):
        raise ValueError(f"{p} is not prime")
    count = 0
    for i in range(2, p + 1):
        if is_prime(i):
            count += 1
    return count


def matula_to_tree(n: int) -> dict:
    """
    Convert Matula number to rooted tree representation.
    
    Matula encoding:
    - 1 represents the empty tree (no nodes)
    - 2 represents a single node (leaf)
    - For composite n = p1^a1 * p2^a2 * ..., the root has children
      corresponding to matula_to_tree(index(p1)), matula_to_tree(index(p2)), etc.
    - For prime p, the tree has a root with one child: matula_to_tree(index(p))
    """
    if n == 1:
        return {"value": "empty", "children": []}
    if n == 2:
        return {"value": "leaf", "children": []}
    
    # Factor n
    children = []
    temp = n
    p = 2
    while temp > 1:
        while temp % p == 0:
            temp //= p
            child_matula = prime_index(p)
            children.append(matula_to_tree(child_matula))
        p += 1
    
    return {"value": "node", "children": children}


def tree_to_matula(tree: dict) -> int:
    """Convert rooted tree representation to Matula number."""
    if not tree["children"]:
        if tree["value"] == "empty":
            return 1
        return 2  # leaf
    
    result = 1
    for child in tree["children"]:
        child_matula = tree_to_matula(child)
        result *= nth_prime(child_matula)
    return result


def tree_to_nested_parens(tree: dict) -> str:
    """Convert tree to nested parentheses notation."""
    if tree["value"] == "empty":
        return ""
    if not tree["children"]:
        return "()"
    
    children_str = "".join(tree_to_nested_parens(c) for c in tree["children"])
    return f"({children_str})"


# =============================================================================
# PASCAL'S TRIANGLE AND SIMPLEX ELEMENTS
# =============================================================================

@lru_cache(maxsize=100)
def pascal_row(n: int) -> Tuple[int, ...]:
    """Return the nth row of Pascal's triangle (0-indexed)."""
    if n == 0:
        return (1,)
    prev = pascal_row(n - 1)
    return tuple([1] + [prev[i] + prev[i+1] for i in range(len(prev)-1)] + [1])


def simplex_elements(dim: int) -> Dict[str, int]:
    """
    Return the count of k-dimensional elements in an n-simplex.
    
    For an n-simplex:
    - vertices (0-dim): C(n+1, 1) = n+1
    - edges (1-dim): C(n+1, 2)
    - faces (2-dim): C(n+1, 3)
    - cells (3-dim): C(n+1, 4)
    - etc.
    """
    if dim < 0:
        return {"void": 1}
    
    elements = {}
    names = ["vertices", "edges", "faces", "cells", "hypercells", "5-faces"]
    
    for k in range(dim + 1):
        count = math.comb(dim + 1, k + 1)
        name = names[k] if k < len(names) else f"{k}-elements"
        elements[name] = count
    
    return elements


# =============================================================================
# TOPOLOGICAL SURFACES - Nested parentheses partitions
# =============================================================================

def generate_partitions(n: int) -> Generator[str, None, None]:
    """
    Generate all valid nested parentheses (Dyck words) for n pairs.
    These represent the topological surfaces / partitions.
    """
    def backtrack(s: str, open_count: int, close_count: int):
        if len(s) == 2 * n:
            yield s
            return
        if open_count < n:
            yield from backtrack(s + "(", open_count + 1, close_count)
        if close_count < open_count:
            yield from backtrack(s + ")", open_count, close_count + 1)
    
    yield from backtrack("", 0, 0)


def catalan_number(n: int) -> int:
    """Return the nth Catalan number."""
    return math.comb(2 * n, n) // (n + 1)


def partition_to_tree(parens: str) -> dict:
    """Convert nested parentheses to tree structure."""
    def parse(s: str, idx: int) -> Tuple[dict, int]:
        children = []
        i = idx
        while i < len(s):
            if s[i] == '(':
                child, i = parse(s, i + 1)
                children.append(child)
            elif s[i] == ')':
                return {"children": children}, i + 1
            else:
                i += 1
        return {"children": children}, i
    
    if not parens:
        return {"children": []}
    
    # Wrap in outer parens for consistent parsing
    result, _ = parse("(" + parens + ")", 1)
    return result


# =============================================================================
# NESTED TUPLE EXPRESSIONS
# =============================================================================

@dataclass
class NestedTuple:
    """Represents a nested tuple expression for a System."""
    level: int
    children: List['NestedTuple'] = field(default_factory=list)
    
    def __repr__(self) -> str:
        if not self.children:
            return f"[{self.level}]"
        children_str = ",".join(repr(c) for c in self.children)
        return f"[{self.level}[{children_str}]]"
    
    def expand(self) -> str:
        """Expand to full nested form."""
        if self.level <= 1:
            return "[1]"
        
        # Create 'level' copies of the previous system
        prev = NestedTuple(self.level - 1)
        return f"[{','.join([prev.expand()] * self.level)}]"
    
    def to_array(self) -> list:
        """Convert to nested Python list."""
        if self.level <= 1:
            return [1]
        
        prev = NestedTuple(self.level - 1)
        return [prev.to_array() for _ in range(self.level)]


def system_nested_tuple(n: int) -> NestedTuple:
    """Create the nested tuple expression for System n."""
    return NestedTuple(n)


# =============================================================================
# SYSTEM DEFINITIONS
# =============================================================================

@dataclass
class CosmosSystem:
    """Complete mathematical definition of a Cosmos System."""
    
    number: int
    name: str
    terms: int
    partitions: int
    universal_count: int
    particular_count: int
    
    # Simplex properties
    simplex_dim: int
    simplex_name: str
    concurrency: int
    concurrency_name: str
    
    # Matula numbers for this system
    matula_numbers: List[int]
    
    # Additional properties
    properties: List[str] = field(default_factory=list)
    
    @property
    def pascal_coefficients(self) -> Tuple[int, ...]:
        """Pascal's triangle row for this system."""
        if self.number < 0:
            return (1,)
        return pascal_row(self.number)
    
    @property
    def simplex_elements(self) -> Dict[str, int]:
        """Element counts for the corresponding simplex."""
        return simplex_elements(self.simplex_dim)
    
    @property
    def nested_tuple(self) -> NestedTuple:
        """Nested tuple expression for this system."""
        return system_nested_tuple(self.number)
    
    @property
    def topological_surfaces(self) -> List[str]:
        """All valid topological surfaces (partitions)."""
        if self.number <= 0:
            return ["{}"]
        return [f"{{{p}}}" for p in generate_partitions(self.number)]
    
    @property
    def catalan(self) -> int:
        """Catalan number for partition count."""
        if self.number <= 0:
            return 1
        return catalan_number(self.number - 1)


# =============================================================================
# SYSTEM INSTANCES
# =============================================================================

SYSTEM_0 = CosmosSystem(
    number=0,
    name="Void (Hole)",
    terms=1,
    partitions=0,
    universal_count=0,
    particular_count=0,
    simplex_dim=-1,
    simplex_name="vo-id",
    concurrency=-1,
    concurrency_name="0-Sets (Category/Spin)",
    matula_numbers=[1],
    properties=["Category", "Spin", "Unmarked State"]
)

SYSTEM_1 = CosmosSystem(
    number=1,
    name="Monad (Whole)",
    terms=1,
    partitions=1,
    universal_count=1,
    particular_count=0,
    simplex_dim=0,
    simplex_name="mon-ad",
    concurrency=0,
    concurrency_name="1-Nest (Degree/Point)",
    matula_numbers=[2],
    properties=["Degree", "Point", "Universal Wholeness"]
)

SYSTEM_2 = CosmosSystem(
    number=2,
    name="Diasect (Term)",
    terms=2,
    partitions=2,
    universal_count=1,
    particular_count=1,
    simplex_dim=1,
    simplex_name="dia-sect",
    concurrency=1,
    concurrency_name="2-Vert (Metric/Line)",
    matula_numbers=[4, 3],
    properties=["Metric", "Line", "Perceptive Wholeness"]
)

SYSTEM_3 = CosmosSystem(
    number=3,
    name="Triagon (Relations)",
    terms=4,
    partitions=3,
    universal_count=1,
    particular_count=2,
    simplex_dim=2,
    simplex_name="tria-gon",
    concurrency=2,
    concurrency_name="3-Edge (Triangle)",
    matula_numbers=[8, 6, 7, 5],
    properties=["Triangle", "Four Relations", "Discretion-Means-Goal-Consequence"]
)

SYSTEM_4 = CosmosSystem(
    number=4,
    name="Tetrahedron (Creative Process)",
    terms=9,
    partitions=5,
    universal_count=2,
    particular_count=3,
    simplex_dim=3,
    simplex_name="tetra-hedron",
    concurrency=3,
    concurrency_name="4-Face (Tetrahedron)",
    matula_numbers=[16, 12, 9, 14, 10, 19, 13, 17, 11],
    properties=["Tetrahedron", "Enneagram", "Primary Creative Process", "12-Stage Cycle"]
)

SYSTEM_5 = CosmosSystem(
    number=5,
    name="Pentachoron (Integration)",
    terms=20,
    partitions=7,
    universal_count=3,
    particular_count=4,
    simplex_dim=4,
    simplex_name="penta-choron",
    concurrency=4,
    concurrency_name="5-Cell (Convolution 2×2)",
    matula_numbers=[32, 34, 18, 28, 21, 20, 15, 38, 26, 34, 22, 53, 37, 23, 43, 29, 67, 41, 53, 31],
    properties=["Pentachoron", "5-Cell", "3 Concurrent Streams", "[[D-T]-[P-O]-[S-M]]"]
)

ALL_SYSTEMS = [SYSTEM_0, SYSTEM_1, SYSTEM_2, SYSTEM_3, SYSTEM_4, SYSTEM_5]


# =============================================================================
# ANALYSIS FUNCTIONS
# =============================================================================

def analyze_system(system: CosmosSystem) -> dict:
    """Generate comprehensive analysis of a system."""
    return {
        "system": system.number,
        "name": system.name,
        "terms": system.terms,
        "partitions": system.partitions,
        "universal": system.universal_count,
        "particular": system.particular_count,
        "pascal_row": system.pascal_coefficients,
        "pascal_sum": sum(system.pascal_coefficients),
        "simplex": {
            "dimension": system.simplex_dim,
            "name": system.simplex_name,
            "elements": system.simplex_elements
        },
        "concurrency": {
            "level": system.concurrency,
            "name": system.concurrency_name
        },
        "matula_numbers": system.matula_numbers,
        "nested_tuple": str(system.nested_tuple),
        "catalan_number": system.catalan,
        "surface_count": len(system.topological_surfaces),
        "properties": system.properties
    }


def print_system_summary():
    """Print a summary table of all systems."""
    print("\n" + "="*80)
    print("COSMOS SYSTEMS MATHEMATICAL SUMMARY")
    print("="*80)
    
    headers = ["Sys", "Name", "Terms", "Parts", "Dim", "Polytope", "Concurrency"]
    print(f"\n{headers[0]:<4} {headers[1]:<25} {headers[2]:<6} {headers[3]:<6} {headers[4]:<4} {headers[5]:<15} {headers[6]}")
    print("-"*80)
    
    for sys in ALL_SYSTEMS:
        print(f"{sys.number:<4} {sys.name:<25} {sys.terms:<6} {sys.partitions:<6} {sys.simplex_dim:<4} {sys.simplex_name:<15} {sys.concurrency_name}")
    
    print("\n" + "="*80)
    print("PASCAL'S TRIANGLE MAPPING")
    print("="*80)
    
    for sys in ALL_SYSTEMS:
        coeffs = " ".join(str(c) for c in sys.pascal_coefficients)
        print(f"System {sys.number}: {coeffs:^40} (sum = {sum(sys.pascal_coefficients)})")
    
    print("\n" + "="*80)
    print("MATULA NUMBERS")
    print("="*80)
    
    for sys in ALL_SYSTEMS:
        matulas = ", ".join(str(m) for m in sys.matula_numbers)
        print(f"System {sys.number}: {{ {matulas} }}")


if __name__ == "__main__":
    print_system_summary()
    
    print("\n" + "="*80)
    print("DETAILED SYSTEM ANALYSIS")
    print("="*80)
    
    for sys in ALL_SYSTEMS:
        analysis = analyze_system(sys)
        print(f"\n--- System {sys.number}: {sys.name} ---")
        print(f"  Nested Tuple: {analysis['nested_tuple']}")
        print(f"  Simplex Elements: {analysis['simplex']['elements']}")
        print(f"  Topological Surfaces: {analysis['surface_count']} (Catalan C_{sys.number-1} = {analysis['catalan_number']})")
