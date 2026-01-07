# Cosmos System of Consciousness (cosysoc)

A systematic reconstruction of Robert Campbell's Systems 1-5 framework from "Fisherman's Guide: A Systems Approach to Creativity and Organization" (1985), with modern visualizations, mathematical formulations, and interactive animations.

## Overview

This repository preserves and extends the work of **Robert Campbell (1936-2021)**, who developed a comprehensive systems theory that bridges subjective experience and objective organization. The framework describes how consciousness and creativity emerge through a staged development process from unity (System 1) to complex creative processes (System 4 and beyond).

## The Systems Framework

| System | Nodes | Terms (A000081) | Clusters (A000055) | Key Concept | Geometric Form |
|--------|-------|-----------------|-------------------|-------------|----------------|
| **0** | 1 | 1 | 1 | The Void - primordial potential | Point |
| **1** | 2 | 1 | 1 | Universal wholeness, unity with sky | Circle |
| **2** | 3 | 2 | 1 | Perceptive wholeness, subjective/objective | Line/Dyad |
| **3** | 4 | 4 | 2 | Four Relations: Discretion, Means, Goal, Consequence | Triangle |
| **4** | 5 | 9 | 3 | Primary creative process, enneagram | Enneagram |
| **5** | 6 | 20 | 6 | Pentachoron with [[D-T]-[P-O]-[S-M]] pattern | Tetrahedron |

## Repository Structure

```
cosysoc/
├── README.md                 # This file
├── docs/                     # Documentation and theory
│   ├── SYSTEMS_DIAGRAMS_CATALOG.md
│   ├── system1.md           # System 1: Universal Wholeness
│   ├── system2.md           # System 2: Perceptive Wholeness
│   ├── system3.md           # System 3: Four Relations
│   ├── system4.md           # System 4: Creative Process
│   └── system5.md           # System 5: Tetrahedral Integration
├── diagrams/                 # Visual representations
│   ├── originals/           # Scanned diagrams from source
│   └── enhanced/            # Digitized and enhanced versions
├── src/                      # Source code
│   ├── models/              # Mathematical models
│   ├── animations/          # Animation generators
│   └── visualizations/      # Interactive visualizations
└── animations/               # Generated animation files
```

## Key Concepts

### System 1: Universal Wholeness
The ground state representing the relationship of all things to indeterminate sky. Everything manifests as a whole within universal wholeness through an unbounded active interface between an absolute center and an absolute periphery.

### System 2: Perceptive Wholeness
Two centers define two modes (subjective and objective) related together as a "term" called perceptive wholeness. This introduces the fundamental duality that underlies all subsequent systems.

### System 3: Four Relations
Four possible ways that three centers can relate to one another:
1. **Discretion** (Relation 1): Timelike succession - Idea → Routine → Formation
2. **Means** (Relation 2): Regenerative mode with countercurrent identities
3. **Goal** (Relation 3): Complete reconciliation of center and periphery
4. **Consequence** (Relation 4): Three mutually independent yet related centers

### System 4: Primary Creative Process
Nine terms generated from five sets of four energy interfaces, represented by the enneagram. The transformation pattern follows:
- Particular sets take alternate steps to see themselves in the mirror
- Universal sets take double steps to flip themselves round with the mirror

### System 5: Tetrahedral Integration
A tetradic system of 4 tensor bundles, each containing a triadic system of 3 dyadic edges. The [[D-T]-[P-O]-[S-M]] pattern represents 18 services organized into triads.

## Mathematical Foundation: OEIS A000081/A000055

The systems are rigorously grounded in combinatorial mathematics:

- **Term Counts (A000081)**: The number of terms at System n equals A000081(n+1), the count of rooted trees with n+1 unlabeled nodes
- **Cluster Counts (A000055)**: Terms group into A000055(n+1) equivalence classes via the **flip transform** (re-rooting)
- **State transitions**: Deterministic transformation matrices
- **Energy flows**: Conservation and transformation equations
- **Geometric symmetries**: Tetrahedral and enneagram rotations

See [OEIS A000081/A000055 Paradigm](docs/OEIS_A000081_A000055_PARADIGM.md) for the complete mathematical formalization.

## Applications

This framework has been applied to:
- **Neural Networks** (cosys-xnn): Cognitive function and brain regions
- **Organizations** (cosys-org): Business structure and enterprise ecosystems
- **Reservoir Computing** (cosys-esn): Echo state networks and membrane computing
- **Cell Biology** (cosys-cell): Eukaryotic cells and organelles
- **Integumentary System** (cosys-skin): Multi-scale skin models

## Credits

- **Robert Campbell** (1936-2021): Original author of "Fisherman's Guide" and developer of the Systems framework
- **Ken Wilber**: General editor of the New Science Library series
- This repository is maintained to preserve and extend Bob Campbell's legacy

## License

This work is dedicated to preserving and extending the intellectual legacy of Robert Campbell. The original diagrams are from "Fisherman's Guide: A Systems Approach to Creativity and Organization" (1985, New Science Library/Shambhala).

## Related Projects

- **[cosmic-sys-lib](https://github.com/o9nn/cosmic-sys-lib)**: C++ library implementing the OEIS-aligned system hierarchy with rooted tree generation, flip transform clustering, and SVG visualization

## References

1. Campbell, R. (1985). *Fisherman's Guide: A Systems Approach to Creativity and Organization*. New Science Library/Shambhala.
2. Campbell, R. *Science and Cosmic Order* (related work on cosmic systems)
3. OEIS A000081: Number of rooted trees with n unlabeled nodes. https://oeis.org/A000081
4. OEIS A000055: Number of unrooted trees with n unlabeled nodes. https://oeis.org/A000055
