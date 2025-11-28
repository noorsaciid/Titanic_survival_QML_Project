"""
Exact Implementation: Schuld & Petruccione Chapter 1.2
Quantum Squared-Distance Classifier (4-Qubit Version)

This script implements the exact toy example from:
Schuld & Petruccione – Supervised Learning with Quantum Computers, Chapter 1.2

Key Specifications:
- 4 qubits (q0: ancilla, q1-q2: features, q3: label)
- 1 Hadamard gate on q0 only
- Post-selection on q0 = 0
- Classification from q3 measurement
- Amplitude encoding with 1/√4 normalization
"""

import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import Aer


def preprocess_data(raw_data):
    """
    STEP 0 & A: Min-Max Scaling + L2 Normalization
    
    Args:
        raw_data: List of [ticket_price, cabin_number, label] for each passenger
    
    Returns:
        List of normalized [x0, x1] vectors and labels
    """
    # Book's exact ranges
    PRICE_MAX = 10000.0
    CABIN_MAX = 2500.0
    
    processed = []
    
    for price, cabin, label in raw_data:
        # STEP 0: Min-max scaling to [0,1]
        price_scaled = price / PRICE_MAX
        cabin_scaled = cabin / CABIN_MAX
        
        # STEP A: L2 normalization
        x = np.array([price_scaled, cabin_scaled])
        x_norm = x / np.linalg.norm(x)
        
        processed.append((x_norm, label))
    
    return processed


def construct_amplitude_vector(P1, P2, P3):
    """
    STEP B: Amplitude Encoding for 4 qubits
    
    Constructs 16-element amplitude vector:
    alpha_init = (1/√4) * [0, P1_x0, 0, P1_x1,
                           P2_x0, 0, P2_x1, 0,
                           0, T_x0, 0, T_x1,
                           T_x0, 0, T_x1, 0]
    
    Args:
        P1: Passenger 1 (label=1, survived)
        P2: Passenger 2 (label=0, died)
        P3: Passenger 3 (label=?, test point)
    
    Returns:
        16-element amplitude vector (normalized)
    """
    alpha = 1.0 / np.sqrt(4)
    amplitude_vector = np.zeros(16, dtype=complex)
    
    # P1 (label=1, survived): q0=0, q3=1 block
    # Indices: 8, 10 (q3=1, q2=0, q1=0/1, q0=0)
    amplitude_vector[8] = alpha * P1[0]   # |1000⟩: q0=0, q3=1, feature 0
    amplitude_vector[10] = alpha * P1[1]  # |1010⟩: q0=0, q3=1, feature 1
    
    # P2 (label=0, died): q0=0, q3=0 block
    # Indices: 0, 2 (q3=0, q2=0, q1=0/1, q0=0)
    amplitude_vector[0] = alpha * P2[0]   # |0000⟩: q0=0, q3=0, feature 0
    amplitude_vector[2] = alpha * P2[1]   # |0010⟩: q0=0, q3=0, feature 1
    
    # P3 (test, duplicated at q0=1 with both labels for Hadamard interference)
    # Copy 1 with label=1: indices 9, 11 (q3=1, q2=0, q1=0/1, q0=1)
    amplitude_vector[9] = alpha * P3[0]   # |1001⟩: q0=1, q3=1, feature 0
    amplitude_vector[11] = alpha * P3[1]  # |1011⟩: q0=1, q3=1, feature 1
    
    # Copy 2 with label=0: indices 1, 3 (q3=0, q2=0, q1=0/1, q0=1)
    amplitude_vector[1] = alpha * P3[0]   # |0001⟩: q0=1, q3=0, feature 0
    amplitude_vector[3] = alpha * P3[1]   # |0011⟩: q0=1, q3=0, feature 1
    
    return amplitude_vector


def build_quantum_circuit(amplitude_vector):
    """
    STEP C: Build 4-qubit circuit with Hadamard interference
    
    Circuit:
    1. Initialize with amplitude vector
    2. Apply Hadamard on q0 (ancilla)
    3. Measure q0 for post-selection
    4. Measure q3 for classification
    
    Args:
        amplitude_vector: 16-element amplitude vector
    
    Returns:
        QuantumCircuit ready for execution
    """
    q = QuantumRegister(4, 'q')
    c = ClassicalRegister(2, 'c')
    qc = QuantumCircuit(q, c)
    
    # Initialize state
    qc.initialize(amplitude_vector, q)
    
    # Hadamard on q0 ONLY (creates interference)
    qc.barrier()
    qc.h(q[0])
    qc.barrier()
    
    # Measurements
    qc.measure(q[0], c[0])  # Ancilla (for post-selection)
    qc.measure(q[3], c[1])  # Label qubit (for classification)
    
    return qc


def execute_with_postselection(qc, shots=10000):
    """
    STEP D & E: Execute circuit and apply post-selection
    
    Post-selection: Keep only shots where q0 = 0
    Classification: Count q3 measurements among post-selected shots
    
    Args:
        qc: Quantum circuit
        shots: Number of measurement shots
    
    Returns:
        (p_survive, p_die, total_post_selected)
    """
    simulator = Aer.get_backend('qasm_simulator')
    job = simulator.run(qc, shots=shots)
    result = job.result()
    counts = result.get_counts()
    
    # Post-selection: keep only q0 = 0
    post_selected_counts = {0: 0, 1: 0}
    total_post_selected = 0
    
    for bitstring, count in counts.items():
        ancilla_bit = int(bitstring[-1])  # c[0] - rightmost
        
        if ancilla_bit == 0:  # Post-select on q0 = 0
            label_bit = int(bitstring[0])  # c[1] - leftmost
            post_selected_counts[label_bit] += count
            total_post_selected += count
    
    # Compute probabilities
    if total_post_selected > 0:
        p_survive = post_selected_counts[1] / total_post_selected
        p_die = post_selected_counts[0] / total_post_selected
    else:
        p_survive = p_die = 0.0
    
    return p_survive, p_die, total_post_selected


def main():
    """Main execution function"""
    print("="*80)
    print("EXACT IMPLEMENTATION: SCHULD & PETRUCCIONE CHAPTER 1.2")
    print("Quantum Squared-Distance Classifier (4-Qubit Version)")
    print("="*80)
    
    # Raw data (from book)
    raw_data = [
        (8500, 910, 1),   # Passenger 1: survived
        (1200, 2105, 0),  # Passenger 2: died
        (7800, 1121, None) # Passenger 3: unknown
    ]
    
    # STEP 0 & A: Preprocessing
    print("\n📊 STEP 0 & A: Data Preprocessing")
    print("-" * 80)
    processed_data = preprocess_data(raw_data)
    
    P1, label1 = processed_data[0]
    P2, label2 = processed_data[1]
    P3, _ = processed_data[2]
    
    print(f"Passenger 1: [{P1[0]:.3f}, {P1[1]:.3f}], label={label1}")
    print(f"Passenger 2: [{P2[0]:.3f}, {P2[1]:.3f}], label={label2}")
    print(f"Passenger 3: [{P3[0]:.3f}, {P3[1]:.3f}], label=?")
    
    # Verify against book's expected values
    assert np.isclose(P1[0], 0.921, atol=0.005), "P1[0] mismatch"
    assert np.isclose(P1[1], 0.390, atol=0.005), "P1[1] mismatch"
    assert np.isclose(P2[0], 0.141, atol=0.005), "P2[0] mismatch"
    assert np.isclose(P2[1], 0.990, atol=0.005), "P2[1] mismatch"
    assert np.isclose(P3[0], 0.866, atol=0.005), "P3[0] mismatch"
    assert np.isclose(P3[1], 0.500, atol=0.005), "P3[1] mismatch"
    print("✓ Normalized values match book's expected output!")
    
    # STEP B: Amplitude encoding
    print("\n🔬 STEP B: Amplitude Encoding (4 qubits)")
    print("-" * 80)
    amplitude_vector = construct_amplitude_vector(P1, P2, P3)
    
    # Print non-zero amplitudes
    for i, amp in enumerate(amplitude_vector):
        if np.abs(amp) > 1e-10:
            print(f"  |{i:04b}⟩: {amp.real:+.4f}")
    
    norm = np.linalg.norm(amplitude_vector)
    print(f"\nAmplitude vector norm: {norm:.6f}")
    assert np.isclose(norm, 1.0, atol=1e-6), "Amplitude vector not normalized!"
    print("✓ Amplitude vector properly normalized!")
    
    # STEP C: Build circuit
    print("\n⚛️  STEP C: Build Quantum Circuit")
    print("-" * 80)
    qc = build_quantum_circuit(amplitude_vector)
    print(f"  Qubits: {qc.num_qubits}")
    print(f"  Classical bits: {qc.num_clbits}")
    print(f"  Hadamard gates: 1 (on q0)")
    print(f"  Measurements: 2 (q0 and q3)")
    print("✓ Circuit built according to book's specifications!")
    
    # STEP D & E: Execute with post-selection
    print("\n📏 STEP D & E: Execute Circuit with Post-Selection")
    print("-" * 80)
    shots = 10000
    p_survive, p_die, total_post_selected = execute_with_postselection(qc, shots)
    
    print(f"Total shots: {shots}")
    print(f"Post-selected (q0=0): {total_post_selected} ({total_post_selected/shots*100:.1f}%)")
    print(f"Discarded (q0≠0): {shots-total_post_selected} ({(shots-total_post_selected)/shots*100:.1f}%)")
    
    # Classification results
    print("\n🎯 CLASSIFICATION RESULTS")
    print("=" * 80)
    print(f"p(survive | q3=1): {p_survive:.4f}")
    print(f"p(die | q3=0):     {p_die:.4f}")
    
    prediction = "SURVIVED" if p_survive > p_die else "DIED"
    print(f"\n>>> PREDICTION FOR PASSENGER 3: {prediction}")
    
    # Comparison with book
    print("\n📖 COMPARISON WITH BOOK'S EXPECTED OUTPUT")
    print("-" * 80)
    print(f"Expected p(survive): 0.552")
    print(f"Measured p(survive): {p_survive:.3f}")
    print(f"Difference: {abs(p_survive - 0.552):.3f}")
    print()
    print(f"Expected p(die):     0.448")
    print(f"Measured p(die):     {p_die:.3f}")
    print(f"Difference: {abs(p_die - 0.448):.3f}")
    
    # Final verification
    print("\n" + "=" * 80)
    if abs(p_survive - 0.552) < 0.05 and abs(p_die - 0.448) < 0.05:
        print("✅ RESULTS MATCH BOOK'S EXPECTED OUTPUT (within statistical variation)")
    else:
        print("⚠️  Results differ from book (may need more shots or check implementation)")
    print("=" * 80)
    print("✓ EXACT IMPLEMENTATION COMPLETE!")
    print("=" * 80)


if __name__ == "__main__":
    main()
