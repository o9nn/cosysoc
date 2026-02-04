"""
Cosmos Systems Mathematical Models

This package provides mathematical models for the Cosmos Systems framework,
including OEIS-aligned tree generation, rooted forest enumeration, and
virtual image analysis.

Modules:
- oeis_trees: Rooted tree generation (A000081) and flip transform (A000055)
- rooted_forests: Rooted forest generation for non-intersecting circles
- virtual_images: Virtual image analysis for System 5
- systems_math: General mathematical utilities
- projective_geometry: Projective geometry models
"""

from .oeis_trees import (
    A000081, A000055,
    TreeNode, RootedTree,
    RootedTreeGenerator, FlipTransform,
    SystemDefinition, get_system_definitions,
    term_count_for_level, cluster_count_for_level,
)

from .rooted_forests import (
    A033185,
    RootedForest, RootedForestGenerator,
    ForestAnalysis, analyze_forest,
    get_system5_configurations,
    group_by_tree_count, group_by_max_depth, group_by_tree_sizes,
)

from .virtual_images import (
    Interface, FeedbackLoop,
    VirtualImageConfiguration,
    identify_virtual_image_configurations,
    explain_virtual_image_mechanism,
)

__all__ = [
    # OEIS sequences
    'A000081', 'A000055', 'A033185',
    
    # Tree structures
    'TreeNode', 'RootedTree', 'RootedForest',
    
    # Generators
    'RootedTreeGenerator', 'RootedForestGenerator', 'FlipTransform',
    
    # System definitions
    'SystemDefinition', 'get_system_definitions',
    'term_count_for_level', 'cluster_count_for_level',
    
    # Forest analysis
    'ForestAnalysis', 'analyze_forest',
    'get_system5_configurations',
    'group_by_tree_count', 'group_by_max_depth', 'group_by_tree_sizes',
    
    # Virtual images
    'Interface', 'FeedbackLoop',
    'VirtualImageConfiguration',
    'identify_virtual_image_configurations',
    'explain_virtual_image_mechanism',
]
