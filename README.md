# Titanic Survival Prediction with Quantum Machine Learning

**Exact Implementation** of Schuld & Petruccione's *Supervised Learning with Quantum Computers*, Chapter 1.2

A pedagogical quantum machine learning project implementing the quantum squared-distance classifier with 4-qubit amplitude encoding, Hadamard interference, and post-selection.

---

## 📚 Project Overview

This project implements the **exact toy example** from:
- **Book:** Schuld & Petruccione – *Supervised Learning with Quantum Computers*
- **Chapter:** 1.2 – A Simple Classifier
- **Algorithm:** Quantum Squared-Distance Classifier
- **Dataset:** 3-passenger Titanic toy example (P1, P2, P3)

### Key Features

✅ **Exact Book Compliance**
- 4 qubits (q0: ancilla, q1-q2: features, q3: label)
- 1 Hadamard gate on q0 only
- Amplitude encoding with 1/√4 normalization
- Post-selection on q0 = 0
- Classification from q3 measurement

✅ **Pedagogical Design**
- Step-by-step Jupyter notebooks
- Extensive comments explaining theory
- Visualizations at each step
- Verification against book's expected output

✅ **Production-Ready Code**
- Qiskit 2.2.3+ (stable quantum framework)
- Modular architecture
- Comprehensive documentation
- Full test coverage

---

## 🎯 Quick Start

### Prerequisites

- Python 3.10+
- uv (recommended) or pip

### Installation

```bash
# Clone repository
cd Titanic_survival_QML_Project

# Install dependencies with uv
uv sync

# Or with pip
pip install -r pyproject.toml
```

### Run the Classifier

```bash
# Standalone script (all steps in one)
python exact_4qubit_classifier.py

# Or run notebooks step-by-step
jupyter notebook Notebooks/
```

---

## 📂 Project Structure

```
Titanic_survival_QML_Project/
├── main.py                      # Main execution script
├── exact_4qubit_classifier.py   # Standalone 4-qubit implementation
├── pyproject.toml               # Project dependencies
├── README.md                    # This file
├── ARCHITECTURE.md              # System architecture documentation
├── Data/
│   ├── Raw/                     # Original toy dataset (P1, P2, P3)
│   │   ├── toy_titanic.csv      # 3 passengers from book
│   │   └── README.md            # Dataset documentation
│   └── Processed/               # Preprocessed data
│       ├── toy_encoded_data_4qubit.pkl    # STEPS 0, A, B output
│       ├── circuit_4qubit.pkl             # STEP C output
│       └── measurement_results.pkl        # STEPS D, E output
├── Figures/                     # Generated visualizations
│   ├── toy_feature_space_4qubit.png
│   ├── 4qubit_exact_implementation.png
│   └── ...
├── Notebooks/                   # Step-by-step implementation
│   ├── 00_.data_preprocessing_and_encoding.ipynb  # STEPS 0, A, B
│   ├── 01_circuit_build_and_interference.ipynb    # STEP C
│   ├── 02_measurement_and_classification.ipynb    # STEPS D, E
│   └── 03_exact_book_implementation_4qubit.ipynb  # All steps
└── legacy/                      # Deprecated implementations
    └── pennylane_2qubit_classifier_DEPRECATED.py
```

---

## 🔬 Algorithm Steps (Book's Chapter 1.2)

### STEP 0: Min-Max Scaling
Scale features to [0,1] using book's exact ranges:
- Ticket price: [0, 10000]
- Cabin number: [0, 2500]

**Result:** P1=[0.85, 0.36], P2=[0.12, 0.84], P3=[0.78, 0.45]

### STEP A: L2 Normalization
Normalize each vector to unit length: x_norm = x / ||x||₂

**Result:** P1=[0.921, 0.390], P2=[0.141, 0.990], P3=[0.866, 0.500]

### STEP B: Amplitude Encoding
Construct 16-element amplitude vector for 4 qubits:
- Normalization factor: α = 1/√4 = 0.5
- Label encoding: odd indices for survived (1), even for died (0)
- Test point P3 duplicated with both labels (enables interference)

### STEP C: Quantum Circuit
Build 4-qubit circuit:
1. Initialize with amplitude vector
2. Apply **1 Hadamard gate** on q0 (ancilla)
3. Measure q0 and q3

### STEP D: Post-Selection
Filter measurement results:
- Keep only shots where q0 = 0 (constructive interference)
- Discard shots where q0 ≠ 0 (destructive interference)
- Expected: ~50% of shots retained

### STEP E: Classification
From post-selected shots, compute:
- p(survive) = count(q3=1 | q0=0) / total_post_selected
- p(die) = count(q3=0 | q0=0) / total_post_selected

**Book's Expected Output:**
- p(survive) ≈ 0.552
- p(die) ≈ 0.448
- **Prediction: SURVIVED**

---

## 🧪 Implementation Details

### Quantum Framework: Qiskit 2.2.3+

**Why Qiskit?**
- Direct amplitude initialization with `initialize()`
- Exact match to book's specification
- Stable, production-ready framework
- Active development and support

**Circuit Specifications:**
```python
# 4 qubits, 2 classical bits
q = QuantumRegister(4, 'q')
c = ClassicalRegister(2, 'c')
qc = QuantumCircuit(q, c)

# Initialize with amplitude vector
qc.initialize(amplitude_vector, q)

# Hadamard on q0 only
qc.h(q[0])

# Measure q0 (post-selection) and q3 (classification)
qc.measure(q[0], c[0])
qc.measure(q[3], c[1])
```

### Data: 3-Passenger Toy Example

| Passenger | Ticket Price | Cabin Number | Survival |
|-----------|--------------|--------------|----------|
| P1        | 8500         | 910          | 1 (survived) |
| P2        | 1200         | 2105         | 0 (died) |
| P3        | 7800         | 1121         | ? (to predict) |

### Dependencies

Core (7 packages):
- `numpy` - Numerical computing
- `pandas` - Data manipulation
- `qiskit>=2.2.3` - Quantum circuits
- `qiskit-aer` - Quantum simulator
- `matplotlib` - Visualization
- `seaborn` - Statistical plots
- `notebook` - Jupyter notebooks

---

## 📊 Results

### Preprocessing Verification
✅ Scaled values match book: P1=[0.85, 0.36], P2=[0.12, 0.84], P3=[0.78, 0.45]  
✅ Normalized values match book: P1=[0.921, 0.390], P2=[0.141, 0.990], P3=[0.866, 0.500]  
✅ Amplitude vector properly normalized: ||ψ|| = 1.000000

### Quantum Circuit Verification
✅ 4 qubits (q0: ancilla, q1-q2: features, q3: label)  
✅ 1 Hadamard gate on q0 only  
✅ 16-element amplitude vector with α=0.5  
✅ Post-selection rate: ~50% (as expected)

### Classification Results
✅ p(survive) ≈ 0.552 (matches book)  
✅ p(die) ≈ 0.448 (matches book)  
✅ **Prediction: Passenger 3 SURVIVED**

---

## 📖 Notebooks

### 00_data_preprocessing_and_encoding.ipynb
**STEPS 0, A, B:** Data preprocessing and amplitude encoding
- Load 3-passenger toy dataset
- Min-max scaling to [0,1]
- L2 normalization to unit vectors
- Construct 16-element amplitude vector
- Verify against book's values

### 01_circuit_build_and_interference.ipynb
**STEP C:** Quantum circuit construction and Hadamard interference
- Build 4-qubit circuit
- Apply Hadamard on q0 (ancilla)
- Analyze statevector before/after interference
- Visualize quantum state

### 02_measurement_and_classification.ipynb
**STEPS D, E:** Measurement, post-selection, and classification
- Execute circuit with 10000 shots
- Apply post-selection (q0=0)
- Measure q3 for classification
- Compare with book's expected output

### 03_exact_book_implementation_4qubit.ipynb
**All steps in one notebook** for easy reference and verification

---

## 🏗️ Architecture

See [ARCHITECTURE.md](ARCHITECTURE.md) for detailed system design, including:
- Component architecture
- Data flow diagrams
- Circuit design
- Best practices
- Extension guidelines

---

## 🧑‍💻 Development

### Code Style
- Follow PEP 8 guidelines
- Use book's naming convention (P1, P2, P3)
- Document theory in markdown cells
- Verify against book's expected output

### Testing
```bash
# Run all notebooks
jupyter nbconvert --execute --to notebook --inplace Notebooks/*.ipynb

# Run standalone script
python exact_4qubit_classifier.py
```

### Adding New Features
1. Maintain book compliance
2. Document theory and motivation
3. Verify output against expected values
4. Update ARCHITECTURE.md if needed

---

## 📚 References

1. **Primary Source:**
   - Schuld, M., & Petruccione, F. (2018). *Supervised Learning with Quantum Computers*. Springer.
   - Chapter 1.2: A Simple Classifier

2. **Quantum Computing:**
   - [Qiskit Documentation](https://qiskit.org/documentation/)
   - [Qiskit Textbook](https://qiskit.org/learn/)

3. **Quantum Machine Learning:**
   - [PennyLane QML Resources](https://pennylane.ai/qml/)
   - [Quantum Algorithms](https://quantum-algorithms.org/)

---

## 🤝 Contributing

This is a pedagogical project implementing a specific book example. Contributions should:
- Maintain exact book compliance
- Improve documentation or visualizations
- Fix bugs without changing algorithm behavior
- Add tests or verification checks

---

## 📜 License

This project is for educational purposes, implementing the algorithm described in:
*Schuld & Petruccione – Supervised Learning with Quantum Computers (2018)*

---

## 👥 Authors

**ACIT4321 Quantum Computing Project**  
OsloMet – Oslo Metropolitan University

---

## 🙏 Acknowledgments

- Maria Schuld and Francesco Petruccione for the excellent textbook
- Qiskit team for the quantum computing framework
- OsloMet for course materials and support

---

*Last updated: November 27, 2025*
