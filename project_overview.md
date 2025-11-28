# Quantum Machine Learning: Titanic Survival Classification

## Exact Implementation: Schuld & Petruccione Chapter 1.2

This project implements the **exact 4-qubit quantum squared-distance classifier** toy example from:
> **Schuld, M., & Petruccione, F. (2018)**  
> *Supervised Learning with Quantum Computers*, Springer  
> **Chapter 1.2** (pages 12-18)

### Toy Dataset (from book)
- **3 passengers total**
- **2 training examples** (Passengers 1 & 2 with known survival outcomes)
- **1 test example** (Passenger 3 with unknown survival to predict)

| Passenger | Ticket Price | Cabin Number | Survival |
|-----------|-------------|--------------|----------|
| Passenger 1 | $8,500 | 910 | 1 (Survived) |
| Passenger 2 | $1,200 | 2,105 | 0 (Died) |
| Passenger 3 | $7,800 | 1,121 | ? (To Predict) |

## Theory and Algorithm (4-Qubit Implementation)

### Background: Classical Squared-Distance Classifier

The squared-distance classifier is a simple pattern recognition algorithm that assigns a new data point to the class whose training examples have the smallest average squared distance to that point.

For a data point **x** and two classes with training data {**x₁⁽ᵃ⁾**, **x₂⁽ᵃ⁾**, ...} and {**x₁⁽ᵇ⁾**, **x₂⁽ᵇ⁾**, ...}, we compute:

- **dₐ²** = (1/Nₐ) Σᵢ ||**x** - **xᵢ⁽ᵃ⁾**||²
- **dᵦ²** = (1/Nᵦ) Σᵢ ||**x** - **xᵢ⁽ᵇ⁾**||²

The point is classified to class A if dₐ² < dᵦ², otherwise to class B.

### Why 4 Qubits? (Not 2!)

**Critical:** The book specifies **4 qubits**, not 2:
- **q0**: Ancilla qubit (for Hadamard interference)
- **q1-q2**: Feature qubits (encode 2D data)
- **q3**: Label qubit (survival outcome)

**Why 4?** To properly encode:
- P1 with label=1: 2 amplitudes
- P2 with label=0: 2 amplitudes  
- P3 with both labels: 4 amplitudes (duplicated for interference)

Total: 8 non-zero amplitudes → requires 4 qubits (2⁴=16 slots)

### Hadamard Interference Mechanism

The Hadamard gate on q0 creates quantum interference:

```
H = (1/√2) [1   1]
           [1  -1]
```

**Effect:**
- H|0⟩ = (|0⟩ + |1⟩)/√2  ← **constructive interference**
- H|1⟩ = (|0⟩ - |1⟩)/√2  ← **destructive interference**

After applying H to q0, the state contains:
- **q0=0 block**: Sum of P3_label0 and P3_label1 (kept by post-selection)
- **q0=1 block**: Difference (discarded by post-selection)

### Quantum Squared-Distance Classifier Algorithm (4-Qubit Version)

#### STEP 0: Min-Max Scaling to [0,1]

**Book's exact ranges:**
- Ticket price: [0, 10000] → scaled = price / 10000
- Cabin number: [0, 2500] → scaled = cabin / 2500

**Results (must match):**
- P1: [0.85, 0.36]
- P2: [0.12, 0.84]
- P3: [0.78, 0.45]

#### STEP A: L2 Normalization

Normalize to unit vectors: **x_norm = x / ||x||₂**

**Results (must match):**
- P1: [0.921, 0.390], label=1
- P2: [0.141, 0.990], label=0
- P3: [0.866, 0.500], label=?

#### STEP B: Amplitude Encoding (4 Qubits)

**Normalization factor:** α = 1/√4 = 0.5

**16-element amplitude vector:**
```
[0, α·P1[0], 0, α·P1[1],           ← P1 with label=1 (indices 1,3)
 α·P2[0], 0, α·P2[1], 0,           ← P2 with label=0 (indices 4,6)
 0, α·P3[0], 0, α·P3[1],           ← P3 copy 1, label=1 (indices 9,11)
 α·P3[0], 0, α·P3[1], 0]           ← P3 copy 2, label=0 (indices 12,14)
```

**Key:** Test point P3 appears **twice** (with both labels) for interference!

#### STEP C: Hadamard Transformation

**Apply Hadamard on q0 ONLY:**
```
Circuit: q0─Initialize─┤H├─M─
         q1─Initialize──────
         q2─Initialize──────
         q3─Initialize─────M─
```

**Constraints:**
- ✅ Exactly 1 Hadamard gate (on q0)
- ✅ No other quantum gates
- ✅ State initialized with 16-element amplitude vector

**Effect:** Creates interference between ancilla blocks (q0=0 and q0=1)

#### STEP D: Post-Selection on q0 = 0

**Measurement logic:**
```
if measurement(q0) == 0:
    keep_shot()
    record q3 value
else:
    discard_shot()
    rerun circuit
```

**Expected:** ~50% of shots kept (Hadamard creates equal superposition)

**Purpose:** Post-selection on q0=0 keeps the constructive interference (sum) terms, which encode squared distances.

#### STEP E: Classification from q3

Among post-selected shots (q0=0), measure label qubit q3:

```
p(survive) = count(q3=1 | q0=0) / total_post_selected_shots
p(die)     = count(q3=0 | q0=0) / total_post_selected_shots
```

**Book's expected output:**
- p(survive) ≈ 0.552
- p(die) ≈ 0.448

**Prediction:** SURVIVED (p(survive) > p(die))

### Key Insights from the Book

1. **Amplitude Encoding Bottleneck:** State preparation may cost O(N) time or worse. The book emphasizes this is a practical limitation for quantum advantage.

2. **Clifford Circuit (Classically Simulable):** Uses only Hadamard gates (Clifford group), so efficiently simulable on classical computers. This is a pedagogical example, not a speedup claim.

3. **Post-Selection Overhead:** Only ~50% of shots are kept (q0=0), requiring 2× more circuit executions.

4. **Squared-Distance Equivalence:** Measured probabilities algebraically equal classical squared-distance classifier with c=4:
   ```
   p(y=i|x) = exp(-c·||x-m_i||²) / χ
   ```

5. **Test Point Duplication:** P3 appears twice in amplitude vector (both labels) - this is the key quantum trick enabling interference-based distance computation!

## Implementation Structure

### Notebook 00: Data Preprocessing and Amplitude Encoding
- **STEP 0**: Min-max scaling to [0,1] with book's exact ranges
- **STEP A**: L2 normalization to unit vectors
- **STEP B**: Construct 16-element amplitude vector for 4 qubits
- Verify all values match book's expected output
- Visualize normalized feature space
- Save preprocessed data

### Notebook 01: 4-Qubit Circuit Build and Hadamard Interference
- **STEP C**: Build 4-qubit circuit (q0: ancilla, q1-q2: features, q3: label)
- Initialize with amplitude vector using Qiskit
- Apply 1 Hadamard gate on q0 ONLY
- Analyze state before and after Hadamard
- Visualize interference effects
- Save circuit for execution

### Notebook 02: Post-Selection, Measurement, and Classification
- **STEP D**: Execute circuit and apply post-selection (keep q0=0)
- **STEP E**: Measure q3 for classification probabilities
- Compare with book's expected output (p_survive≈0.552)
- Visualize classification results
- Document key insights from the book

## Dependencies

- **Qiskit & Qiskit-Aer**: 4-qubit circuit construction and simulation
- **NumPy**: Numerical operations and preprocessing
- **Pandas**: Data manipulation
- **Matplotlib**: Visualization
- **Pickle**: Save/load preprocessed data

## Files

- **Notebooks/00_.data_preprocessing_and_encoding.ipynb**: STEPS 0, A, B
- **Notebooks/01_circuit_build_and_interference.ipynb**: STEP C  
- **Notebooks/02_measurement_and_classification.ipynb**: STEPS D, E
- **exact_4qubit_classifier.py**: Standalone Python implementation
- **EXACT_IMPLEMENTATION_GUIDE.md**: Complete documentation
- **2QUBIT_VS_4QUBIT.md**: Explains why 4 qubits (not 2!)

## References

1. **Schuld, M., & Petruccione, F. (2018)**. *Supervised Learning with Quantum Computers*. Springer. **Chapter 1.2** (pages 12-18) - The exact toy example.
2. **Key Equation (1.2)**: Squared-distance classifier probability formula with c=4.
3. **Figure 1.2**: Circuit diagram showing 4-qubit structure with Hadamard on ancilla.
