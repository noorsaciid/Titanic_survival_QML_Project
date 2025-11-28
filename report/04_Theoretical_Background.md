\section{Theoretical Background}

\subsection{Quantum State Representation}

Quantum machine learning exploits quantum mechanical principles to represent and process classical data. A quantum system of $n$ qubits exists in a superposition of $2^n$ computational basis states, described by the state vector:

\begin{equation}
|\psi\rangle = \sum_{i=0}^{2^n-1} \alpha_i |i\rangle, \quad \text{where} \quad \sum_{i=0}^{2^n-1} |\alpha_i|^2 = 1
\end{equation}

The complex amplitudes $\alpha_i$ encode information exponentially: $n$ qubits can represent $2^n$ amplitudes simultaneously, providing the foundation for quantum parallelism.

\subsection{Amplitude Encoding}

Classical feature vectors $\mathbf{x} = (x_1, x_2, \ldots, x_d)$ are encoded into quantum amplitudes through normalization. For a normalized vector $\|\mathbf{x}\| = 1$, the quantum state becomes:

\begin{equation}
|\mathbf{x}\rangle = \sum_{i=1}^{d} x_i |i\rangle
\end{equation}

This exponentially compact representation requires only $\lceil \log_2 d \rceil$ qubits to encode $d$ features, contrasting with classical representations requiring $O(d)$ memory.

\subsection{Hadamard Interference}

The Hadamard gate $H$ creates equal superposition, transforming basis states as:

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

For binary classification, the quantum interference mechanism implements a squared-distance classifier. Training exemplars $\mathbf{m}_0$ (class 0) and $\mathbf{m}_1$ (class 1) are encoded with test point $\mathbf{x}$. The measurement probability for predicting class $y$ becomes:

\begin{equation}
p(y|\mathbf{x}) \propto \|\mathbf{m}_y + \mathbf{x}\|^2 = \|\mathbf{m}_y\|^2 + \|\mathbf{x}\|^2 + 2\mathbf{m}_y \cdot \mathbf{x}
\end{equation}

After normalization and algebraic manipulation, this reduces to an exponential form equivalent to classical kernel methods:

\begin{equation}
p(y|\mathbf{x}) = \frac{e^{-c\|\mathbf{x} - \mathbf{m}_y\|^2}}{\sum_{y'} e^{-c\|\mathbf{x} - \mathbf{m}_{y'}\|^2}}
\end{equation}

where $c$ is a constant determined by the encoding scheme. The predicted class maximizes this probability, effectively selecting the nearest training exemplar in feature space.
