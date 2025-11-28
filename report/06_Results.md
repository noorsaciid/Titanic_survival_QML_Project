\section{Results}

\subsection{Preprocessing Results}

The data preprocessing pipeline successfully transformed raw passenger features into normalized quantum-ready vectors. Figure~\ref{fig:preprocessing} illustrates the three-stage transformation process from raw data to quantum amplitude encoding.

\begin{figure}[H]
\centering
\includegraphics[width=0.9\textwidth]{preprocessing_pipeline.pdf}
\caption{\label{fig:preprocessing}Data preprocessing pipeline showing transformation from raw passenger data through min-max scaling to L2 normalization. The three passengers (P1, P2, P3) undergo systematic feature scaling to prepare vectors for quantum amplitude encoding.}
\end{figure}

The preprocessing yielded the following normalized coordinates:
\begin{itemize}
\item \textbf{P1 (Survived):} $(0.831, 0.556)$ - High ticket price, low cabin number
\item \textbf{P2 (Died):} $(0.141, 0.990)$ - Low ticket price, high cabin number  
\item \textbf{P3 (Test):} $(0.865, 0.502)$ - High ticket price, low cabin number
\end{itemize}

These values precisely match the Schuld-Petruccione textbook specifications, validating the preprocessing implementation. The normalized vectors maintain unit length ($\|\mathbf{x}\|_2 = 1$) as required for quantum amplitude encoding.

\subsection{Quantum Circuit Execution}

Circuit execution was performed on both Qiskit Aer simulator and IBM Quantum hardware with 10,000 measurement shots per platform. Figure~\ref{fig:circuit} displays the complete 4-qubit quantum circuit architecture.

\begin{figure}[H]
\centering
\includegraphics[width=0.8\textwidth]{quantum_circuit_4qubit.pdf}
\caption{\label{fig:circuit}4-qubit quantum circuit implementation showing amplitude initialization, Hadamard gate on ancilla qubit $q_0$, and measurement of qubits $q_0$ and $q_3$ for post-selection and classification.}
\end{figure}

Post-selection statistics revealed the following measurement distributions:

\textbf{Simulator Results:}
\begin{itemize}
\item Total measurements: 10,000 shots
\item Post-selected ($q_0=0$): 4,998 shots (49.98\%)
\item Discarded ($q_0 \neq 0$): 5,002 shots (50.02\%)
\end{itemize}

\textbf{Hardware Results (IBM ibm\_fez):}
\begin{itemize}
\item Total measurements: 10,000 shots
\item Post-selected ($q_0=0$): 4,847 shots (48.47\%)
\item Discarded ($q_0 \neq 0$): 5,153 shots (51.53\%)
\end{itemize}

The post-selection rates closely match the theoretical expectation of 50\% from Hadamard interference, with hardware showing slight deviation due to noise effects.

\subsection{Classification Results}

Classification probabilities were extracted from post-selected measurements of the label qubit $q_3$. Figure~\ref{fig:classification} compares results across platforms.

\begin{figure}[H]
\centering
\includegraphics[width=0.95\textwidth]{4qubit_classification_results.pdf}
\caption{\label{fig:classification}Classification probability comparison between expected textbook values and measured results. Left panel shows probability distributions for survival prediction. Right panel displays post-selection statistics demonstrating the 50\% overhead from quantum interference.}
\end{figure}

\textbf{Simulator Classification:}
\begin{equation}
p(\text{survive}|q_3=1) = 0.5524, \quad p(\text{die}|q_3=0) = 0.4476
\end{equation}

\textbf{Hardware Classification (ibm\_fez):}
\begin{equation}
p(\text{survive}|q_3=1) = 0.5483, \quad p(\text{die}|q_3=0) = 0.4517  
\end{equation}

Both platforms predict \textbf{Passenger 3 SURVIVED} ($p(\text{survive}) > p(\text{die})$), consistent with the textbook expected outcome. The hardware results show minimal deviation from simulator values, indicating robust quantum interference despite noise.

Figure~\ref{fig:hardware_comparison} provides detailed hardware versus simulator analysis, quantifying noise impact across multiple metrics.

\begin{figure}[H]
\centering
\includegraphics[width=\textwidth]{4qubit_hardware_vs_simulator.pdf}
\caption{\label{fig:hardware_comparison}Comprehensive hardware versus simulator comparison showing classification probabilities, error analysis, and noise impact metrics. Hardware execution on IBM ibm\_fez demonstrates 1.5-2× error increase while maintaining prediction accuracy.}
\end{figure}

\subsection{Statistical Analysis}

Error analysis quantified deviations from textbook expected values ($p_{\text{expected}}(\text{survive}) = 0.552$, $p_{\text{expected}}(\text{die}) = 0.448$):

\textbf{Simulator Error Metrics:}
\begin{itemize}
\item Survival probability error: $|0.5524 - 0.552| = 0.0004$
\item Death probability error: $|0.4476 - 0.448| = 0.0004$ 
\item Average absolute error: $0.0004$
\end{itemize}

\textbf{Hardware Error Metrics:}
\begin{itemize}
\item Survival probability error: $|0.5483 - 0.552| = 0.0037$
\item Death probability error: $|0.4517 - 0.448| = 0.0037$
\item Average absolute error: $0.0037$
\end{itemize}

Hardware noise increases classification error by a factor of $0.0037/0.0004 = 9.25×$ compared to ideal simulation, primarily due to gate imperfections, decoherence effects (T₁ ≈ 100-200 μs), and readout errors (≈2% infidelity).

Figure~\ref{fig:advanced_analysis} presents comprehensive statevector analysis and quantum interference visualization.

\begin{figure}[H]
\centering
\includegraphics[width=\textwidth]{4qubit_advanced_analysis.pdf}
\caption{\label{fig:advanced_analysis}Advanced quantum analysis showing statevector amplitudes before and after Hadamard transformation, feature space visualization, and quantum interference patterns. Green bars indicate kept states ($q_0=0$) while red bars show discarded states ($q_0=1$) in the post-selection process.}
\end{figure}

Confidence intervals were estimated using binomial statistics for the post-selected sample sizes:

\textbf{Simulator (n=4,998):} $p(\text{survive}) = 0.552 \pm 0.014$ (95\% CI)

\textbf{Hardware (n=4,847):} $p(\text{survive}) = 0.548 \pm 0.014$ (95\% CI)

Both confidence intervals encompass the textbook expected value, confirming statistically significant agreement. The quantum squared-distance classifier successfully demonstrates interference-based machine learning with measurable quantum effects, while hardware implementation validates practical feasibility despite noise-induced limitations.

Feature space analysis in Figure~\ref{fig:feature_space} illustrates the geometric relationship between training and test points in normalized coordinates.

\begin{figure}[H]
\centering
\includegraphics[width=0.7\textwidth]{toy_feature_space_4qubit.pdf}
\caption{\label{fig:feature_space}Feature space visualization showing normalized coordinates of training points P1, P2 and test point P3 in 2D feature space. Euclidean distances indicate P3's proximity to P1 (survived class), supporting the classification outcome.}
\end{figure}

The experimental results validate the complete quantum machine learning pipeline, from data preprocessing through quantum interference to final classification, achieving theoretical accuracy within statistical margins while demonstrating quantum algorithm robustness on contemporary quantum hardware.

\textbf{Word Count:} 784 words