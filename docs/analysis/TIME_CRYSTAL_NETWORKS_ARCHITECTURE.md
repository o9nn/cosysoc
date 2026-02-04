# Time Crystal Networks: Unified Architecture Specification

## Overview

This document provides a comprehensive architectural specification for Time Crystal Networks (TCNs), unifying the nn4c (single neuron) and nn9c (whole brain) implementations with System 5 rooted forest structures.

---

## 1. Foundational Concepts

### 1.1 The Rooted Forest Basis

Every TCN is built on a **rooted forest** from the System 5 set. The 20 possible forests for 5 nodes provide the structural templates:

| Trees | Count | Configurations | TCN Interpretation |
|-------|-------|----------------|-------------------|
| 1 | 9 | Fully connected | Integrated processing |
| 2 | 8 | Two components | Dual-stream processing |
| **3** | **3** | **Virtual image** | **Conscious binding** |
| 4 | 0 | - | - |
| 5 | 0 | - | - |

The **3-tree configurations** (T03, T04, T06) are architecturally special—they enable the "virtual image" phenomenon that corresponds to conscious awareness.

### 1.2 Temporal Hierarchy

TCNs operate across multiple temporal scales, organized hierarchically:

```
Level 0 (8ms)    → Protein dynamics
Level 1 (26ms)   → Ion channels
Level 2 (52ms)   → Membrane dynamics
Level 3 (110ms)  → Axon initial segment
Level 4 (160ms)  → Dendritic integration
Level 5 (250ms)  → Synaptic plasticity
Level 6 (330ms)  → Soma processing
Level 7 (500ms)  → Network synchronization
Level 8 (1000ms) → Global rhythm
```

Each level has a characteristic **period** that determines its oscillatory frequency.

### 1.3 Phase Coupling

Oscillators at different levels are **phase-coupled**, meaning their relative phases influence each other. This coupling is the mechanism for information binding across temporal scales.

---

## 2. Module Specifications

### 2.1 Core Modules

#### `TimeCrystalOscillator`

The fundamental unit of a TCN. Each oscillator has:

- **Period** (τ): The characteristic oscillation period
- **Phase** (φ): Current phase in [0, 2π)
- **Amplitude** (A): Oscillation amplitude (learnable)
- **Offset** (θ): Phase offset (learnable)

**Dynamics**:
```
output(t) = A · sin(2π·t/τ + φ + θ)
```

#### `OscillatoryActivation`

A nonlinear activation function modulated by an oscillator:

```
σ_osc(x, t) = σ(x) · (1 + α·sin(2π·t/τ + φ))
```

Where σ is a base activation (e.g., tanh) and α is the modulation depth.

#### `FeedbackLoop`

Implements the Fi-lo (feedback loop) mechanism:

```
y = main(x) + β · feedback(y_prev)
```

Where β is the feedback strength (learnable).

#### `JunctionModule`

Implements different junction types between modules:

| Type | Description | Mechanism |
|------|-------------|-----------|
| `Ax-d` | Axo-dendritic | Unidirectional, excitatory |
| `El` | Electrical | Bidirectional, fast |
| `GlS` | Glial-synaptic | Modulatory, slow |

#### `RhythmModule`

Generates rhythmic patterns that modulate other modules:

```
rhythm(t) = Σ_k A_k · sin(2π·f_k·t + φ_k)
```

Where the sum is over harmonic components.

### 2.2 Container Modules

#### `TimeCrystalLevel`

A single level in the temporal hierarchy:

```lua
nn.TimeCrystalLevel(inputSize, outputSize, period, level)
```

Contains:
- `OscillatoryActivation` with the level's period
- Linear transformation
- Optional `FeedbackLoop`

#### `TimeCrystalNeuron` (nn4c)

A 9-level hierarchy modeling a single neuron:

```lua
nn.TimeCrystalNeuron({a, b, c, d})
```

Where `[a,b,c,d]` encodes:
- **a**: Spatial domains (dendrite, soma, axon)
- **b**: Functional layers per domain
- **c**: Temporal scales per layer
- **d**: Component types per scale

Default: `[3,4,3,3]`

#### `TimeCrystalBrain` (nn9c)

A 12-level hierarchy modeling the whole brain:

```lua
nn.TimeCrystalBrain({
   inputSize = 256,
   hiddenSize = 512,
   outputSize = 256,
   regionSize = 128,
})
```

Contains specialized modules for:
- Cortex (4 lobes)
- Cerebellum (3 lobes)
- Hippocampus (CA1-4, DG)
- Thalamus (relay nuclei)
- Hypothalamus (homeostatic nuclei)
- Cranial nerves (12 nerves)

---

## 3. System 5 Integration

### 3.1 Forest-to-Architecture Mapping

Each of the 20 System 5 configurations maps to a specific TCN architecture:

| Term | Forest | Tree Sizes | Architecture |
|------|--------|------------|--------------|
| T01 | `((((()))))` | [5] | Deep serial chain |
| T02 | `(())()()()` | [2,1,1,1] | Hub-and-spoke |
| **T03** | `(())(())()` | [2,2,1] | **Balanced dual + singleton** |
| **T04** | `(()())()()` | [3,1,1] | **Asymmetric triad** |
| T05 | `(()())(())` | [3,2] | Dual-stream |
| **T06** | `((()))()()` | [3,1,1] | **Hierarchical triad** |
| T07 | `((()))(())` | [3,2] | Deep + shallow |
| ... | ... | ... | ... |
| T20 | `()()()()()` | [1,1,1,1,1] | Fully parallel |

### 3.2 Virtual Image Architectures

The three virtual image configurations have special architectural significance:

#### T03: Balanced Dual + Singleton `(())(())()`

```
     [2]        [2]      [1]
    /   \      /   \      |
   O     O    O     O     O
```

**Architecture**: Two parallel 2-level streams plus an independent singleton. The streams process complementary information, and the singleton provides a reference signal.

**Neural Correlate**: Limbic system (emotional processing)

**Use Case**: Empathy, emotional understanding, affective computing

#### T04: Asymmetric Triad `(()())()()` 

```
       [3]        [1]    [1]
      / | \        |      |
     O  O  O       O      O
```

**Architecture**: One 3-level hierarchical stream plus two independent singletons. The hierarchy provides deep processing, while the singletons provide context.

**Neural Correlate**: Parasympathetic nervous system (action restraint)

**Use Case**: Self-control, inhibition, decision-making under uncertainty

#### T06: Hierarchical Triad `((()))()()` 

```
       [3]        [1]    [1]
        |          |      |
        O          O      O
        |
        O
        |
        O
```

**Architecture**: One deeply nested 3-level chain plus two independent singletons. The chain provides serial, hierarchical processing.

**Neural Correlate**: Motor cortex (somatic response initiation)

**Use Case**: Motor planning, action sequencing, robotics

### 3.3 Triadic Organization

The 20 configurations organize into three triads:

| Triad | Brain System | Terms | Characteristic |
|-------|--------------|-------|----------------|
| **Cerebral** | Neocortex | T01, T05, T07, T09, T11, T13, T14, T16, T17, T18 | High nesting depth |
| **Autonomic** | Limbic | T02, T03, T04, T10 | Moderate fragmentation |
| **Somatic** | Basal | T06, T08, T12, T15, T19, T20 | Low nesting depth |

---

## 4. B-Series Connection

### 4.1 TCN as B-Series Expansion

The forward pass of a TCN can be written as a B-series:

```
y = y₀ + Σ_t χ(t) · (1/σ(t)) · F(t) · h^|t|
```

Where:
- **t** is a rooted tree (from the TCN's forest structure)
- **χ(t)** is the network's weight for tree t
- **σ(t)** is the tree's symmetry
- **F(t)** is the elementary differential for tree t
- **h** is the time step

### 4.2 Order Conditions

A TCN satisfies **order p** if its B-series matches the exact solution up to trees of order p. This provides a principled way to analyze the approximation quality of a TCN.

### 4.3 Training as Coefficient Optimization

Training a TCN is equivalent to finding the B-series coefficients χ(t) that minimize a loss function. The `TimeCrystalCriterion` we developed implements this.

---

## 5. Implementation Guidelines

### 5.1 Choosing a Forest Structure

1. **For integrated processing** (e.g., classification): Use 1-tree configurations (T01, T07, T09, T11, T16, T17, T18)

2. **For dual-stream processing** (e.g., comparison): Use 2-tree configurations (T05, T07, T14, T19)

3. **For conscious binding / virtual images**: Use 3-tree configurations (T03, T04, T06)

4. **For parallel processing** (e.g., multi-modal): Use high-tree configurations (T02, T20)

### 5.2 Setting Temporal Scales

Use the nn4c/nn9c temporal hierarchy as a guide:

```python
TEMPORAL_SCALES = {
    0: 0.008,   # 8ms
    1: 0.026,   # 26ms
    2: 0.052,   # 52ms
    3: 0.110,   # 110ms
    4: 0.160,   # 160ms
    5: 0.250,   # 250ms
    6: 0.330,   # 330ms
    7: 0.500,   # 500ms
    8: 1.000,   # 1000ms
}
```

### 5.3 Training Protocol

1. **Initialize** phases randomly in [0, 2π)
2. **Train** with `TimeCrystalCriterion` (includes temporal coherence penalty)
3. **Advance time** with `model:step(dt)` after each forward pass
4. **Reset** periodically with `model:reset()` to clear memory traces

### 5.4 Hyperparameters

| Parameter | Description | Recommended Range |
|-----------|-------------|-------------------|
| `α` (modulation depth) | Oscillation influence | 0.1 - 0.5 |
| `β` (feedback strength) | Feedback loop gain | 0.1 - 0.3 |
| `temporal_weight` | Coherence penalty weight | 0.01 - 0.1 |
| `dt` (time step) | Simulation time step | 0.001 - 0.01 |

---

## 6. Example Architectures

### 6.1 TCN for Emotion Recognition (T03)

```lua
-- Balanced dual + singleton for empathy
local tcn = nn.Sequential()
   :add(nn.Concat(2)
      :add(nn.TimeCrystalLevel(64, 32, 0.250, 5))  -- Stream 1
      :add(nn.TimeCrystalLevel(64, 32, 0.250, 5))  -- Stream 2
      :add(nn.TimeCrystalLevel(64, 16, 0.330, 6))) -- Singleton
   :add(nn.Linear(80, 7))  -- 7 basic emotions
```

### 6.2 TCN for Motor Planning (T06)

```lua
-- Hierarchical triad for action sequencing
local tcn = nn.Sequential()
   :add(nn.Concat(2)
      :add(nn.Sequential()
         :add(nn.TimeCrystalLevel(64, 64, 0.052, 2))
         :add(nn.TimeCrystalLevel(64, 64, 0.110, 3))
         :add(nn.TimeCrystalLevel(64, 32, 0.160, 4)))  -- Deep chain
      :add(nn.TimeCrystalLevel(64, 16, 0.250, 5))      -- Singleton 1
      :add(nn.TimeCrystalLevel(64, 16, 0.330, 6)))     -- Singleton 2
   :add(nn.Linear(64, 10))  -- 10 motor commands
```

### 6.3 TCN for Full Brain Simulation (nn9c)

```lua
local brain = nn.TimeCrystalBrain({
   inputSize = 256,
   hiddenSize = 512,
   outputSize = 256,
   regionSize = 128,
})
```

---

## 7. Future Extensions

### 7.1 System 6 and Beyond

System 6 has 48 configurations, System 7 has 115. These provide increasingly rich architectural templates for more complex TCNs.

### 7.2 Learnable Forest Structure

Instead of fixing the forest structure, allow the network to **learn** its own optimal structure during training.

### 7.3 Continuous-Time TCNs

Replace discrete time steps with continuous-time dynamics using Neural ODEs.

### 7.4 Quantum Time Crystals

Explore connections to quantum time crystals and quantum computing.

---

## References

1. Butcher, J.C. (2021). *B-Series: Algebraic Analysis of Numerical Methods*. Springer.
2. Campbell, R. (1985). *Fisherman's Guide: A Systems Approach to Creativity and Organization*. New Science Library/Shambhala.
3. Bandyopadhyay, A. (2020). *Nanobrain: The Making of an Artificial Brain from a Time Crystal*. CRC Press.
4. Chen, R.T.Q., et al. (2018). Neural Ordinary Differential Equations. *NeurIPS*.
