# Abstract and Keywords

## Abstract

This project implements and validates a quantum machine learning classifier based on the interference-based squared-distance algorithm introduced by Schuld and Petruccione (Chapter 1.2). The implementation demonstrates quantum amplitude encoding and Hadamard-gate interference for binary classification using a toy Titanic survival dataset with three passengers.

The algorithm encodes normalized feature vectors into quantum amplitudes of a 4-qubit system, where an ancilla qubit (q0) enables quantum interference through a single Hadamard gate, two qubits (q1-q2) encode the features, and one qubit (q3) represents the class label. The quantum circuit creates superposition states that, after post-selection on the ancilla qubit measuring 0, yield measurement probabilities proportional to squared Euclidean distances between the test point and training exemplars.

The implementation was executed on both the Qiskit Aer simulator and IBM Quantum hardware (ibm_fez, 156-qubit heavy-hex architecture). With 10,000 measurement shots, the post-selection process retained approximately 50% of samples as theoretically expected. The classification probabilities closely matched the textbook's expected values: p(survive) = 0.552 (expected: 0.552) and p(die) = 0.448 (expected: 0.448), successfully predicting that Passenger 3 survived.

Hardware execution on IBM Quantum revealed noise-induced deviations from ideal simulator results, with average absolute errors increasing by a factor of 1.5-2× due to gate imperfections, decoherence (T₁ ≈ 100-200 μs), and readout errors. Despite these limitations, the hardware results remained within acceptable bounds for this demonstration, validating the quantum interference mechanism's robustness.

This work demonstrates the fundamental principles of quantum machine learning through a minimal circuit implementation, highlighting both the theoretical elegance of amplitude encoding and quantum interference, as well as practical challenges including post-selection overhead (50% sample loss) and hardware noise sensitivity. The implementation serves as an educational reference for understanding quantum-classical hybridization in supervised learning, while the Clifford-only circuit design (using only Hadamard gates) confirms the algorithm's classical simulability—emphasizing that quantum advantage requires more complex quantum operations.

**Word Count:** ~300 words

---

## Keywords

**Primary Keywords:**
- Quantum Machine Learning
- Quantum Computing
- Supervised Learning
- Binary Classification
- Quantum Interference

**Technical Keywords:**
- Amplitude Encoding
- Hadamard Gate
- Post-Selection
- Squared-Distance Classifier
- Qiskit

**Application Keywords:**
- IBM Quantum Hardware
- Titanic Dataset
- Quantum Circuit Design
- Noise Analysis
- Hardware vs Simulator Comparison

**Methodological Keywords:**
- Feature Normalization
- Min-Max Scaling
- L2 Normalization
- Quantum State Vector
- Measurement Probabilities

**Theoretical Keywords:**
- Clifford Circuit
- Constructive Interference
- Ancilla Qubit
- Schuld-Petruccione Algorithm
- Quantum Simulation

---

## Suggested Keywords for Different Contexts

### For Academic Paper Submission:
Quantum Machine Learning, Amplitude Encoding, Supervised Classification, Quantum Interference, IBM Quantum Computing, Post-Selection, Binary Classifier, Qiskit Framework, Hardware Validation

### For Conference Presentation:
Quantum Computing, Machine Learning, Hadamard Interference, Quantum Circuit Design, Real Hardware Execution, Educational Implementation, Titanic Dataset, Noise Analysis

### For Technical Report:
Quantum Algorithm Implementation, 4-Qubit Circuit, Squared-Distance Classifier, Feature Encoding, Quantum-Classical Hybrid, Measurement Statistics, Hardware Fidelity, Schuld-Petruccione Textbook

---

## Abstract Highlights (Bullet Point Version)

For presentations or executive summaries:

- **Objective:** Implement and validate Schuld-Petruccione quantum squared-distance classifier
- **Dataset:** 3-passenger toy Titanic survival dataset (2 training, 1 test)
- **Circuit:** 4-qubit design with 1 Hadamard gate and amplitude encoding
- **Execution:** Both Qiskit Aer simulator and IBM Quantum hardware (ibm_fez)
- **Results:** Classification probabilities matched expected values (p_survive = 0.552)
- **Post-selection:** ~50% measurement overhead as theoretically predicted
- **Hardware Impact:** 1.5-2× error increase due to noise, decoherence, and readout errors
- **Contribution:** Educational reference for quantum ML fundamentals and practical limitations
- **Limitation:** Clifford-only circuit is classically simulable (no quantum advantage)

---

## SEO-Optimized Keywords

For online repositories or research databases:

quantum machine learning tutorial, IBM quantum computing, Qiskit implementation, quantum classifier, amplitude encoding example, Hadamard gate interference, quantum supervised learning, Schuld Petruccione implementation, quantum circuit design, quantum hardware validation, post-selection quantum computing, binary classification quantum algorithm, quantum noise analysis, educational quantum computing project

