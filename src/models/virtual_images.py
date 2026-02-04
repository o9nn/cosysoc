"""
Virtual Image Analysis for System 5

This module analyzes the 3 configurations of System 5 that generate "virtual images"
as described in Robert Campbell's framework.

Based on the text analysis:
- "bi-polar coalescence of Emotional Knowledge (3) <↔> Routine(4) <↔> Form(5)"
- "Host Idea(1) and Conscious Knowledge(2) are coalesced as One"
- "R1, R2, and R3 are together a single coherent realization"

The 3 virtual image configurations are identified as the 3 configurations with
exactly 3 trees (factors), which matches the R1-R2-R3 pattern described.

References:
- Mathar, R.J. (2016). "Topologically Distinct Sets of Non-Intersecting Circles
  in the Plane." arXiv:1603.00077
- Campbell, R. (1985). "Fisherman's Guide: A Systems Approach to Creativity
  and Organization." New Science Library/Shambhala.
"""

from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass, field
from enum import Enum

from .rooted_forests import (
    RootedForest, RootedForestGenerator, ForestAnalysis,
    analyze_forest, get_system5_configurations, group_by_tree_count
)


# =============================================================================
# SYSTEM 5 INTERFACE DEFINITIONS
# =============================================================================

class Interface(Enum):
    """The five active interfaces of System 5."""
    HOST_IDEA = 1           # Host Idea
    CONSCIOUS_KNOWLEDGE = 2  # Conscious Knowledge (Cerebral)
    EMOTIONAL_KNOWLEDGE = 3  # Emotional Knowledge (Limbic)
    ROUTINE = 4             # Routine
    FORM = 5                # Form


class FeedbackLoop(Enum):
    """The three feedback loops in the virtual image configuration."""
    R1 = "R1"  # Internal balance: Emotional Knowledge (3) → Routine (4)
    R2 = "R2"  # External balance: Routine (4) → Form (5)
    R3 = "R3"  # Coalescence: Host (1) + Conscious (2) working through R1 and R2


# =============================================================================
# VIRTUAL IMAGE CONFIGURATION
# =============================================================================

@dataclass
class VirtualImageConfiguration:
    """
    A configuration that generates a virtual image.
    
    The virtual image arises from the specific structural arrangement of the
    five interfaces that creates a "stereoscopic perception" - a potential
    behavior felt as an urge but not necessarily acted upon.
    """
    forest: RootedForest
    analysis: ForestAnalysis
    
    # Structural properties
    coalescence_pattern: str
    feedback_structure: Dict[FeedbackLoop, str]
    
    # Virtual image properties
    virtual_perception_type: str
    consciousness_integration: str
    
    def describe(self) -> str:
        """Generate a human-readable description of this configuration."""
        lines = [
            f"Configuration: {self.analysis.bracket_notation}",
            f"Tree sizes: {self.analysis.tree_sizes}",
            f"Max depth: {self.analysis.max_depth}",
            "",
            f"Coalescence Pattern: {self.coalescence_pattern}",
            "",
            "Feedback Structure:",
        ]
        for loop, desc in self.feedback_structure.items():
            lines.append(f"  {loop.value}: {desc}")
        
        lines.extend([
            "",
            f"Virtual Perception: {self.virtual_perception_type}",
            f"Consciousness Integration: {self.consciousness_integration}",
        ])
        
        return "\n".join(lines)


# =============================================================================
# VIRTUAL IMAGE IDENTIFICATION
# =============================================================================

def identify_virtual_image_configurations() -> List[VirtualImageConfiguration]:
    """
    Identify and analyze the 3 configurations that generate virtual images.
    
    Based on the analysis of Campbell's text, the virtual image configurations
    are the 3 configurations with exactly 3 trees (factors), corresponding to
    the R1-R2-R3 coherent realization pattern.
    """
    forests = get_system5_configurations()
    by_count = group_by_tree_count(forests)
    
    # The 3-tree configurations are the virtual image generators
    three_tree_forests = by_count.get(3, [])
    
    configurations = []
    for i, forest in enumerate(three_tree_forests):
        analysis = analyze_forest(forest)
        config = _create_virtual_image_config(forest, analysis, i)
        configurations.append(config)
    
    return configurations


def _create_virtual_image_config(forest: RootedForest, analysis: ForestAnalysis,
                                  index: int) -> VirtualImageConfiguration:
    """Create a detailed virtual image configuration analysis."""
    
    tree_sizes = analysis.tree_sizes
    
    # Determine coalescence pattern based on tree structure
    if tree_sizes == [3, 1, 1]:
        if analysis.max_depth == 2:
            coalescence = "Deep 3-coalescence: (3-4-5) nested + (1) + (2) separate"
            perception = "Hierarchical virtual perception with nested emotional-routine-form integration"
        else:
            coalescence = "Flat 3-coalescence: (3-4-5) flat + (1) + (2) separate"
            perception = "Parallel virtual perception with concurrent emotional-routine-form processing"
    elif tree_sizes == [2, 2, 1]:
        coalescence = "Dual 2-coalescence: (1-2) + (3-4) + (5) or (1-2) + (4-5) + (3)"
        perception = "Balanced virtual perception with symmetric coalescence pairs"
    else:
        coalescence = f"Mixed coalescence: sizes {tree_sizes}"
        perception = "Complex virtual perception"
    
    # Define feedback structure
    feedback = {
        FeedbackLoop.R1: "Emotional Knowledge (3) ↔ Routine (4): Internal balance",
        FeedbackLoop.R2: "Routine (4) ↔ Form (5): External balance with physical world",
        FeedbackLoop.R3: "Host (1) + Conscious (2): Working through R1 and R2 as single process",
    }
    
    # Consciousness integration description
    if tree_sizes == [3, 1, 1]:
        consciousness = "Host and Conscious Knowledge relate independently while 3-4-5 form integrated perception"
    else:
        consciousness = "Balanced integration with symmetric coalescence supporting stereoscopic perception"
    
    return VirtualImageConfiguration(
        forest=forest,
        analysis=analysis,
        coalescence_pattern=coalescence,
        feedback_structure=feedback,
        virtual_perception_type=perception,
        consciousness_integration=consciousness,
    )


# =============================================================================
# EXPRESSIVE AND REGENERATIVE VARIANTS
# =============================================================================

@dataclass
class VariantPair:
    """
    A pair of Expressive and Regenerative variants.
    
    The text mentions: "There are Expressive and Regenerative variants to the
    Term where Centers 1 and 2 exchange places."
    """
    expressive: VirtualImageConfiguration
    regenerative: VirtualImageConfiguration
    exchange_description: str


def analyze_variants(configs: List[VirtualImageConfiguration]) -> List[VariantPair]:
    """
    Analyze the Expressive and Regenerative variants among the configurations.
    
    Note: In the unlabeled forest representation, the exchange of Centers 1 and 2
    may not produce a distinct configuration (since forests are unlabeled).
    However, when labels are applied, each configuration can have variants.
    """
    # In the unlabeled case, we have 3 distinct configurations
    # Each can have Expressive and Regenerative labeled variants
    
    pairs = []
    for i, config in enumerate(configs):
        # Create a conceptual variant pair
        # In practice, the labeled variants would differ in which interface
        # is assigned to which tree position
        pair = VariantPair(
            expressive=config,
            regenerative=config,  # Same structure, different labeling
            exchange_description=f"Centers 1 and 2 exchange places in configuration {i+1}"
        )
        pairs.append(pair)
    
    return pairs


# =============================================================================
# VIRTUAL IMAGE MECHANISM
# =============================================================================

def explain_virtual_image_mechanism() -> str:
    """
    Explain how virtual images are generated in System 5.
    
    Based on Campbell's description in the source text.
    """
    return """
VIRTUAL IMAGE GENERATION IN SYSTEM 5
=====================================

The virtual image arises from the specific structural arrangement of the five
interfaces that creates a "stereoscopic perception" - a potential behavior
felt as an urge but not necessarily acted upon.

KEY MECHANISM:
--------------

1. BI-POLAR COALESCENCE
   The coalescence of Emotional Knowledge (3) ↔ Routine (4) ↔ Form (5) creates
   a bi-polar structure that reflects the internal-to-external balance:
   
   - R1: Internal balance between Emotional Knowledge (3) and Routine (4)
   - R2: External balance between Routine (4) and Form (5)
   
   This represents how we perceive the physical world emotionally (R2) and
   respond with animated behavior (R1).

2. HOST-CONSCIOUS COALESCENCE
   Host Idea (1) and Conscious Knowledge (2) are "coalesced as One" and relate
   from inside each other through R3, which also relates from inside Form (5)
   and Emotional Knowledge (3) in both directions via R1 and R2.

3. COHERENT REALIZATION
   R1, R2, and R3 work together as "a single coherent realization" - they are
   not separate processes but aspects of one integrated perception.

RESULT: VIRTUAL PERCEPTION
--------------------------

The subjective-to-objective disparity across the Routine (4) interface creates
a "virtual perception of a potential Routine" - a stereoscopic perception that
is Consciously perceived by the Host as an Emotionally felt urge to respond.

This virtual image is:
- A potential behavior, not necessarily acted upon
- Felt as an urge (e.g., wanting to go for a walk, sit and watch a sunset)
- The result of the specific 3-factor structure that enables R1-R2-R3 coherence

WHY 3 CONFIGURATIONS?
---------------------

The 3 configurations with exactly 3 trees (factors) in the forest representation
correspond to the 3 ways the five interfaces can be arranged to create this
specific R1-R2-R3 coherent realization pattern:

1. [((()))()()]  - Deep nested 3-coalescence with 2 singletons
2. [(()())()()]  - Flat 3-coalescence with 2 singletons  
3. [(())(())()]  - Dual 2-coalescence with 1 singleton

Each represents a different structural arrangement that still maintains the
essential property of having 3 distinct groupings (factors) that can support
the R1-R2-R3 feedback structure.
"""


# =============================================================================
# REPORTING
# =============================================================================

def print_virtual_image_report():
    """Print a comprehensive report on virtual image configurations."""
    print("=" * 70)
    print("SYSTEM 5 VIRTUAL IMAGE ANALYSIS")
    print("=" * 70)
    
    configs = identify_virtual_image_configurations()
    
    print(f"\nIdentified {len(configs)} virtual image configurations:")
    print("-" * 70)
    
    for i, config in enumerate(configs, 1):
        print(f"\n### Configuration {i} ###\n")
        print(config.describe())
        print()
    
    print("=" * 70)
    print("MECHANISM EXPLANATION")
    print("=" * 70)
    print(explain_virtual_image_mechanism())
    
    # Variant analysis
    print("=" * 70)
    print("EXPRESSIVE AND REGENERATIVE VARIANTS")
    print("=" * 70)
    
    variants = analyze_variants(configs)
    print(f"\nEach of the {len(variants)} configurations can have Expressive and")
    print("Regenerative variants where Centers 1 and 2 exchange places.")
    print("\nIn the unlabeled forest representation, these variants share the")
    print("same structure but differ in how the five interfaces are assigned")
    print("to the tree positions.")


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print_virtual_image_report()
