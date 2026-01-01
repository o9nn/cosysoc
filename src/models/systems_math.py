"""
Cosmos System of Consciousness - Mathematical Models

This module provides mathematical representations for Systems 1-5
based on Robert Campbell's framework from "Fisherman's Guide".

The models capture:
- State representations for each system level
- Transformation matrices for state transitions
- Energy flow equations
- Geometric symmetries (tetrahedral, enneagram)
"""

import numpy as np
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum
import math


# =============================================================================
# SYSTEM 1: Universal Wholeness
# =============================================================================

@dataclass
class System1State:
    """
    System 1: Single center representing universal wholeness.
    
    The ground state - undifferentiated unity with sky.
    Represented by a single point with unbounded interface.
    """
    center: float = 1.0  # Unity value
    periphery: float = float('inf')  # Unbounded
    
    def energy(self) -> float:
        """Total energy in System 1 (normalized to 1)"""
        return self.center
    
    def interface_ratio(self) -> float:
        """Ratio of center to periphery (approaches 0 for unbounded)"""
        if self.periphery == float('inf'):
            return 0.0
        return self.center / self.periphery


# =============================================================================
# SYSTEM 2: Perceptive Wholeness
# =============================================================================

class Mode(Enum):
    """Two modes in System 2"""
    SUBJECTIVE = "subjective"
    OBJECTIVE = "objective"


@dataclass
class System2State:
    """
    System 2: Two centers forming perceptive wholeness.
    
    Introduces duality: subjective/objective modes.
    Two centers define a single "term".
    """
    center1: float  # Subjective center (inner)
    center2: float  # Objective center (outer)
    
    def __post_init__(self):
        # Normalize to maintain unity
        total = self.center1 + self.center2
        if total > 0:
            self.center1 /= total
            self.center2 /= total
    
    def term_value(self) -> float:
        """The perceptive wholeness term (relationship between centers)"""
        return self.center1 * self.center2
    
    def polarity(self) -> float:
        """Polarity between subjective and objective (-1 to 1)"""
        return self.center1 - self.center2
    
    def transition(self, rate: float = 0.1) -> 'System2State':
        """Transition between modes"""
        new_c1 = self.center1 + rate * (self.center2 - self.center1)
        new_c2 = self.center2 + rate * (self.center1 - self.center2)
        return System2State(new_c1, new_c2)


# =============================================================================
# SYSTEM 3: Four Relations
# =============================================================================

class Relation(Enum):
    """The four relations in System 3"""
    DISCRETION = 1   # Timelike succession
    MEANS = 2        # Regenerative mode
    GOAL = 3         # Reconciliation
    CONSEQUENCE = 4  # Independent wholes


@dataclass
class System3State:
    """
    System 3: Four centers forming four relation terms.
    
    The four relations:
    1. Discretion: Idea → Routine → Formation (timelike)
    2. Means: Regenerative countercurrent identities
    3. Goal: Reconciliation of center and periphery
    4. Consequence: Three independent yet related centers (spacelike)
    """
    centers: np.ndarray  # 4 centers
    
    def __init__(self, values: Optional[List[float]] = None):
        if values is None:
            values = [0.25, 0.25, 0.25, 0.25]
        self.centers = np.array(values)
        self._normalize()
    
    def _normalize(self):
        """Normalize centers to sum to 1"""
        total = np.sum(self.centers)
        if total > 0:
            self.centers = self.centers / total
    
    def relation_terms(self) -> Dict[Relation, float]:
        """Calculate the four relation term values"""
        c = self.centers
        return {
            Relation.DISCRETION: c[0] * c[1] * c[2],      # Timelike product
            Relation.MEANS: (c[0] + c[1]) * c[2],          # Regenerative sum
            Relation.GOAL: c[0] * c[3],                    # Reconciliation
            Relation.CONSEQUENCE: c[1] * c[2] * c[3]       # Spacelike product
        }
    
    def dyadic_pairs(self) -> Tuple[Tuple[float, float], Tuple[float, float]]:
        """
        Return the two orthogonal dyadic pairs:
        Universal: (Discretion, Means)
        Particular: (Goal, Consequence)
        """
        terms = self.relation_terms()
        universal = (terms[Relation.DISCRETION], terms[Relation.MEANS])
        particular = (terms[Relation.GOAL], terms[Relation.CONSEQUENCE])
        return universal, particular


# =============================================================================
# SYSTEM 4: Primary Creative Process (Enneagram)
# =============================================================================

class EnneagramPosition(Enum):
    """Nine positions of the enneagram"""
    POS_1 = 1  # Marketing
    POS_2 = 2  # Product Development
    POS_3 = 3
    POS_4 = 4  # Organization & Manning
    POS_5 = 5  # Product Processing
    POS_6 = 6
    POS_7 = 7  # Treasury
    POS_8 = 8  # Sales
    POS_9 = 9  # Mediating axis


@dataclass
class System4State:
    """
    System 4: Nine terms in the enneagram structure.
    
    The primary creative process with:
    - Six-pointed figure (particular centers i, ii, iii)
    - Mediating triangle (universal centers O, X)
    - 12-stage transformation cycle
    """
    positions: np.ndarray  # 9 position values
    stage: int = 0  # Current stage (0-11)
    
    def __init__(self, values: Optional[List[float]] = None, stage: int = 0):
        if values is None:
            values = [1/9] * 9
        self.positions = np.array(values)
        self.stage = stage % 12
        self._normalize()
    
    def _normalize(self):
        """Normalize positions to sum to 1"""
        total = np.sum(self.positions)
        if total > 0:
            self.positions = self.positions / total
    
    @property
    def six_pointed_positions(self) -> List[int]:
        """Positions in the six-pointed figure: 1,4,2,8,5,7"""
        return [1, 4, 2, 8, 5, 7]
    
    @property
    def mediating_positions(self) -> List[int]:
        """Positions in the mediating triangle: 3,6,9"""
        return [3, 6, 9]
    
    def transformation_matrix(self) -> np.ndarray:
        """
        Generate the transformation matrix for one stage.
        
        Based on Campbell's transformation rules:
        - Particular sets alternate between positions 8,7,4 and 1,2,5
        - Universal sets flip with the mediating triangle
        """
        # Simplified transformation matrix
        # Full implementation would follow the exact rules from Fisherman's Guide
        T = np.eye(9)
        
        # Six-pointed figure transformations (1→4→2→8→5→7→1)
        sequence = [0, 3, 1, 7, 4, 6]  # 0-indexed
        for i in range(len(sequence)):
            j = (i + 1) % len(sequence)
            T[sequence[i], sequence[i]] = 0.5
            T[sequence[j], sequence[i]] = 0.5
        
        return T
    
    def advance_stage(self) -> 'System4State':
        """Advance to the next stage in the 12-stage cycle"""
        T = self.transformation_matrix()
        new_positions = T @ self.positions
        return System4State(list(new_positions), self.stage + 1)
    
    def expressive_regenerative_mode(self) -> str:
        """Determine if current stage is expressive or regenerative"""
        # 7 expressive, 5 regenerative in 12-step cycle
        expressive_stages = [0, 1, 2, 4, 5, 8, 9]
        return "expressive" if self.stage in expressive_stages else "regenerative"


# =============================================================================
# SYSTEM 5: Tetrahedral Integration
# =============================================================================

@dataclass
class TetrahedralVertex:
    """A vertex in the tetrahedral structure"""
    id: int
    value: float
    thread_id: int  # Which of 4 threads this vertex represents


@dataclass
class DyadicEdge:
    """An edge connecting two vertices (dyadic relationship)"""
    vertex1_id: int
    vertex2_id: int
    weight: float


@dataclass
class TriadicFace:
    """A face of the tetrahedron (triadic bundle)"""
    vertex_ids: Tuple[int, int, int]
    edges: Tuple[DyadicEdge, DyadicEdge, DyadicEdge]


class System5State:
    """
    System 5: Tetrahedral integration with 18 services.
    
    Structure:
    - 4 vertices (monadic threads)
    - 6 edges (dyadic relationships)
    - 4 faces (triadic bundles)
    - [[D-T]-[P-O]-[S-M]] pattern
    """
    
    def __init__(self):
        # Initialize 4 vertices
        self.vertices = [
            TetrahedralVertex(i, 0.25, i) for i in range(4)
        ]
        
        # Initialize 6 edges (all pairs of vertices)
        self.edges = []
        for i in range(4):
            for j in range(i+1, 4):
                self.edges.append(DyadicEdge(i, j, 1.0/6))
        
        # Initialize 4 faces (each face excludes one vertex)
        self.faces = []
        for excluded in range(4):
            vertex_ids = tuple(i for i in range(4) if i != excluded)
            face_edges = tuple(
                e for e in self.edges 
                if e.vertex1_id in vertex_ids and e.vertex2_id in vertex_ids
            )
            self.faces.append(TriadicFace(vertex_ids, face_edges))
        
        # 18 services in [[D-T]-[P-O]-[S-M]] pattern
        self.services = self._init_services()
    
    def _init_services(self) -> Dict[str, float]:
        """Initialize the 18 services"""
        polarities = ['D-T', 'P-O', 'S-M']
        services = {}
        for polarity in polarities:
            for i in range(6):  # 6 services per polarity
                key = f"{polarity}_{i+1}"
                services[key] = 1.0/18
        return services
    
    def phase_angle(self, stream: int) -> float:
        """
        Get phase angle for one of 3 concurrent streams.
        Streams are 120° (4 steps) apart.
        """
        return (stream * 120) % 360
    
    def step_triad(self, step: int) -> Tuple[int, int, int]:
        """
        Get the triad of steps that occur together.
        Steps grouped: {1,5,9}, {2,6,10}, {3,7,11}, {4,8,12}
        """
        base = (step - 1) % 4 + 1
        return (base, base + 4, base + 8)


# =============================================================================
# ENERGY FLOW EQUATIONS
# =============================================================================

def energy_conservation(state: System4State) -> float:
    """
    Verify energy conservation in System 4.
    Total energy should remain constant through transformations.
    """
    return np.sum(state.positions)


def flow_rate(source: float, sink: float, conductance: float = 1.0) -> float:
    """
    Calculate flow rate between two centers.
    Based on potential difference and conductance.
    """
    return conductance * (source - sink)


def transformation_energy(before: System4State, after: System4State) -> float:
    """
    Calculate energy required for state transformation.
    """
    delta = after.positions - before.positions
    return np.sum(np.abs(delta))


# =============================================================================
# GEOMETRIC SYMMETRIES
# =============================================================================

def enneagram_rotation(positions: np.ndarray, steps: int = 1) -> np.ndarray:
    """
    Rotate the enneagram by a number of steps.
    The sequence 1→4→2→8→5→7 defines the rotation.
    """
    sequence = [0, 3, 1, 7, 4, 6, 2, 5, 8]  # 0-indexed, includes mediating
    new_positions = np.zeros(9)
    for i, pos in enumerate(sequence):
        new_idx = (i + steps) % 9
        new_positions[sequence[new_idx]] = positions[pos]
    return new_positions


def tetrahedral_rotation(vertices: List[TetrahedralVertex], axis: int) -> List[TetrahedralVertex]:
    """
    Rotate the tetrahedron around one of its symmetry axes.
    axis: 0-3 corresponds to rotation around each vertex
    """
    # Simplified rotation - permutes the other 3 vertices
    new_vertices = vertices.copy()
    others = [v for v in vertices if v.id != axis]
    # Cyclic permutation
    others = others[1:] + others[:1]
    j = 0
    for i, v in enumerate(new_vertices):
        if v.id != axis:
            new_vertices[i] = others[j]
            j += 1
    return new_vertices


# =============================================================================
# OEIS A000081 RELATIONSHIP
# =============================================================================

def rooted_trees(n: int) -> int:
    """
    Calculate the number of rooted trees with n nodes.
    OEIS A000081 sequence.
    
    This defines the relationship between nesting levels and terms:
    - 1 nest → 1 term
    - 2 nests → 2 terms
    - 3 nests → 4 terms
    - 4 nests → 9 terms
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    # A000081 values for small n
    a000081 = [0, 1, 1, 2, 4, 9, 20, 48, 115, 286]
    if n < len(a000081):
        return a000081[n]
    
    # For larger n, would need recursive calculation
    return -1  # Not implemented for large n


def nesting_to_terms(nesting_level: int) -> int:
    """
    Map nesting level to number of terms.
    Based on the user's abstract model relating to A000081.
    """
    mapping = {1: 1, 2: 2, 3: 4, 4: 9, 5: 18}
    return mapping.get(nesting_level, -1)


# =============================================================================
# DEMONSTRATION
# =============================================================================

if __name__ == "__main__":
    print("=== Cosmos System Mathematical Models ===\n")
    
    # System 1
    s1 = System1State()
    print(f"System 1 - Energy: {s1.energy()}")
    
    # System 2
    s2 = System2State(0.6, 0.4)
    print(f"System 2 - Polarity: {s2.polarity():.3f}, Term: {s2.term_value():.3f}")
    
    # System 3
    s3 = System3State([0.3, 0.2, 0.3, 0.2])
    terms = s3.relation_terms()
    print(f"System 3 - Relations: D={terms[Relation.DISCRETION]:.3f}, "
          f"M={terms[Relation.MEANS]:.3f}, G={terms[Relation.GOAL]:.3f}, "
          f"C={terms[Relation.CONSEQUENCE]:.3f}")
    
    # System 4
    s4 = System4State()
    print(f"System 4 - Stage: {s4.stage}, Mode: {s4.expressive_regenerative_mode()}")
    s4_next = s4.advance_stage()
    print(f"System 4 - After advance: Stage {s4_next.stage}")
    
    # System 5
    s5 = System5State()
    print(f"System 5 - Vertices: {len(s5.vertices)}, Edges: {len(s5.edges)}, "
          f"Faces: {len(s5.faces)}, Services: {len(s5.services)}")
    
    # OEIS relationship
    print(f"\nNesting → Terms mapping:")
    for n in range(1, 6):
        print(f"  {n} nests → {nesting_to_terms(n)} terms")
