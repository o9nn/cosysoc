# OEIS A000081 - Unlabeled Rooted Trees

## Source
- **File**: a000081(1).scm
- **Language**: Guile Scheme
- **Sequence**: A000081 in the Online Encyclopedia of Integer Sequences

---

## The Sequence

A000081 counts the number of **unlabeled rooted trees** with n nodes:

| n | a(n) | Description |
|---|------|-------------|
| 0 | 0 | Empty |
| 1 | 1 | Single node (root) |
| 2 | 1 | Root with one child |
| 3 | 2 | Linear or branching |
| 4 | 4 | Four distinct shapes |
| 5 | 9 | Nine distinct shapes |
| 6 | 20 | Twenty distinct shapes |
| 7 | 48 | ... |
| 8 | 115 | ... |
| 9 | 286 | ... |
| 10 | 719 | ... |

---

## The Recursive Formula

The key formula implemented in the Scheme code is:

```
∀ n ∈ ℕ⁺: a_{n+1} = (1/n) Σ_{k=1}^{n} (Σ_{d|k} d·a_d) · a_{n-k+1}
```

Where:
- `Σ_{d|k}` means sum over all divisors d of k
- `a_d` is the dth term of the sequence
- The outer sum runs from k=1 to n

### Implementation Details

```scheme
(define (a000081-recursive n)
  (cond
    ((< n 0) 0)
    ((= n 0) 0)
    ((= n 1) 1)
    (else
     (let loop ((k 1) (sum 0))
       (if (> k (- n 1))
           (/ sum (- n 1))
           (let* ((divisor-sum (sum-of-divisors k a000081-recursive))
                  (a-term (a000081-recursive (- n k)))
                  (term (* divisor-sum a-term)))
             (loop (+ k 1) (+ sum term))))))))
```

---

## Asymptotic Behavior

The sequence grows asymptotically as:

```
a_n ~ C · α^n · n^{-3/2}
```

Where:
- **α ≈ 2.9557652857** (the tree constant)
- **C ≈ 0.4399237** (a computed constant)

This exponential growth reflects the combinatorial explosion of tree structures.

---

## Connection to System 5

### System 5 Uses Rooted Forests, Not Trees

System 5 has **20 configurations** for 5 interfaces. This is **not** A000081(5) = 9.

Instead, System 5 uses **rooted forests** (collections of rooted trees), which is sequence **A033185**:

| n | A000081(n) | A033185(n) |
|---|------------|------------|
| 1 | 1 | 1 |
| 2 | 1 | 2 |
| 3 | 2 | 4 |
| 4 | 4 | 9 |
| 5 | 9 | **20** |
| 6 | 20 | 48 |

A033185(n) counts **partitions of n into parts, where each part is a rooted tree**.

### The Relationship

```
A033185(n) = Σ (product of A000081 values for partition parts)
```

For n=5, the 20 forests come from:
- 1 forest of a single 5-node tree (9 ways from A000081(5))
- Forests with multiple trees summing to 5 nodes (11 additional ways)

---

## Generating Function

The generating function for A000081 is:

```
A(x) = x · exp(Σ_{k=1}^∞ A(x^k)/k)
```

This functional equation encodes the recursive structure of trees.

---

## Key Properties

1. **Multiplicative Structure**: The divisor sum formula reflects how trees can be decomposed into subtrees

2. **Symmetry**: The symmetry σ(t) of a tree counts its automorphisms

3. **Matula Numbers**: Each rooted tree has a unique prime factorization encoding (Matula, 1968)

4. **Hopf Algebra**: Rooted trees form a Hopf algebra under grafting and cutting operations

---

## Python Equivalent

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def a000081(n):
    """Number of unlabeled rooted trees with n nodes."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    total = 0
    for k in range(1, n):
        divisor_sum = sum(d * a000081(d) for d in range(1, k+1) if k % d == 0)
        total += divisor_sum * a000081(n - k)
    
    return total // (n - 1)

# Generate sequence
for i in range(1, 11):
    print(f"a({i}) = {a000081(i)}")
```

---

## References

1. OEIS Foundation. (2024). A000081 - Number of unlabeled rooted trees with n nodes. https://oeis.org/A000081
2. Otter, R. (1948). The number of trees. *Annals of Mathematics*, 49(3), 583-599.
3. Matula, D. W. (1968). A natural rooted tree enumeration by prime factorization. *SIAM Review*, 10(2), 273.
