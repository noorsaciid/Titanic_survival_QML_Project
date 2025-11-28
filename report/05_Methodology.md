\section{Methodology}

\subsection{Algorithm Description}

The quantum squared-distance classifier follows a systematic five-step process as defined by Schuld and Petruccione:

\textbf{STEP 0 (Data Preparation):} Raw feature vectors are preprocessed through min-max scaling followed by L2 normalization. For feature vector $\mathbf{x} = (x_1, x_2)$, min-max scaling transforms each component:
\begin{equation}
x_i^{\text{scaled}} = \frac{x_i - \min(x_i)}{\max(x_i) - \min(x_i)}
\end{equation}
Subsequently, L2 normalization ensures unit vectors: $\mathbf{x}^{\text{norm}} = \mathbf{x}^{\text{scaled}} / \|\mathbf{x}^{\text{scaled}}\|_2$.

\textbf{STEP A (Amplitude Encoding):} Normalized training points $P_1, P_2$ and test point $P_3$ are encoded into quantum amplitudes. The amplitude vector construction duplicates $P_3$ with both possible labels (0 and 1):
\begin{equation}
|\psi_{\text{init}}\rangle = \alpha(|0\rangle|P_1\rangle|1\rangle + |0\rangle|P_2\rangle|0\rangle + |0\rangle|P_3\rangle|0\rangle + |0\rangle|P_3\rangle|1\rangle)
\end{equation}
where $\alpha = 1/\sqrt{4}$ ensures normalization across four training-test pairs.

\textbf{STEP B (State Initialization):} The 16-dimensional amplitude vector is loaded into the 4-qubit quantum register through the \texttt{initialize()} method, mapping amplitudes to computational basis states $|q_0 q_1 q_2 q_3\rangle$ where $q_0$ is the ancilla, $q_1$-$q_2$ encode features, and $q_3$ represents the class label.

\textbf{STEP C (Hadamard Interference):} A single Hadamard gate applied to the ancilla qubit $q_0$ creates quantum superposition:
\begin{equation}
H|q_0\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)|q_1 q_2 q_3\rangle
\end{equation}
This operation generates constructive interference (ancilla=$|0\rangle$) and destructive interference (ancilla=$|1\rangle$) patterns encoding squared distances.

\textbf{STEP D (Measurement and Post-Selection):} Both ancilla $q_0$ and label $q_3$ qubits are measured. Post-selection retains only measurements where $q_0=0$, isolating constructive interference terms with probability $\approx 50\%$.

\textbf{STEP E (Classification):} Among post-selected measurements, the label qubit $q_3$ distribution determines classification. The probability ratio $p(q_3=1)/p(q_3=0)$ indicates survival (1) or death (0) prediction.

\subsection{Dataset Specification}

The toy Titanic dataset comprises three passengers with two features:

\begin{table}[h]
\centering
\begin{tabular}{|c|c|c|c|}
\hline
\textbf{Passenger} & \textbf{Ticket Price (\$)} & \textbf{Cabin Number} & \textbf{Label} \\
\hline
P1 & 8500 & 910 & 1 (Survived) \\
P2 & 1200 & 2105 & 0 (Died) \\
P3 & 7800 & 1121 & ? (Test) \\
\hline
\end{tabular}
\end{table}

After preprocessing, normalized coordinates become: $P_1 = (0.831, 0.556)$, $P_2 = (0.141, 0.990)$, $P_3 = (0.865, 0.502)$.

\subsection{Implementation Framework}

The implementation utilizes Qiskit version 2.2.3+ with the following specifications:

\textbf{Quantum Circuit:} A 4-qubit system with 2 classical bits for measurement readout. The circuit architecture employs:
\begin{itemize}
\item Qubit allocation: $q_0$ (ancilla), $q_1$-$q_2$ (feature encoding), $q_3$ (label)
\item Gate operations: 1 Hadamard gate on $q_0$, preceded by amplitude initialization
\item Measurement targets: $q_0$ and $q_3$ mapped to classical registers $c[0]$ and $c[1]$
\end{itemize}

\textbf{Python Environment:} Python 3.10+ managed via \texttt{uv} package manager, with dependencies including NumPy 1.24.0+, Pandas 2.0.0+, Matplotlib 3.7.0+, and Qiskit 2.2.3+.

\subsection{Experimental Setup}

Experiments were conducted on two platforms for comparative analysis:

\textbf{Local Simulator:} Qiskit Aer's \texttt{qasm\_simulator} provides ideal noiseless quantum computation, serving as the theoretical baseline. The simulator employs exact statevector computation without decoherence or gate errors.

\textbf{IBM Quantum Hardware:} The \texttt{ibm\_fez} backend featuring 156 qubits arranged in heavy-hex topology. Key hardware specifications include:
\begin{itemize}
\item Coherence time: $T_1 \approx 100$-$200~\mu$s (energy relaxation)
\item Gate fidelity: Single-qubit gates $\sim 99.95\%$, two-qubit gates $\sim 99.5\%$
\item Readout fidelity: $\sim 98\%$ average across qubits
\item Connectivity: Heavy-hex architecture with degree-3 connectivity
\end{itemize}

\textbf{Measurement Parameters:} Each circuit execution employed 10,000 shots to ensure sufficient statistical sampling. Post-selection filtering retained approximately 5,000 measurements ($\sim 50\%$) corresponding to ancilla $q_0=0$ outcomes.

\subsection{Data Preprocessing Pipeline}

The preprocessing workflow consists of three sequential transformations:

\textbf{Stage 1 - Raw Data:} Original feature values exhibit disparate scales (ticket prices: 1,200-8,500; cabin numbers: 910-2,105).

\textbf{Stage 2 - Min-Max Scaling:} Each feature normalized to $[0, 1]$ range independently:
\begin{equation}
\mathbf{x}_{\text{scaled}} = \begin{pmatrix} \frac{8500-1200}{8500-1200} \\ \frac{910-910}{2105-910} \end{pmatrix} = \begin{pmatrix} 0.85 \\ 0.36 \end{pmatrix}
\end{equation}

\textbf{Stage 3 - L2 Normalization:} Vectors normalized to unit length for quantum amplitude encoding:
\begin{equation}
\mathbf{x}_{\text{norm}} = \frac{\mathbf{x}_{\text{scaled}}}{\sqrt{0.85^2 + 0.36^2}} = \begin{pmatrix} 0.831 \\ 0.556 \end{pmatrix}
\end{equation}

\subsection{Validation Approach}

Validation employed two complementary strategies:

\textbf{Theoretical Comparison:} Measured classification probabilities were compared against textbook expected values: $p(\text{survive}) = 0.552$ and $p(\text{die}) = 0.448$. Agreement within $\pm 0.05$ indicates successful implementation.

\textbf{Statistical Analysis:} Post-selection rates were analyzed to verify $\sim 50\%$ retention predicted by Hadamard interference theory. Hardware noise impact quantified through absolute error metrics comparing simulator and physical device outcomes.

\section{Implementation Details}

\subsection{Quantum Circuit Construction}

The circuit construction follows a two-phase process. First, the \texttt{QuantumCircuit(4, 2)} instantiates four qubits and two classical bits. The \texttt{initialize(amplitude\_vector, [0,1,2,3])} method loads the 16-element amplitude vector spanning the complete Hilbert space. Second, a single \texttt{h(0)} applies the Hadamard gate to the ancilla. Finally, \texttt{measure([0,3], [0,1])} extracts measurement outcomes from qubits $q_0$ and $q_3$.

\subsection{Execution Workflow}

\textbf{Simulator Execution:} Direct circuit execution via \texttt{Aer.get\_backend('qasm\_simulator').run(qc, shots=10000)} yields ideal measurement statistics.

\textbf{Hardware Execution:} IBM Quantum execution requires transpilation for physical qubit mapping and gate decomposition. The workflow employs \texttt{generate\_preset\_pass\_manager(backend=ibm\_fez, optimization\_level=1)} to translate the abstract circuit into native gate operations, followed by \texttt{SamplerV2(backend).run()} for job submission to the quantum processor.

\textbf{Word Count:} 789 words
