# Project Architecture: Quantum Titanic Survival Classifier

## 📋 Overview

This project implements the **exact 4-qubit quantum squared-distance classifier** from Schuld & Petruccione's "Supervised Learning with Quantum Computers" (Chapter 1.2). The architecture follows a modular, research-oriented design with clear separation between exploratory notebooks, production code, and documentation.

---

## 🏗️ High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        PROJECT ROOT                              │
│  Quantum Squared-Distance Classifier (4-Qubit Implementation)   │
└─────────────────────────────────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│  NOTEBOOKS   │   │  SCRIPTS     │   │  DATA/MODELS │
│  (Research)  │   │  (Prod Code) │   │  (Artifacts) │
└──────────────┘   └──────────────┘   └──────────────┘
        │                   │                   │
        └───────────────────┴───────────────────┘
                            │
                    ┌───────┴───────┐
                    │  DOCUMENTATION │
                    └────────────────┘
```

---

## 📁 Directory Structure

```
Titanic_survival_QML_Project/
│
├── Notebooks/                          # Jupyter notebooks (step-by-step research)
│   ├── 00_data_preprocessing_and_encoding.ipynb    # STEPS 0, A, B
│   ├── 01_circuit_build_and_interference.ipynb     # STEP C
│   ├── 02_measurement_and_classification.ipynb     # STEPS D, E
│   └── 03_exact_book_implementation_4qubit.ipynb   # Complete standalone
│
├── Data/                               # Data storage
│   ├── Raw/                            # Original toy dataset (3 passengers)
│   └── Processed/                      # Preprocessed data (.pkl files)
│       ├── toy_encoded_data_4qubit.pkl
│       └── circuit_4qubit.pkl
│
├── Models/                             # Trained models / circuit artifacts
│   └── (quantum circuits, classifiers)
│
├── Figures/                            # Generated plots and visualizations
│   └── (circuit diagrams, probability distributions)
│
├── src/                                # Python package (currently empty)
│   └── (future modular code: preprocessing, circuits, metrics)
│
├── exact_4qubit_classifier.py         # Standalone production script
├── quantum_classifier.py              # PennyLane-based classifier (legacy)
├── main.py                             # Entry point (placeholder)
│
├── ARCHITECTURE.md                     # This file
├── project_overview.md                 # Theory and algorithm explanation
├── EXACT_IMPLEMENTATION_GUIDE.md       # 4-qubit implementation guide
├── 2QUBIT_VS_4QUBIT.md                 # Why 4 qubits, not 2
├── README.md                           # Project description
├── README_IMPLEMENTATION.md            # Implementation notes
│
├── pyproject.toml                      # UV package manager configuration
├── uv.lock                             # Locked dependencies
├── .python-version                     # Python 3.12
└── .venv/                              # Virtual environment

```

---

## 🧩 Component Architecture

### 1. **Notebook Layer** (Exploratory Research)

**Purpose:** Step-by-step exploration and validation of quantum algorithm

```
┌────────────────────────────────────────────────────────────────┐
│  NOTEBOOK 00: Data Preprocessing & Amplitude Encoding          │
│  ─────────────────────────────────────────────────────────────│
│  • STEP 0: Min-max scaling [0,1]                               │
│  • STEP A: L2 normalization                                    │
│  • STEP B: 16-element amplitude vector construction            │
│  • Verification: Match book's expected values                  │
│  • Output: toy_encoded_data_4qubit.pkl                         │
└────────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────────────┐
│  NOTEBOOK 01: Circuit Build & Hadamard Interference            │
│  ─────────────────────────────────────────────────────────────│
│  • STEP C: Build 4-qubit circuit (q0-q3)                       │
│  • Initialize with amplitude vector (Qiskit)                   │
│  • Apply 1 Hadamard on q0 (ancilla)                            │
│  • State analysis before/after Hadamard                        │
│  • Output: circuit_4qubit.pkl                                  │
└────────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────────────┐
│  NOTEBOOK 02: Measurement & Classification                     │
│  ─────────────────────────────────────────────────────────────│
│  • STEP D: Execute circuit with post-selection (q0=0)          │
│  • STEP E: Extract classification from q3                      │
│  • Visualization: measured vs expected probabilities           │
│  • Output: Final prediction + insights                         │
└────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────┐
│  NOTEBOOK 03: Complete Standalone Implementation               │
│  ─────────────────────────────────────────────────────────────│
│  • All STEPS 0-E in one notebook                               │
│  • Self-contained, reproducible                                │
│  • Used for validation and demo                                │
└────────────────────────────────────────────────────────────────┘
```

**Technologies:**
- Jupyter Notebook
- Qiskit 2.2.3+ (quantum circuits)
- Qiskit-Aer (simulation)
- NumPy, Pandas, Matplotlib, Seaborn

---

### 2. **Script Layer** (Production Code)

**Purpose:** Reusable, executable scripts for deployment

```
┌────────────────────────────────────────────────────────────────┐
│  exact_4qubit_classifier.py                                    │
│  ─────────────────────────────────────────────────────────────│
│  Main Functions:                                               │
│  • preprocess_data()          ← STEP 0 & A                     │
│  • construct_amplitude_vector() ← STEP B                       │
│  • build_quantum_circuit()    ← STEP C                         │
│  • execute_with_postselection() ← STEP D                       │
│  • classify_from_q3()         ← STEP E                         │
│  • main()                     ← Orchestrator                   │
│                                                                 │
│  Input:  Raw toy dataset (3 passengers)                        │
│  Output: Classification prediction + probabilities             │
│  Status: ✅ Tested and working                                 │
└────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────┐
│  quantum_classifier.py (Legacy PennyLane Version)              │
│  ─────────────────────────────────────────────────────────────│
│  Class: QuantumSquaredDistanceClassifier                       │
│  • Uses PennyLane framework                                    │
│  • 2-qubit implementation (older approach)                     │
│  Status: 🔒 Kept for reference, superseded by Qiskit 4-qubit   │
└────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────┐
│  main.py (Entry Point - Placeholder)                           │
│  ─────────────────────────────────────────────────────────────│
│  • Currently prints "Hello from titanic-survival-qml-project!" │
│  • Future: CLI interface to run classifier                     │
└────────────────────────────────────────────────────────────────┘
```

---

### 3. **Data Flow Architecture**

```
┌──────────────┐
│  Raw Data    │   3 passengers: [price, cabin, survival]
│  (Hardcoded) │   P1: [8500, 910, 1]
└──────┬───────┘   P2: [1200, 2105, 0]
       │           P3: [7800, 1121, ?]
       ▼
┌──────────────────────────────────────────────────────────────┐
│  STEP 0: Min-Max Scaling                                     │
│  price_scaled = price / 10000                                │
│  cabin_scaled = cabin / 2500                                 │
└──────────────────┬───────────────────────────────────────────┘
                   ▼
┌──────────────────────────────────────────────────────────────┐
│  STEP A: L2 Normalization                                    │
│  x_normalized = x / ||x||₂                                   │
│  Expected: P1=[0.921, 0.390], P2=[0.141, 0.990]             │
└──────────────────┬───────────────────────────────────────────┘
                   ▼
┌──────────────────────────────────────────────────────────────┐
│  STEP B: Amplitude Vector (16 elements)                      │
│  α = 1/√4 = 0.5                                              │
│  [0, α·P1[0], 0, α·P1[1],                                    │
│   α·P2[0], 0, α·P2[1], 0,                                    │
│   0, α·P3[0], 0, α·P3[1],                                    │
│   α·P3[0], 0, α·P3[1], 0]                                    │
└──────────────────┬───────────────────────────────────────────┘
                   ▼
┌──────────────────────────────────────────────────────────────┐
│  STEP C: Quantum Circuit (4 qubits)                          │
│  q0: ─Initialize─┤H├─M─  (ancilla for interference)         │
│  q1: ─Initialize─────────  (feature bit 0)                   │
│  q2: ─Initialize─────────  (feature bit 1)                   │
│  q3: ─Initialize────────M─  (label: 0=died, 1=survived)      │
└──────────────────┬───────────────────────────────────────────┘
                   ▼
┌──────────────────────────────────────────────────────────────┐
│  STEP D: Post-Selection (q0 = 0)                             │
│  Run 8192 shots → Keep only q0=0 measurements (~50%)         │
│  Discard q0=1 shots (destructive interference)               │
└──────────────────┬───────────────────────────────────────────┘
                   ▼
┌──────────────────────────────────────────────────────────────┐
│  STEP E: Classification                                       │
│  p(survive) = count(q3=1 | q0=0) / total_postselected        │
│  p(die)     = count(q3=0 | q0=0) / total_postselected        │
│  Prediction: argmax(p)                                        │
└──────────────────┬───────────────────────────────────────────┘
                   ▼
           ┌───────────────┐
           │ Final Result  │  Passenger 3: SURVIVED
           │ Probabilities │  p(survive)≈0.552 (expected)
           └───────────────┘  p(die)≈0.448
```

---

### 4. **Quantum Circuit Architecture (4-Qubit)**

```
Qubit Roles:
┌─────┬──────────────────────────────────────────────────────┐
│ q0  │ ANCILLA - Hadamard interference, post-selection      │
│ q1  │ FEATURE BIT 0 - Encodes x[0] (price dimension)       │
│ q2  │ FEATURE BIT 1 - Encodes x[1] (cabin dimension)       │
│ q3  │ LABEL - Classification outcome (0=died, 1=survived)  │
└─────┴──────────────────────────────────────────────────────┘

Circuit Diagram (Qiskit):
     ┌────────────┐┌───┐┌─┐
q_0: ┤ Initialize ├┤ H ├┤M├─────────
     ├────────────┤└───┘└╥┘
q_1: ┤ Initialize ├──────╫──────────
     ├────────────┤      ║
q_2: ┤ Initialize ├──────╫──────────
     ├────────────┤      ║  ┌─┐
q_3: ┤ Initialize ├──────╫──┤M├─────
     └────────────┘      ║  └╥┘
c: 2/════════════════════╩═══╩══════
                         0   1

Gate Count:
• 1 Initialize gate (sets 16 amplitudes)
• 1 Hadamard gate (on q0)
• 2 Measurement gates (q0, q3)
• 0 CNOT gates (Clifford circuit)
```

**Key Property:** This is a **Clifford circuit** (only Hadamard + measurements), making it efficiently classically simulable. The book uses it as a pedagogical example, not for quantum advantage.

---

### 5. **Algorithm Architecture (Book's 5-Step Process)**

```
┌────────────────────────────────────────────────────────────────┐
│  ALGORITHM: Quantum Squared-Distance Classifier (4-Qubit)      │
├────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Input:  2 training examples {(x₁,y₁), (x₂,y₂)}               │
│          1 test example xₜₑₛₜ                                  │
│  Output: Predicted label ŷ ∈ {0, 1}                           │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │ PREPROCESSING PHASE (Classical)                          │ │
│  ├──────────────────────────────────────────────────────────┤ │
│  │ STEP 0: Min-Max Scaling [0,1]                            │ │
│  │         • price: [0, 10000] → scaled                     │ │
│  │         • cabin: [0, 2500] → scaled                      │ │
│  │                                                           │ │
│  │ STEP A: L2 Normalization                                 │ │
│  │         • x_norm = x / ||x||₂                            │ │
│  │         • Ensures unit vectors                           │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │ QUANTUM ENCODING PHASE                                   │ │
│  ├──────────────────────────────────────────────────────────┤ │
│  │ STEP B: Amplitude Encoding                               │ │
│  │         • Construct 16-element vector                    │ │
│  │         • α = 1/√4 normalization                         │ │
│  │         • Duplicate test point (both labels)             │ │
│  │         • Indices: P1(1,3), P2(4,6), P3(9,11,12,14)      │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │ QUANTUM INTERFERENCE PHASE                               │ │
│  ├──────────────────────────────────────────────────────────┤ │
│  │ STEP C: Circuit Execution                                │ │
│  │         • Initialize 4 qubits with amplitude vector      │ │
│  │         • Apply H on q0 (creates interference)           │ │
│  │         • H|0⟩ = (|0⟩ + |1⟩)/√2 ← keeps sum terms       │ │
│  │         • H|1⟩ = (|0⟩ - |1⟩)/√2 ← discarded             │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │ MEASUREMENT PHASE                                         │ │
│  ├──────────────────────────────────────────────────────────┤ │
│  │ STEP D: Post-Selection                                   │ │
│  │         • Measure q0                                     │ │
│  │         • Keep shots with q0=0 (~50%)                    │ │
│  │         • Discard shots with q0=1                        │ │
│  │                                                           │ │
│  │ STEP E: Classification                                   │ │
│  │         • Among q0=0 shots, count q3 values              │ │
│  │         • p(survive) = #(q3=1) / total_kept              │ │
│  │         • p(die) = #(q3=0) / total_kept                  │ │
│  │         • Predict: argmax(p)                             │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                 │
└────────────────────────────────────────────────────────────────┘

Mathematical Equivalence (Book's Key Result):
  p(y=i|x) ∝ exp(-c·||x - mᵢ||²)   with c=4
  
Where mᵢ are class means (prototypes).
```

---

## 🔧 Technology Stack

### **Quantum Computing Frameworks**
```
Primary:
  • Qiskit 2.2.3+        - Circuit construction
  • Qiskit-Aer 0.17.2    - Simulation backend

Legacy:
  • PennyLane 0.43.1     - Alternative framework (quantum_classifier.py)
```

### **Scientific Computing**
```
  • NumPy 2.3.5          - Numerical operations
  • SciPy 1.16.3         - Scientific functions
  • Pandas 2.3.3         - Data manipulation
```

### **Visualization**
```
  • Matplotlib 3.10.7    - Plotting
  • Seaborn 0.13.2       - Statistical visualization
```

### **ML & Utilities**
```
  • Scikit-learn 1.7.2   - Preprocessing utilities
  • MLflow 3.6.0         - Experiment tracking (future)
```

### **Development Tools**
```
  • UV Package Manager   - Fast Python package management
  • Jupyter Notebook     - Interactive development
  • Python 3.12          - Language version
```

---

## 🔄 Workflow & Execution Flow

### **Research Workflow (Notebooks)**
```
1. Start with Notebook 00 → Run all cells → Generates toy_encoded_data_4qubit.pkl
                           ↓
2. Open Notebook 01 → Load .pkl → Run circuit → Save circuit_4qubit.pkl
                           ↓
3. Open Notebook 02 → Load circuit → Execute → Classification results
```

### **Production Workflow (Script)**
```
$ uv run python exact_4qubit_classifier.py

Flow:
  main() 
    → preprocess_data() 
    → construct_amplitude_vector() 
    → build_quantum_circuit() 
    → execute_with_postselection() 
    → classify_from_q3()
    → print results
```

### **Package Management**
```
# Install dependencies
$ uv sync

# Add new package
$ uv add <package-name>

# Run script
$ uv run python <script.py>
```

---

## 📊 Data Architecture

### **Input Data Schema**
```python
# Raw Data (3 passengers)
raw_data = [
    [ticket_price: float, cabin_number: int, survival: int],  # P1
    [ticket_price: float, cabin_number: int, survival: int],  # P2
    [ticket_price: float, cabin_number: int, survival: int],  # P3 (test)
]

# Book's exact values:
P1 = [8500, 910, 1]   # Survived
P2 = [1200, 2105, 0]  # Died
P3 = [7800, 1121, ?]  # Unknown (to predict)
```

### **Intermediate Data Structures**
```python
# After STEP 0 & A (preprocessed)
processed_data = [
    (np.array([x0, x1]), label),  # Normalized 2D vectors
    ...
]

# After STEP B (amplitude vector)
amplitude_vector = np.array([...], dtype=complex)  # 16 elements

# Circuit state (STEP C)
qc = QuantumCircuit(4, 2)  # 4 qubits, 2 classical bits
```

### **Output Data Schema**
```python
# Classification result
result = {
    'p_survive': float,     # Probability of survival
    'p_die': float,         # Probability of death
    'prediction': str,      # "SURVIVED" or "DIED"
    'postselection_rate': float,  # % of shots kept (q0=0)
    'total_shots': int,     # Number of circuit executions
}
```

### **Saved Artifacts**
```
Data/Processed/
  ├── toy_encoded_data_4qubit.pkl
  │   └── Contains: {P1, P2, P3, labels, amplitude_vector}
  │
  └── circuit_4qubit.pkl
      └── Contains: QuantumCircuit object (pre-configured)
```

---

## 🧪 Testing & Validation Strategy

### **Verification Checkpoints**

1. **STEP 0 Validation** (Min-Max Scaling)
   ```python
   assert 0 <= price_scaled <= 1
   assert 0 <= cabin_scaled <= 1
   ```

2. **STEP A Validation** (L2 Normalization)
   ```python
   assert np.isclose(np.linalg.norm(P1), 1.0)
   assert np.isclose(P1[0], 0.921, atol=1e-3)
   assert np.isclose(P1[1], 0.390, atol=1e-3)
   ```

3. **STEP B Validation** (Amplitude Vector)
   ```python
   assert len(amplitude_vector) == 16
   assert np.isclose(np.linalg.norm(amplitude_vector), 1.0)
   assert amplitude_vector[1] == 0.5 * P1[0]
   ```

4. **STEP C Validation** (Circuit Structure)
   ```python
   assert qc.num_qubits == 4
   assert qc.count_ops()['h'] == 1  # Exactly 1 Hadamard
   ```

5. **STEP D Validation** (Post-Selection)
   ```python
   assert 0.40 <= postselection_rate <= 0.60  # ~50%
   ```

6. **STEP E Validation** (Classification)
   ```python
   assert np.isclose(p_survive, 0.552, atol=0.1)  # Expected from book
   ```

### **Expected Results (from Book)**
```
Preprocessing:
  P1_normalized = [0.921, 0.390]
  P2_normalized = [0.141, 0.990]
  P3_normalized = [0.866, 0.500]

Classification:
  p(survive | P3) ≈ 0.552
  p(die | P3)     ≈ 0.448
  Prediction: SURVIVED
```

---

## 📚 Documentation Architecture

```
Documentation Hierarchy:

README.md                          ← Project intro (currently empty)
  └─ Quick start, installation

ARCHITECTURE.md                    ← This file
  └─ System design, components, flows

project_overview.md                ← Theory & algorithm
  └─ Book reference, mathematical background

EXACT_IMPLEMENTATION_GUIDE.md      ← Implementation details
  └─ Step-by-step guide, code snippets

2QUBIT_VS_4QUBIT.md                ← Design decision
  └─ Why 4 qubits needed (not 2)

README_IMPLEMENTATION.md           ← Implementation notes
  └─ Additional context

Notebooks/*.ipynb                  ← Inline documentation
  └─ Markdown cells explain each step
```

---

## 🚀 Future Enhancements

### **Planned Improvements**

1. **Modularize Code into `src/` Package**
   ```
   src/
     ├── __init__.py
     ├── preprocessing.py    # STEP 0, A
     ├── encoding.py         # STEP B
     ├── circuits.py         # STEP C
     ├── measurement.py      # STEP D, E
     └── utils.py            # Helper functions
   ```

2. **CLI Interface in `main.py`**
   ```bash
   $ python main.py --data custom_data.csv --shots 10000 --output results.json
   ```

3. **MLflow Experiment Tracking**
   - Log preprocessing parameters
   - Track circuit execution metrics
   - Compare different quantum backends

4. **Extended Dataset**
   - Scale beyond 3 passengers
   - Real Titanic dataset integration
   - Hybrid quantum-classical approach

5. **Unit Tests**
   ```
   tests/
     ├── test_preprocessing.py
     ├── test_encoding.py
     ├── test_circuits.py
     └── test_integration.py
   ```

6. **CI/CD Pipeline**
   - Automated testing with GitHub Actions
   - Notebook execution validation
   - Documentation generation

---

## 🎯 Design Principles

1. **Fidelity to Source Material**
   - Exact implementation of book's toy example
   - All steps (0-E) match Chapter 1.2
   - Expected outputs validated against book

2. **Reproducibility**
   - Fixed random seeds
   - Locked dependencies (uv.lock)
   - Deterministic preprocessing

3. **Modularity**
   - Notebooks for exploration
   - Scripts for production
   - Clear separation of concerns

4. **Documentation-First**
   - Every step explained
   - Theory before implementation
   - Inline comments + external docs

5. **Research-Oriented**
   - Jupyter notebooks as primary development environment
   - Visualizations for every stage
   - Pedagogical clarity over performance

---

## 🔍 Key Architectural Decisions

### **Decision 1: Why 4 Qubits (Not 2)?**
**Rationale:** Need 2^4=16 amplitude slots to encode:
- P1 (label=1): 2 amplitudes
- P2 (label=0): 2 amplitudes
- P3 (both labels): 4 amplitudes (duplicated for interference)
- Total: 8 non-zero entries → requires 16 slots

### **Decision 2: Why Qiskit (Not PennyLane)?**
**Rationale:** Qiskit's `initialize()` method allows direct amplitude encoding, matching book's specification exactly. PennyLane requires gate decomposition.

### **Decision 3: Why Post-Selection (Not Measurement)?**
**Rationale:** Book explicitly requires keeping only q0=0 measurements to isolate constructive interference terms. This is the quantum "trick" that encodes squared distances.

### **Decision 4: Why Separate Notebooks (00, 01, 02)?**
**Rationale:** Educational clarity - each notebook teaches one concept (preprocessing, circuit, measurement). Notebook 03 combines all for validation.

### **Decision 5: Why Hardcoded Data (Not CSV)?**
**Rationale:** Book's toy example uses 3 specific passengers. Hardcoding ensures exact reproducibility and matches pedagogical intent.

---

## 📖 References

1. **Schuld, M., & Petruccione, F. (2018)**  
   *Supervised Learning with Quantum Computers*. Springer.  
   **Chapter 1.2** (pages 12-18) - Quantum Squared-Distance Classifier

2. **Qiskit Documentation**  
   https://docs.quantum.ibm.com/

3. **UV Package Manager**  
   https://github.com/astral-sh/uv

---

## 📞 Contact & Maintenance

**Project Type:** Research/Educational  
**Status:** Active Development  
**Last Updated:** November 27, 2025  
**Python Version:** 3.12  
**Key Dependency:** Qiskit 2.2.3+

---

*This architecture document is a living document and will be updated as the project evolves.*
