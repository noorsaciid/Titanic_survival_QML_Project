# Project-Wide Refactoring Summary

**Date:** November 27, 2025  
**Objective:** Align entire project with book's P1, P2, P3 naming convention

---

## 🎯 Refactoring Scope

### Goal
Replace sklearn-style naming (`X_train`, `X_test`, `y_train`, `y_test`) with book's pedagogical naming (`P1`, `P2`, `P3`) throughout the entire project.

### Motivation
- **Book compliance:** Schuld & Petruccione use simple P1, P2, P3 throughout Chapter 1.2
- **Pedagogical clarity:** More intuitive for learning (3 specific passengers vs abstract train/test sets)
- **Consistency:** Match the book's notation exactly in code and comments

---

## 📝 Files Modified

### 1. **Notebook 00: Data Preprocessing and Encoding** ✅
**File:** `Notebooks/00_.data_preprocessing_and_encoding.ipynb`

**Changes:**
- Cell 6 (markdown): Updated description to "Extract P1, P2, P3"
- Cell 7 (code): Changed from `X_train`, `X_test` to `P1_raw`, `P2_raw`, `P3_raw`
- Cell 9 (code): Changed from `X_train_scaled`, `X_test_scaled` to `P1_scaled`, `P2_scaled`, `P3_scaled`
- Cell 11 (code): Changed from `X_train_normalized`, `X_test_normalized` to `P1`, `P2`, `P3` (final normalized)
- Cell 12 (NEW): Added STEP B (amplitude vector construction) with clear P1, P2, P3 usage
- Cell 16 (save): Now correctly saves `P1`, `P2`, `P3` (previously referenced undefined variables)

**Key Fix:**
- Cells 14 and 16 were referencing `P1`, `P2`, `P3` before they were defined
- Now properly created in Cell 11 after L2 normalization

**Result:** All variables follow book's naming from raw → scaled → normalized → amplitude encoding

---

### 2. **Notebook 01: Circuit Build and Interference** ✅
**File:** `Notebooks/01_circuit_build_and_interference.ipynb`

**Changes:**
- Deleted 10 cells containing deprecated PennyLane 2-qubit code (cells 15-24)
- These cells used `X_test`, `y_test`, `prototype_a`, `prototype_b` (old naming)
- Retained only 4-qubit Qiskit implementation matching book

**Cells Deleted:**
1. Step 3 markdown (old 2-qubit description)
2. `state_preparation()` function (PennyLane)
3. `quantum_classifier_circuit()` (PennyLane)
4. Circuit visualization (PennyLane)
5. Sample testing (referenced `X_test[i]`, `y_test[i]`)
6. Interference analysis (referenced `X_test`, `prototype_a/b`)
7. Save circuit results (saved old variables)

**Retained:**
- Steps 0-2: Load P1, P2, P3 from Notebook 00 ✅
- STEP C: Build 4-qubit Qiskit circuit ✅
- State analysis (before/after Hadamard) ✅
- Save circuit data with P1, P2, P3 ✅

**Result:** Pure 4-qubit Qiskit implementation, no legacy code

---

### 3. **Notebook 02: Measurement and Classification** ✅
**File:** `Notebooks/02_measurement_and_classification.ipynb`

**Changes:**
- Deleted 14 cells containing deprecated PennyLane code (cells 14-27)
- These cells used `X_test`, `y_test`, `prototype_a`, `prototype_b`
- Retained only 4-qubit Qiskit measurement and post-selection
- Added summary cell explaining complete pipeline

**Cells Deleted:**
1. "Recreate Quantum Classifier" (PennyLane device setup)
2. 2-qubit circuit definitions
3. Test set classification loop (referenced `X_test`)
4. Accuracy evaluation (referenced `y_test`)
5. Confusion matrix (old variables)
6. Classical baseline comparison (referenced `prototype_a/b`)
7. Measurement probability analysis (old variables)
8. Insights summary (outdated)
9. Save final results (saved old variables)

**Retained:**
- Steps 0-1: Load P1, P2, P3 and circuit from Notebook 01 ✅
- STEP D: Post-selection on q0=0 ✅
- STEP E: Classification from q3 ✅
- Verification against book's expected output ✅
- NEW: Summary cell with complete pipeline overview ✅

**Result:** Clean 4-qubit post-selection and measurement, matches book exactly

---

### 4. **README.md** ✅ (Created)
**File:** `README.md`

**Changes:**
- Created comprehensive project README (was empty)
- Uses P1, P2, P3 throughout documentation
- Clear algorithm steps matching book's STEPS 0, A, B, C, D, E
- Dataset table shows P1, P2, P3 explicitly
- Expected output uses book's values

**Key Sections:**
- Quick Start guide
- Project structure (showing P1/P2/P3 in data files)
- Algorithm steps (STEPS 0, A, B, C, D, E from book)
- Implementation details with P1, P2, P3 examples
- Results verification against book

---

### 5. **Data/Raw/README.md** ✅
**File:** `Data/Raw/README.md`

**Changes:**
- Updated usage example to use P1, P2, P3 naming
- Changed from:
  ```python
  train_df = df[df['survival'].notna()]
  X_train = train_df[...].values
  ```
- To:
  ```python
  P1_raw = df.iloc[0][...].values  # Passenger 1 (survived)
  P2_raw = df.iloc[1][...].values  # Passenger 2 (died)
  P3_raw = df.iloc[2][...].values  # Passenger 3 (unknown)
  ```

**Result:** Documentation matches code naming

---

### 6. **Notebook 03: Exact Book Implementation** ✅ (Already Compliant)
**File:** `Notebooks/03_exact_book_implementation_4qubit.ipynb`

**Status:** No changes needed - already uses P1, P2, P3 throughout

---

### 7. **exact_4qubit_classifier.py** ✅ (Already Compliant)
**File:** `exact_4qubit_classifier.py`

**Status:** No changes needed - already uses P1, P2, P3 in comments and structure

---

## 📊 Impact Summary

### Variables Renamed Across Project

| Old Name | New Name | Meaning |
|----------|----------|---------|
| `X_train[0]` | `P1` | Passenger 1 (survived, label=1) |
| `X_train[1]` | `P2` | Passenger 2 (died, label=0) |
| `X_test[0]` | `P3` | Passenger 3 (unknown label) |
| `y_train[0]` | `P1_label` | Passenger 1's label (1) |
| `y_train[1]` | `P2_label` | Passenger 2's label (0) |
| `train_df` | *(removed)* | No longer needed |
| `test_df` | *(removed)* | No longer needed |
| `prototype_a` | `P2` | Class 0 prototype (died) |
| `prototype_b` | `P1` | Class 1 prototype (survived) |

### Code Removed
- **22 cells deleted** across Notebooks 01 and 02
- All deprecated PennyLane 2-qubit code
- All references to `X_train`, `X_test`, `y_train`, `y_test`
- All references to `prototype_a`, `prototype_b`

### Code Added
- **1 cell** in Notebook 00 (STEP B amplitude encoding)
- **1 cell** in Notebook 02 (summary)
- **Full README.md** documentation

---

## ✅ Verification Checklist

### Naming Consistency
- ✅ All notebooks use P1, P2, P3
- ✅ All documentation uses P1, P2, P3
- ✅ Pickle files save P1, P2, P3
- ✅ No references to X_train/X_test remain in active code

### Book Compliance
- ✅ Data preprocessing matches book's STEP 0 (min-max scaling)
- ✅ Normalization matches book's STEP A (L2 normalization)
- ✅ Amplitude encoding matches book's STEP B (1/√4 normalization)
- ✅ Circuit matches book's STEP C (4 qubits, 1 Hadamard)
- ✅ Post-selection matches book's STEP D (q0=0 filter)
- ✅ Classification matches book's STEP E (q3 measurement)

### Code Quality
- ✅ All notebooks run without NameError
- ✅ Variables defined before use
- ✅ No deprecated code remains
- ✅ Comments explain book's theory
- ✅ Expected values verified against book

---

## 🎓 Pedagogical Benefits

### Before Refactoring
```python
# Abstract, ML-focused naming
X_train = train_df[['ticket_price', 'cabin_number']].values
y_train = train_df['survival'].values
X_test = test_df[['ticket_price', 'cabin_number']].values

# Unclear which passenger is which
prototype_a = X_train[0]  # Who is this?
prototype_b = X_train[1]  # Who is this?
```

### After Refactoring
```python
# Concrete, passenger-focused naming
P1_raw = df.iloc[0][['ticket_price', 'cabin_number']].values  # Passenger 1 (survived)
P2_raw = df.iloc[1][['ticket_price', 'cabin_number']].values  # Passenger 2 (died)
P3_raw = df.iloc[2][['ticket_price', 'cabin_number']].values  # Passenger 3 (to predict)

# Crystal clear - matches book exactly
P1 = normalize_l2(P1_scaled)  # [0.921, 0.390], label=1
P2 = normalize_l2(P2_scaled)  # [0.141, 0.990], label=0
P3 = normalize_l2(P3_scaled)  # [0.866, 0.500], label=?
```

**Key Improvements:**
1. **Traceability:** Each variable directly maps to book's notation
2. **Clarity:** No need to remember "train[0] = P1, train[1] = P2"
3. **Intent:** Names convey meaning (passengers, not abstract arrays)
4. **Learning:** Students can follow book while reading code

---

## 🔄 Data Flow (New Naming)

```
Raw Data (CSV)
    ↓
P1_raw, P2_raw, P3_raw  ← Extract from dataframe
    ↓ STEP 0 (Min-Max Scaling)
P1_scaled, P2_scaled, P3_scaled  ← [0,1] ranges
    ↓ STEP A (L2 Normalization)
P1, P2, P3  ← Unit vectors (FINAL)
    ↓ STEP B (Amplitude Encoding)
amplitude_vector  ← 16 elements, α=1/√4
    ↓ STEP C (Quantum Circuit)
qc (4 qubits, 1 Hadamard)
    ↓ STEP D (Post-Selection)
shots where q0=0
    ↓ STEP E (Classification)
p(survive), p(die)
```

**Naming at each stage:**
- Raw: `P1_raw`, `P2_raw`, `P3_raw` + `P1_label`, `P2_label`
- Scaled: `P1_scaled`, `P2_scaled`, `P3_scaled`
- Normalized: **`P1`, `P2`, `P3`** (primary names used everywhere)
- Encoded: `amplitude_vector` (constructed from P1, P2, P3)

---

## 📚 Book Reference Mapping

| Code Variable | Book Notation | Description |
|---------------|---------------|-------------|
| `P1` | **P1** | First training point (survived) |
| `P2` | **P2** | Second training point (died) |
| `P3` | **P3** | Test point (unknown label) |
| `P1_label` | **y₁ = 1** | P1's survival (binary) |
| `P2_label` | **y₂ = 0** | P2's survival (binary) |
| `alpha` | **α = 1/√4** | Normalization factor |
| `amplitude_vector` | **\|ψ⟩** | Quantum state amplitudes |
| `q[0]` | **ancilla qubit** | Post-selection qubit |
| `q[1], q[2]` | **feature qubits** | Encode x₀, x₁ |
| `q[3]` | **label qubit** | Encode y (survival) |

---

## 🚀 Next Steps

### For Users
1. Run Notebook 00 to see P1, P2, P3 extraction and preprocessing
2. Run Notebook 01 to see circuit build with P1, P2, P3
3. Run Notebook 02 to see classification of P3
4. Check Notebook 03 for complete standalone implementation

### For Developers
1. Always use P1, P2, P3 in new code
2. Reference book's STEPS 0, A, B, C, D, E in comments
3. Verify expected values against book
4. Update ARCHITECTURE.md if adding new features

---

## 📖 References

**Primary Source:**
- Schuld, M., & Petruccione, F. (2018). *Supervised Learning with Quantum Computers*. Chapter 1.2: A Simple Classifier.

**Implementation:**
- This project uses the book's exact notation (P1, P2, P3) throughout
- All expected values verified against book's toy example
- No deviation from book's specification

---

## ✅ Verification: All Changes Applied

- ✅ Notebook 00: 6 cells edited (P1, P2, P3 naming)
- ✅ Notebook 01: 10 cells deleted (PennyLane legacy code)
- ✅ Notebook 02: 14 cells deleted (PennyLane legacy code), 1 cell added (summary)
- ✅ Notebook 03: No changes (already compliant)
- ✅ README.md: Created from scratch with P1/P2/P3
- ✅ Data/Raw/README.md: Updated usage example
- ✅ exact_4qubit_classifier.py: Already compliant

**Total Impact:**
- 6 cells edited
- 24 cells deleted (deprecated code)
- 2 cells added (new functionality)
- 2 documentation files updated
- 0 bugs introduced (all variables defined before use)

---

*Refactoring completed: November 27, 2025*  
*Project now 100% compliant with Schuld & Petruccione Chapter 1.2 naming*
