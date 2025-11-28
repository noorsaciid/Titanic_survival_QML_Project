# 2-Qubit vs 4-Qubit: Understanding the Difference

## Why the Confusion?

The original implementation used **2 qubits**, but Schuld & Petruccione's book specifies **4 qubits**. Here's why:

---

## 🔴 2-Qubit Implementation (Simplified Version)

### Structure
- **q0**: Class qubit (superposition of |0⟩ + |1⟩)
- **q1**: Compressed data encoding (both features squeezed into rotation angles)

### Amplitude Vector (4 elements)
```
|ψ⟩ = [α₀₀, α₀₁, α₁₀, α₁₁]
```

### Limitations
1. **Compressed encoding**: Both 2D features mapped to a single qubit via rotation angles
2. **No explicit label qubit**: Label encoded implicitly in superposition
3. **Oversimplified**: Doesn't match book's actual circuit structure

### Circuit
```
q0: ─H─[ψ_prep]─H─M
q1: ───[ψ_prep]───M
```

---

## ✅ 4-Qubit Implementation (Book's Exact Specification)

### Structure
- **q0**: Ancilla qubit (for Hadamard interference)
- **q1**: Feature bit 0 (ticket price amplitude)
- **q2**: Feature bit 1 (cabin number amplitude)
- **q3**: Label qubit (survival outcome)

### Amplitude Vector (16 elements)
```
|ψ⟩ = [α₀₀₀₀, α₀₀₀₁, α₀₀₁₀, ..., α₁₁₁₁]
      ↑ q0   ↑ q1   ↑ q2   ↑ q3
```

### Key Features
1. **Explicit amplitude encoding**: Each feature gets its own qubit(s)
2. **Dedicated label qubit**: Clear separation of data and labels
3. **Test point duplication**: P3 appears twice (with label=0 and label=1)
4. **Matches book exactly**: All specifications align with Chapter 1.2

### Circuit
```
q0: ─Initialize─H─M─
q1: ─Initialize─────
q2: ─Initialize─────
q3: ─Initialize───M─
```

---

## 📊 Comparison Table

| Feature | 2-Qubit (Simplified) | 4-Qubit (Book Exact) |
|---------|---------------------|----------------------|
| **Amplitude slots** | 4 (2²) | 16 (2⁴) |
| **Feature encoding** | Compressed (rotation) | Explicit (amplitude) |
| **Label qubit** | No (implicit) | Yes (q3) |
| **Ancilla qubit** | q0 (dual purpose) | q0 (dedicated) |
| **Test point** | Once | Twice (both labels) |
| **Normalization** | 1/√2 | 1/√4 |
| **Book fidelity** | ❌ Approximate | ✅ Exact |
| **Complexity** | Lower | Higher |
| **Pedagogical value** | Introduction | Full algorithm |

---

## 🎯 Why 4 Qubits for 2D Data?

### Logical Breakdown

**For 2D data [x₀, x₁], we need to encode:**

1. **Training data**: P1=[x₀, x₁] with label=1, P2=[x₀, x₁] with label=0
2. **Test data**: P3=[x₀, x₁] with label=? (unknown)

**Amplitude encoding requirements:**

- P1 needs 2 slots (x₀, x₁) + label=1
- P2 needs 2 slots (x₀, x₁) + label=0
- P3 needs 4 slots (x₀, x₁ twice: once with label=0, once with label=1)

**Total: 8 data slots + labels → requires 4 qubits (2⁴ = 16 slots)**

### Why Duplicate P3?

The quantum interference (Hadamard on q0) computes:
```
H|0⟩|P3,label=0⟩ = (|0⟩ + |1⟩)|P3,label=0⟩
H|1⟩|P3,label=1⟩ = (|0⟩ - |1⟩)|P3,label=1⟩
```

Post-selecting on |0⟩ creates the sum: |P3,label=0⟩ + |P3,label=1⟩

This is the **key quantum trick** that enables computing similarities to both training prototypes simultaneously!

---

## 🧮 Mathematical Proof: Why 4 Qubits?

### Amplitude Vector Structure

**Goal:** Encode 3 passengers × 2 features × 2 label options

**Required amplitude slots:**
```
P1 with label=1: 2 amplitudes (x₀, x₁)
P2 with label=0: 2 amplitudes (x₀, x₁)
P3 with label=0: 2 amplitudes (x₀, x₁)  ← First copy
P3 with label=1: 2 amplitudes (x₀, x₁)  ← Second copy (for interference)
```

**Total: 8 non-zero amplitudes**

**Minimum qubits needed:**
- 3 qubits → 2³ = 8 slots ❌ (not enough for label separation)
- 4 qubits → 2⁴ = 16 slots ✅ (with room for label qubit)

### Qubit Assignment Logic

```
q0 (ancilla): Controls which "block" of training data
  |0⟩ → Training block (P1, P2)
  |1⟩ → Test block (P3, P3)

q1-q2 (features): Encode 2D data via amplitude
  |00⟩ → component 0 of feature 0
  |01⟩ → component 1 of feature 0
  |10⟩ → component 0 of feature 1
  |11⟩ → component 1 of feature 1

q3 (label): Survival outcome
  |0⟩ → Did not survive
  |1⟩ → Survived
```

---

## 📈 When to Use Each?

### Use 2-Qubit Implementation When:
- ✅ Learning quantum ML concepts
- ✅ Quick prototyping
- ✅ Resource-constrained environments
- ✅ You need a "quantum-inspired" approach

### Use 4-Qubit Implementation When:
- ✅ Reproducing book's exact results
- ✅ Academic paper/thesis work
- ✅ Teaching Schuld & Petruccione Chapter 1.2
- ✅ Understanding true amplitude encoding
- ✅ You need the pedagogically correct version

---

## 🔬 Key Takeaway

The **2-qubit version is pedagogically incomplete** because it:
1. Doesn't show explicit amplitude encoding
2. Compresses features artificially
3. Lacks the label qubit structure
4. Can't demonstrate the test-point duplication trick

The **4-qubit version is the book's actual algorithm** because it:
1. ✅ Uses explicit amplitude encoding (book's main teaching point)
2. ✅ Has dedicated label qubit (shows data/label separation)
3. ✅ Duplicates test point (demonstrates quantum interference)
4. ✅ Matches all book equations and circuit diagrams

---

## 💡 Historical Note

Many early quantum ML tutorials simplified the algorithm to 2 qubits because:
- Easier to explain to beginners
- Smaller state vectors to visualize
- Less memory for classical simulation
- But this **sacrifices the key pedagogical insights**!

Schuld & Petruccione deliberately chose 4 qubits to demonstrate:
1. **Amplitude encoding** with real quantum states
2. **Label qubits** as a core ML concept
3. **Quantum interference** for computing similarities
4. **Post-selection** as a quantum measurement strategy

---

## ✅ Implementation Checklist

**Have you verified your implementation is using the EXACT book specification?**

- [ ] 4 qubits (not 2!)
- [ ] 16-element amplitude vector
- [ ] Normalization factor α = 1/√4
- [ ] Test point (P3) appears twice (indices 9,11 and 12,14)
- [ ] Label qubit q3 separated from data qubits q1-q2
- [ ] Ancilla qubit q0 for Hadamard only
- [ ] Post-selection on q0 = 0
- [ ] Classification from q3 measurement
- [ ] Results: p(survive)≈0.552, p(die)≈0.448

**If any box is unchecked, you're not implementing the book's exact algorithm!**

---

## 📚 Further Reading

1. **Schuld & Petruccione (2018), Chapter 1.2**  
   Pages 12-18: The exact toy example with 4-qubit circuit diagram

2. **Why amplitude encoding?**  
   Chapter 1.1: Data encoding strategies for quantum ML

3. **Post-selection overhead**  
   Chapter 1.2.4: Discussion of practical limitations

4. **Quantum advantage?**  
   Chapter 1.3: Why this algorithm is classically simulable

---

**Bottom Line:** Always use the **4-qubit implementation** for faithful reproduction of Schuld & Petruccione Chapter 1.2!
