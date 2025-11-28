# Quantum Titanic Survival Classification

A complete implementation of the **quantum squared-distance classifier** toy example from Schuld & Petruccione's "Supervised Learning with Quantum Computing" (Chapter 1), applied to the Titanic dataset.

## 📖 Project Overview

This project demonstrates how quantum interference can be used for machine learning classification tasks. Using a 2-qubit quantum circuit with Hadamard transformations, we implement an interference-based classifier that encodes squared distances in measurement probabilities.

## 🎯 Key Features

- **Amplitude Encoding**: Classical data encoded in quantum state amplitudes
- **Quantum Interference**: Hadamard gates create interference patterns
- **Measurement-Based Classification**: Decision emerges from quantum measurements
- **Complete Pipeline**: Data preprocessing → Circuit design → Classification analysis

## 📂 Project Structure

```
Titanic_survival_QML_Project/
├── Notebooks/
│   ├── 00_.data_preprocessing_and_encoding.ipynb  # Step 0-5: Data prep & encoding
│   ├── 01_circuit_build_and_interference.ipynb    # Step C-D: Circuit & Hadamard
│   └── 02_measurement_and_classification.ipynb    # Step E: Measurement & results
├── Data/
│   ├── Raw/
│   │   └── titanic_data.csv
│   └── Processed/
│       ├── encoded_data.pkl
│       ├── circuit_results.pkl
│       └── final_results.pkl
├── Figures/
│   ├── feature_distributions.png
│   ├── normalized_feature_space.png
│   ├── interference_effect.png
│   ├── quantum_confusion_matrix.png
│   └── measurement_probabilities.png
├── quantum_classifier.py                          # Reusable classifier class
├── project_overview.md                            # Theory & algorithm details
└── README.md                                      # This file
```

## 🚀 Getting Started

### Prerequisites

This project uses **UV** for dependency management. The environment is already configured.

### Installation

```powershell
# Activate the UV environment (already done in your workspace)
.\.venv\Scripts\Activate

# All dependencies are installed via pyproject.toml
```

### Running the Notebooks

Execute notebooks in order:

1. **Notebook 00**: Data preprocessing and amplitude encoding
   - Loads Titanic dataset
   - Selects Age & Fare features
   - Normalizes data to unit vectors
   - Computes class prototypes
   
2. **Notebook 01**: Circuit build and interference
   - Constructs 2-qubit quantum circuit
   - Implements state preparation
   - Applies Hadamard transformation
   - Analyzes interference effects

3. **Notebook 02**: Measurement and classification
   - Measures quantum states
   - Classifies test samples
   - Evaluates accuracy
   - Compares with classical baseline

## 🔬 Theory

### The Quantum Squared-Distance Classifier

The algorithm encodes squared distances using quantum interference:

1. **State Preparation**: 
   ```
   |ψ⟩ = (|0⟩|a⟩ + |1⟩|b⟩) ⊗ |x⟩
   ```
   where |x⟩ is the test point, |a⟩ and |b⟩ are class prototypes

2. **Hadamard Transformation**: 
   Creates interference between class branches
   ```
   H ⊗ I ⊗ I |ψ⟩
   ```

3. **Measurement**: 
   P(first qubit = 0) encodes distance information
   - Predict class 0 if P(|0⟩) > P(|1⟩)
   - Otherwise predict class 1

### Key Concepts

- **Amplitude Encoding**: Data → quantum amplitudes (exponentially compact)
- **Interference**: Quantum superposition enables distance calculations
- **Measurement Collapse**: Classification decision from quantum measurement

## 📊 Results

The implementation demonstrates:
- ✅ Successful quantum circuit execution
- ✅ Interference-based distance encoding
- ✅ Measurement-driven classification
- ✅ Comparable performance to classical baseline

## 📚 References

1. **Schuld, M., & Petruccione, F. (2018)**. *Supervised Learning with Quantum Computers*. Springer. Chapter 1.
2. **Weigold et al. (2021)**. *Expanding Data Encoding Patterns for Quantum Algorithms*.
3. **PennyLane Documentation**: https://pennylane.ai/

## 🛠️ Implementation Details

- **Quantum Framework**: PennyLane
- **Simulator**: `default.qubit`
- **Qubits**: 2 (1 class qubit + 1 data qubit)
- **Gates**: Hadamard, RY, Controlled-RY
- **Features**: Age & Fare (normalized)

## 💡 Key Insights

1. **Quantum = Classical for Toy Example**: Same logic, different implementation
2. **Interference is Key**: Encodes distances in measurement probabilities
3. **Scalability Challenge**: Real advantage requires larger problems
4. **Educational Value**: Excellent introduction to quantum ML concepts

## 📝 Notes

- This is a **toy example** for educational purposes
- Real quantum advantage requires more qubits and data
- Circuit depth is minimal (shallow circuit)
- Suitable for NISQ-era quantum computers

## 🤝 Contributing

This is an academic project. For questions or improvements, please reach out through the course channels.

## 📄 License

Educational use for ACIT4321 Quantum Computing course at OsloMet.

---

**✨ Project Complete! Explore the notebooks to see quantum machine learning in action.**
