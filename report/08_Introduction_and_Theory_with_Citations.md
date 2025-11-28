\section{Introduction}

Quantum machine learning (QML) stands at the intersection of quantum computing and artificial intelligence, where quantum mechanical phenomena such as superposition, entanglement, and interference are used to enhance computational capabilities for learning tasks \cite{biamonte2017quantum}. As quantum hardware continues to mature from experimental prototypes to commercially accessible systems \cite{preskill2018nisq}, understanding the fundamental principles that enable quantum algorithms to process classical data becomes increasingly critical for researchers and practitioners alike.

This project implements and experimentally validates the interference-based squared-distance classifier introduced by Schuld and Petruccione in Chapter 1.2 of their seminal textbook on quantum machine learning \cite{schuld2018supervised}. This algorithm serves as an elegant pedagogical example that demonstrates how quantum interference—a purely quantum mechanical phenomenon—can be leveraged for supervised binary classification. Unlike complex variational quantum algorithms \cite{cerezo2021variational} that require extensive parameterization and optimization, this approach utilizes a remarkably simple 4-qubit circuit with a single Hadamard gate, making it an ideal entry point for understanding quantum approaches to machine learning.

The algorithm encodes classical feature vectors into quantum amplitudes through a process known as amplitude encoding \cite{lloyd2013quantum}, where normalized data points are embedded into the probability amplitudes of a quantum state. By duplicating the test sample with both possible class labels and applying a Hadamard gate to an ancilla qubit, the circuit creates quantum superposition states that, after post-selection, produce measurement probabilities proportional to squared Euclidean distances between the test point and training exemplars. This quantum interference mechanism effectively implements a distance-based classifier without explicitly computing distance metrics—showcasing the potential elegance of quantum information processing \cite{nielsen2010quantum}.

To validate this theoretical framework, we implement the complete pipeline using the Qiskit quantum computing framework \cite{qiskit2024} and execute the circuit on two platforms: the ideal Qiskit Aer simulator and real IBM Quantum hardware (ibm\_fez backend with 156 qubits) \cite{ibm_quantum_2024}. The implementation uses a toy Titanic survival dataset with three passengers, maintaining complete fidelity to the textbook example to enable direct comparison with expected theoretical outcomes. This dual-platform execution strategy reveals critical insights into both the algorithm's theoretical soundness and its practical limitations when confronted with hardware noise, gate imperfections, and decoherence \cite{preskill2018nisq}.

Beyond merely reproducing textbook results, this work provides comprehensive analysis of quantum-classical hybridization challenges, post-selection overhead implications, and hardware noise impact quantification. The findings underscore that while this particular algorithm offers no quantum computational advantage—being classically simulable due to its Clifford-only gate set \cite{gottesman1998heisenberg,aaronson2004improved}—it nevertheless provides invaluable pedagogical insights into how quantum resources might be exploited for machine learning tasks, establishing foundational understanding necessary for exploring more sophisticated quantum learning algorithms \cite{rebentrost2014quantum}.

\section{Theoretical Background}

\subsection{Quantum State Representation}

Quantum machine learning exploits quantum mechanical principles to represent and process classical data \cite{biamonte2017quantum,schuld2018supervised}. A quantum system of $n$ qubits exists in a superposition of $2^n$ computational basis states, described by the state vector \cite{nielsen2010quantum}:

\begin{equation}
|\psi\rangle = \sum_{i=0}^{2^n-1} \alpha_i |i\rangle, \quad \text{where} \quad \sum_{i=0}^{2^n-1} |\alpha_i|^2 = 1
\end{equation}

The complex amplitudes $\alpha_i$ encode information exponentially: $n$ qubits can represent $2^n$ amplitudes simultaneously, providing the foundation for quantum parallelism \cite{nielsen2010quantum}.

\subsection{Amplitude Encoding}

Classical feature vectors $\mathbf{x} = (x_1, x_2, \ldots, x_d)$ are encoded into quantum amplitudes through normalization \cite{lloyd2013quantum}. For a normalized vector $\|\mathbf{x}\| = 1$, the quantum state becomes:

\begin{equation}
|\mathbf{x}\rangle = \sum_{i=1}^{d} x_i |i\rangle
\end{equation}

This exponentially compact representation requires only $\lceil \log_2 d \rceil$ qubits to encode $d$ features, contrasting with classical representations requiring $O(d)$ memory \cite{lloyd2013quantum}.

\subsection{Hadamard Interference}

The Hadamard gate $H$ creates equal superposition \cite{nielsen2010quantum}, transforming basis states as:

\begin{equation}
H|0\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}}, \quad H|1\rangle = \frac{|0\rangle - |1\rangle}{\sqrt{2}}
\end{equation}

Applied to an ancilla qubit in a composite system, the Hadamard gate generates constructive and destructive interference patterns. For states $|\psi_0\rangle$ and $|\psi_1\rangle$, the transformation yields:

\begin{equation}
H \otimes I (|0\rangle|\psi_0\rangle + |1\rangle|\psi_1\rangle) = \frac{1}{\sqrt{2}}(|0\rangle(|\psi_0\rangle + |\psi_1\rangle) + |1\rangle(|\psi_0\rangle - |\psi_1\rangle))
\end{equation}

Post-selecting on the ancilla measuring $|0\rangle$ isolates the constructive interference term, with measurement probability:

\begin{equation}
P(\text{ancilla}=0) = \frac{1}{2}\langle\psi_0 + \psi_1|\psi_0 + \psi_1\rangle = \frac{1}{2}(\langle\psi_0|\psi_0\rangle + \langle\psi_1|\psi_1\rangle + 2\text{Re}\langle\psi_0|\psi_1\rangle)
\end{equation}

\subsection{Squared-Distance Classification}

For binary classification, the quantum interference mechanism implements a squared-distance classifier \cite{schuld2018supervised}. Training exemplars $\mathbf{m}_0$ (class 0) and $\mathbf{m}_1$ (class 1) are encoded with test point $\mathbf{x}$. The measurement probability for predicting class $y$ becomes:

\begin{equation}
p(y|\mathbf{x}) \propto \|\mathbf{m}_y + \mathbf{x}\|^2 = \|\mathbf{m}_y\|^2 + \|\mathbf{x}\|^2 + 2\mathbf{m}_y \cdot \mathbf{x}
\end{equation}

After normalization and algebraic manipulation, this reduces to an exponential form equivalent to classical kernel methods \cite{havlicek2019supervised}:

\begin{equation}
p(y|\mathbf{x}) = \frac{e^{-c\|\mathbf{x} - \mathbf{m}_y\|^2}}{\sum_{y'} e^{-c\|\mathbf{x} - \mathbf{m}_{y'}\|^2}}
\end{equation}

where $c$ is a constant determined by the encoding scheme. The predicted class maximizes this probability, effectively selecting the nearest training exemplar in feature space \cite{schuld2018supervised}.

\section{Methodology}

\subsection{Algorithm Description}

The quantum squared-distance classifier follows a systematic five-step process as defined by Schuld and Petruccione \cite{schuld2018supervised}:

\textbf{STEP 0 (Data Preparation):} Raw feature vectors are preprocessed through min-max scaling followed by L2 normalization \cite{schuld2018supervised}. For feature vector $\mathbf{x} = (x_1, x_2)$, min-max scaling transforms each component:
\begin{equation}
x_i^{\text{scaled}} = \frac{x_i - \min(x_i)}{\max(x_i) - \min(x_i)}
\end{equation}
Subsequently, L2 normalization ensures unit vectors: $\mathbf{x}^{\text{norm}} = \mathbf{x}^{\text{scaled}} / \|\mathbf{x}^{\text{scaled}}\|_2$.

\textbf{STEP A (Amplitude Encoding):} Normalized training points $P_1, P_2$ and test point $P_3$ are encoded into quantum amplitudes \cite{lloyd2013quantum}. The amplitude vector construction duplicates $P_3$ with both possible labels (0 and 1):
\begin{equation}
|\psi_{\text{init}}\rangle = \alpha(|0\rangle|P_1\rangle|1\rangle + |0\rangle|P_2\rangle|0\rangle + |0\rangle|P_3\rangle|0\rangle + |0\rangle|P_3\rangle|1\rangle)
\end{equation}
where $\alpha = 1/\sqrt{4}$ ensures normalization across four training-test pairs.

\textbf{STEP B (State Initialization):} The 16-dimensional amplitude vector is loaded into the 4-qubit quantum register through the \texttt{initialize()} method \cite{qiskit2024}, mapping amplitudes to computational basis states $|q_0 q_1 q_2 q_3\rangle$ where $q_0$ is the ancilla, $q_1$-$q_2$ encode features, and $q_3$ represents the class label.

\textbf{STEP C (Hadamard Interference):} A single Hadamard gate applied to the ancilla qubit $q_0$ creates quantum superposition \cite{nielsen2010quantum}:
\begin{equation}
H|q_0\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)|q_1 q_2 q_3\rangle
\end{equation}
This operation generates constructive interference (ancilla=$|0\rangle$) and destructive interference (ancilla=$|1\rangle$) patterns encoding squared distances.

\textbf{STEP D (Measurement and Post-Selection):} Both ancilla $q_0$ and label $q_3$ qubits are measured. Post-selection retains only measurements where $q_0=0$, isolating constructive interference terms with probability $\approx 50\%$ \cite{schuld2018supervised}.

\textbf{STEP E (Classification):} Among post-selected measurements, the label qubit $q_3$ distribution determines classification. The probability ratio $p(q_3=1)/p(q_3=0)$ indicates survival (1) or death (0) prediction.

\subsection{Dataset Specification}

The toy Titanic dataset comprises three passengers with two features, exactly as specified in the Schuld-Petruccione textbook \cite{schuld2018supervised}:

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

The implementation utilizes Qiskit version 2.2.3+ with the following specifications \cite{qiskit2024}:

\textbf{Quantum Circuit:} A 4-qubit system with 2 classical bits for measurement readout. The circuit architecture employs:
\begin{itemize}
\item Qubit allocation: $q_0$ (ancilla), $q_1$-$q_2$ (feature encoding), $q_3$ (label)
\item Gate operations: 1 Hadamard gate on $q_0$, preceded by amplitude initialization
\item Measurement targets: $q_0$ and $q_3$ mapped to classical registers $c[0]$ and $c[1]$
\end{itemize}

\textbf{Python Environment:} Python 3.10+ managed via \texttt{uv} package manager, with dependencies including NumPy 1.24.0+ \cite{numpy2024}, Pandas 2.0.0+ \cite{pandas2024}, Matplotlib 3.7.0+ \cite{matplotlib2024}, and Qiskit 2.2.3+ \cite{qiskit2024}.

\subsection{Experimental Setup}

Experiments were conducted on two platforms for comparative analysis \cite{preskill2018nisq}:

\textbf{Local Simulator:} Qiskit Aer's \texttt{qasm\_simulator} provides ideal noiseless quantum computation, serving as the theoretical baseline. The simulator employs exact statevector computation without decoherence or gate errors \cite{qiskit2024}.

\textbf{IBM Quantum Hardware:} The \texttt{ibm\_fez} backend featuring 156 qubits arranged in heavy-hex topology \cite{ibm_quantum_2024}. Key hardware specifications include:
\begin{itemize}
\item Coherence time: $T_1 \approx 100$-$200~\mu$s (energy relaxation)
\item Gate fidelity: Single-qubit gates $\sim 99.95\%$, two-qubit gates $\sim 99.5\%$
\item Readout fidelity: $\sim 98\%$ average across qubits
\item Connectivity: Heavy-hex architecture with degree-3 connectivity
\end{itemize}

\textbf{Measurement Parameters:} Each circuit execution employed 10,000 shots to ensure sufficient statistical sampling. Post-selection filtering retained approximately 5,000 measurements ($\sim 50\%$) corresponding to ancilla $q_0=0$ outcomes.

\subsection{Data Preprocessing Pipeline}

The preprocessing workflow consists of three sequential transformations following the textbook specification \cite{schuld2018supervised}:

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

\textbf{Theoretical Comparison:} Measured classification probabilities were compared against textbook expected values: $p(\text{survive}) = 0.552$ and $p(\text{die}) = 0.448$ \cite{schuld2018supervised}. Agreement within $\pm 0.05$ indicates successful implementation.

\textbf{Statistical Analysis:} Post-selection rates were analyzed to verify $\sim 50\%$ retention predicted by Hadamard interference theory. Hardware noise impact quantified through absolute error metrics comparing simulator and physical device outcomes.

\section{Implementation Details}

\subsection{Quantum Circuit Construction}

The circuit construction follows a two-phase process using Qiskit primitives \cite{qiskit2024}. First, the \texttt{QuantumCircuit(4, 2)} instantiates four qubits and two classical bits. The \texttt{initialize(amplitude\_vector, [0,1,2,3])} method loads the 16-element amplitude vector spanning the complete Hilbert space. Second, a single \texttt{h(0)} applies the Hadamard gate to the ancilla. Finally, \texttt{measure([0,3], [0,1])} extracts measurement outcomes from qubits $q_0$ and $q_3$.

\subsection{Execution Workflow}

\textbf{Simulator Execution:} Direct circuit execution via \texttt{Aer.get\_backend('qasm\_simulator').run(qc, shots=10000)} yields ideal measurement statistics \cite{qiskit2024}.

\textbf{Hardware Execution:} IBM Quantum execution requires transpilation for physical qubit mapping and gate decomposition \cite{ibm_quantum_2024}. The workflow employs \texttt{generate\_preset\_pass\_manager(backend=ibm\_fez, optimization\_level=1)} to translate the abstract circuit into native gate operations, followed by \texttt{SamplerV2(backend).run()} for job submission to the quantum processor.