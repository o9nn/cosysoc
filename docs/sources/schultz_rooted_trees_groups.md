# Enumerations of Rooted Trees with an Application to Group Presentations

## Source
- **Author**: Phillip Schultz
- **Institution**: Department of Mathematics, University of Western Australia
- **Journal**: Discrete Mathematics 41 (1982) 199-214
- **Publisher**: North-Holland Publishing Company

---

## Overview

This seminal paper establishes a **fundamental isomorphism** between rooted trees and positive integers via prime factorization. This provides a number-theoretic representation of rooted trees that enables efficient enumeration and connects to abelian p-group presentations.

---

## Key Concepts

### 1. The Algebra of Rooted Trees (T, ⊗, p, 1)

Schultz defines an **algebra** on the set of rooted trees T with:

- **Identity**: **1** = the single-vertex tree (root only)
- **Binary operation ⊗**: For trees **u**, **v** ∈ T, **u⊗v** is obtained by identifying the roots of **u** and **v**
- **Unary operation p**: For tree **u**, **p(u)** is obtained by adding a new edge from the root of **u** to a new root

### Visual Example

If **u** = a tree with 2 children and **v** = a tree with 1 child + 1 grandchild:

```
u⊗v combines them at the root
p(u) adds a new root below u
```

### 2. The Fundamental Isomorphism φ

> **Theorem**: The mapping φ: 1 → 1 extends uniquely to an algebra isomorphism of N onto T.

Where N = (N, ×, p, 1) is the algebra of positive integers under:
- **Multiplication** (×)
- **p(n)** = the nth prime in natural order

This means:
- **φ(n × m) = φ(n) ⊗ φ(m)** (multiplication → root identification)
- **φ(p(n)) = p(φ(n))** (nth prime → adding a root)

### 3. The Prime Encoding (Matula Numbers)

Each rooted tree has a unique **Matula number** (positive integer encoding):

| Integer | Factorization | Tree | Bracket Notation |
|---------|---------------|------|------------------|
| 1 | 1 | • | () |
| 2 | p(1) | •-• | (()) |
| 3 | p(2) | •-•-• | ((())) |
| 4 | 2×2 | Y | (()()) |
| 5 | p(3) | chain-4 | (((()))) |
| 6 | 2×3 | | (())((())) |
| 7 | p(4) | | ((()()))  |
| ... | ... | ... | ... |

### 4. Table 1: First 200 Rooted Trees

The paper provides a complete enumeration of the first 200 rooted trees in bracket notation, indexed by their Matula number. Key entries:

| n | Bracket Notation | Description |
|---|------------------|-------------|
| 2 | () | Single edge |
| 3 | (()) | 2-chain |
| 4 | ()() | 2 leaves from root |
| 5 | ((())) | 3-chain |
| 6 | ()(()) | 1 leaf + 2-chain |
| 7 | (()()) | Binary tree |
| 8 | ()()() | 3 leaves from root |
| 9 | (())(())) | Two 2-chains |
| ... | ... | ... |

### 5. Terms in the Algebra T

A **term** in T satisfies:
1. **1** is a term
2. If **u** and **v** are terms, then **u⊗v** is a term
3. If **u** is a term, then **p(u)** is a term
4. Nothing else is a term

A term is **reduced** if it satisfies (1), (3), (4) and:
- (2') If **u** and **v** are reduced terms, neither of which is **1**, then **u⊗v** is reduced

A term is **completely reduced** if:
- (2'') If **u** and **v** are completely reduced terms, neither of which is **1**, such that **u < v**, then **u⊗v** is completely reduced

### 6. Connection to Abelian p-Groups

Hales (1971) showed that each rooted tree defines an abelian p-group. Two trees are **similar** if they define isomorphic groups.

> **Theorem**: The similarity classes of rooted trees correspond to the presentations of finite abelian p-groups.

This connects the combinatorics of rooted trees to abstract algebra.

---

## Relevance to Time Crystal Networks

### 1. Matula Numbers as Network Indices

Each TCN architecture can be uniquely identified by its **Matula number**:

| Matula # | Tree | TCN Architecture |
|----------|------|------------------|
| 1 | • | Single oscillator |
| 2 | •-• | 2-level chain |
| 3 | •-•-• | 3-level chain |
| 4 | Y | Binary split |
| 5 | 4-chain | Deep hierarchy |
| 7 | (()())) | Asymmetric binary |

### 2. Prime Factorization = Module Composition

The isomorphism φ means:
- **Multiplying Matula numbers** = combining modules at the root
- **Taking the nth prime** = adding a hierarchical level

This provides a **canonical way to compose TCN modules**.

### 3. Group Structure

The connection to abelian p-groups suggests that TCN architectures have an underlying **group structure** that governs their behavior. Similar trees (same group) may have similar computational properties.

### 4. Efficient Enumeration

The number-theoretic representation enables efficient algorithms for:
- Generating all TCN architectures up to a given size
- Testing isomorphism between architectures
- Finding canonical forms

---

## Key Formulas

### Number of Ordered Trees Isomorphic to φ(n)

> **Theorem 1**: For each positive integer n, let N(n) be the number of ordered rooted trees isomorphic to a given rooted tree φ(n).

If n = p(n₁)^k₁ × p(n₂)^k₂ × ... × p(nᵣ)^kᵣ, then:

```
N(n) = (k₁ + k₂ + ... + kᵣ)! / (k₁! × k₂! × ... × kᵣ!) × N(n₁)^k₁ × N(n₂)^k₂ × ... × N(nᵣ)^kᵣ
```

This is a multinomial coefficient times a product of recursive terms.

### Height Distribution

The **height** h(n) of tree φ(n) satisfies:
- h(1) = 0
- h(p(n)) = h(n) + 1
- h(n × m) = max(h(n), h(m))

---

## References

1. Schultz, P. (1982). Enumerations of rooted trees with an application to group presentations. *Discrete Mathematics*, 41, 199-214.
2. Göbel, F. (1980). On a 1-1 correspondence between rooted trees and natural numbers. *Journal of Combinatorial Theory, Series B*, 29(2), 141-143.
3. Read, R.C. (1972). The coding of various kinds of unlabeled trees. *Graph Theory and Computing*, 153-182.
4. Hales, A.W. (1971). On the isomorphism problem for finite abelian groups. *Notices of the American Mathematical Society*, 18, 808.
5. Matula, D.W. (1968). A natural rooted tree enumeration by prime factorization. *SIAM Review*, 10(2), 273.


---

## Additional Theorems

### Theorem 2: Properties of Completely Reduced Terms

Let **u** be a completely reduced term in T. Then:

1. The number of occurrences of p in **u** = the number of edges of **u**
2. The number of occurrences of **1** in **u** = 1 + (the number of occurrences of ⊗ in **u**) = the number of leaves of **u**
3. Each pair of matched brackets contains a completely reduced term of T, so represents a rooted sub-tree of **u**

### Theorem 3: Bounds on Matula Numbers

Let φ(n) be a rooted tree with e ≥ 3 edges, and let e = 3i + j, where 0 ≤ j < 3.

1. If j = 0, then 5^i ≤ n ≤ p^(e-3)(8)
2. If j = 1, then 9 × 5^(i-1) ≤ n ≤ p^(e-3)(8)
3. If j = 2, then 3 × 5^(i-1) ≤ n ≤ p^(e-3)(8)

In each case, upper and lower bounds can be achieved.

### Theorem 4: Bounds with Leaf Constraints

Let φ(n) be a rooted tree with e ≥ 3 edges and l ≥ 3 leaves. Let e = li + j, where 0 ≤ j < l. Then:

```
p^i(1)^(l-j) × p^(i+1)(1)^j ≤ n ≤ p^(e-l)(2^l)
```

Both bounds are achieved.

### Table 2: Tree Counts by Edges (E) and Leaves (L)

| L\E | 4 | 5 | 6 | 7 | 8 |
|-----|---|---|---|---|---|
| 2 | 4 | 6 | 9 | 12 | 16 |
| 3 | 3 | 8 | 18 | 35 | 62 |
| 4 | - | 4 | 14 | 39 | 97 |
| 5 | - | - | 5 | 21 | 72 |
| 6 | - | - | - | 6 | 30 |
| 7 | - | - | - | - | 7 |

### Key Insight: Minimal vs Maximal Trees

- **Minimal tree** (smallest Matula number): Consists of l chains, as near equal in length as possible, joined at the root
- **Maximal tree** (largest Matula number): Consists of a chain of length e - l, topped by an l-leaved star

**Example for 5 edges**:
- Minimum (n = 15): Balanced tree
- Maximum (n = 67): Chain with star on top

---

## Section 5: Simple Presentations of Finite Abelian p-Groups

### The Height Distribution

For a finite abelian p-group G:
- The **exponent** e is the minimal value where p^e·G = 0
- An element x ∈ G has **height** n if x ∈ p^n·G \ p^(n+1)·G
- The **height distribution** (v₀, v₁, ..., v_(e-1)) is a complete invariant

### The Ulm Invariant

The sequence (u₀, u₁, ..., u_(e-1)) where:
```
u_n = v_n - v_(n+1)  for n < e-1,    u_(e-1) = v_(e-1)
```

is the **Ulm invariant** of G. Two groups are isomorphic iff they have the same Ulm invariant.

### Simply Presented Groups (Crawley-Hales, 1969)

A **simply presented** abelian p-group has presentation G = ⟨X; R⟩ where:
- X is an irredundant set of generators
- All relations in R are of the form px = 0 or px = y

> **Key Theorem**: A simple presentation ⟨X; R⟩ defines a unique rooted tree T(⟨X; R⟩) as follows:
> - Vertices are X ∪ {0}, where 0 is the root
> - There is an arrow from vertex x to vertex y iff px = y

Conversely, a rooted tree **u** defines a simple presentation P(**u**) = ⟨X; R⟩.

### The Fundamental Correspondence

> **Theorem (Hales)**: Two rooted trees are similar (define isomorphic groups) iff they have the same height distribution.

This establishes a **bijection** between:
- Similarity classes of rooted trees
- Isomorphism classes of finite abelian p-groups

---

## Implications for Time Crystal Networks

### 1. Group-Theoretic Classification of TCN Architectures

Since each rooted tree defines an abelian p-group, TCN architectures can be classified by their associated group structure:

| Tree Property | Group Property | TCN Interpretation |
|---------------|----------------|-------------------|
| Height | Exponent | Maximum depth of processing |
| Leaves | Generators | Number of independent inputs |
| Edges | Relations | Number of connections |
| Ulm invariant | Structure | Information flow pattern |

### 2. Similarity Classes = Equivalent Architectures

Two TCN architectures are **computationally equivalent** if their trees are similar (same height distribution). This provides a principled way to identify redundant architectures.

### 3. Minimal/Maximal Architectures

For a given number of edges (connections) and leaves (inputs):
- **Minimal architecture**: Most balanced, smallest Matula number
- **Maximal architecture**: Most hierarchical, largest Matula number

This guides architecture selection based on desired properties.

### 4. The Ulm Invariant as a Network Signature

The Ulm invariant provides a **canonical signature** for each TCN architecture that captures its essential structure independent of labeling.
