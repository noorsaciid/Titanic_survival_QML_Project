# Quantum Computing Course - Comprehensive Study Guide

## Table of Contents
1. [The Birth of Quantum Physics](#the-birth-of-quantum-physics)
2. [The Wave Function](#the-wave-function)
3. [Operators as Matrices](#operators-as-matrices)
4. [The Time Propagator](#the-time-propagator)
5. [Scattering and Tunneling](#scattering-and-tunneling)
6. [Time-Independent Quantum Physics](#time-independent-quantum-physics)
7. [Quantization](#quantization)
8. [The Variational Principle](#the-variational-principle)
9. [Spin, Pauli Matrices, and the Pauli Principle](#spin-pauli-matrices-and-the-pauli-principle)
10. [Entanglement](#entanglement)
11. [Dynamics](#dynamics)
12. [The Adiabatic Theorem](#the-adiabatic-theorem)
13. [Qubits and Quantum Gates](#qubits-and-quantum-gates)
14. [Quantum Key Distribution](#quantum-key-distribution)
15. [Superdense Coding](#superdense-coding)
16. [Quantum Teleportation](#quantum-teleportation)
17. [Quantum Circuits and Algorithms](#quantum-circuits-and-algorithms)
18. [Deutsch-Jozsa Algorithm](#deutsch-jozsa-algorithm)
19. [Simon's Algorithm](#simons-algorithm)
20. [Quantum Algorithms and Their Implications](#quantum-algorithms-and-their-implications)
21. [Adiabatic Quantum Computing](#adiabatic-quantum-computing)
22. [Quantum Annealing](#quantum-annealing)
23. [QAOA and Variational Circuits](#qaoa-and-variational-circuits)

---

## The Birth of Quantum Physics

### Definition
Quantum physics emerged in the early 20th century as a revolutionary framework to explain phenomena that classical physics couldn't account for, such as blackbody radiation, the photoelectric effect, and atomic spectra.

### Key Concepts

#### Planck's Quantum Hypothesis (1900)
**Energy is quantized** in discrete packets (quanta) with E = hν

**Context**: Max Planck solved the "ultraviolet catastrophe" (classical physics predicted infinite energy from hot objects at high frequencies) by proposing that electromagnetic energy can only be emitted or absorbed in discrete chunks.

**Formula**: E = hν where:
- E = energy of one quantum (photon)
- h = Planck's constant = 6.626 × 10⁻³⁴ J·s
- ν = frequency of radiation

This was revolutionary—energy is NOT continuous but comes in packets!

#### Photoelectric Effect (Einstein, 1905)
**Light behaves as particles** (photons) with energy E = hf

**Observation**: When light shines on metal, electrons are ejected, but only if the light frequency is high enough. Increasing intensity doesn't help if frequency is too low.

**Classical prediction**: Higher intensity → more energy → electrons ejected (WRONG!)

**Quantum explanation**: Light consists of photons, each with energy E = hf. An electron needs minimum energy (work function W) to escape. If hf < W, no electrons escape no matter how intense the light.

**Key equation**: KEₘₐₓ = hf - W (kinetic energy of ejected electron)

This proved light has particle properties, earning Einstein the 1921 Nobel Prize.

#### Wave-Particle Duality
**Particles exhibit both wave and particle properties**

**Wave properties of particles**:
- de Broglie wavelength: λ = h/p (momentum p gives wavelength λ)
- Electrons create interference patterns (like waves)
- Diffraction through crystals

**Particle properties of waves**:
- Photons have discrete energy E = hf
- Localized interactions (click in detector)
- Momentum p = h/λ

**Complementarity principle** (Bohr): Wave and particle aspects are complementary—experiments reveal one or the other, never both simultaneously.

#### Uncertainty Principle
**Fundamental limits on simultaneous measurement precision**

Position-momentum: Δx · Δp ≥ ℏ/2
Energy-time: ΔE · Δt ≥ ℏ/2

Not a technological limitation—it's how nature works at quantum scales.

### Example - Photoelectric Effect in Detail

**Experimental setup**:
- Shine light on metal surface (e.g., sodium)
- Measure if/when electrons are ejected
- Vary light frequency and intensity

**Observations**:
1. **Threshold frequency f₀**: Below this frequency, NO electrons ejected (even with very bright light)
2. **Immediate emission**: Electrons ejected instantly when f > f₀ (no delay)
3. **Energy depends on frequency**: Higher frequency → higher electron kinetic energy
4. **Intensity affects quantity not quality**: Brighter light → more electrons, but same energy per electron

**Classical prediction (FAILED)**:
- Any frequency should work if bright enough
- Should be a time delay while electron "absorbs" energy
- Energy should depend on intensity

**Quantum explanation (SUCCESS)**:
- Photon energy: E = hf
- Work function: W = hf₀ (minimum energy to free electron)
- If E > W: electron escapes with KE = hf - W
- If E < W: no effect, regardless of intensity
- One photon → one electron (immediate)

**Numerical example**:
Sodium work function W = 2.3 eV
- Red light (f = 4.5×10¹⁴ Hz): E = hf = 1.9 eV < W → No electrons
- Blue light (f = 7×10¹⁴ Hz): E = hf = 2.9 eV > W → Electrons with KE = 0.6 eV

This demonstrated that light energy comes in discrete packets (photons), which cannot be explained by classical wave theory.

**Sources**: Background from Quantum Computing textbooks, historical physics experiments

---

## The Wave Function

### Definition
The wave function ψ(x,t) is a complex-valued function that contains **all information** about a quantum system. It is the fundamental object in quantum mechanics. The square of its magnitude |ψ(x,t)|² gives the **probability density** for finding a particle at position x at time t.

**Mathematical statement** (from Solutions Manual): The probability of finding a particle between x = a and x = b is:
```
P(a ≤ x ≤ b) = ∫ₐᵇ |Ψ(x)|² dx
```

### Key Concepts

#### 1. Normalization
The particle must be found *somewhere* in space, so:
```
∫₋∞^∞ |ψ(x,t)|² dx = 1
```

**Physical requirement**: For this integral to be finite, the wave function must **fall off toward zero** as |x| becomes large. If Ψ(x) approached a finite value or diverged as x → ±∞, the integral wouldn't be finite.

#### 2. Complex Nature
Wave functions are generally complex-valued:
```
ψ(x,t) = Re[ψ] + i·Im[ψ]
|ψ|² = (Re[ψ])² + (Im[ψ])²
```

**Phase factor invariance**: A constant phase factor doesn't change physical predictions. If ψ and e^(iφ)ψ represent the same physical state since:
```
|e^(iφ)ψ|² = e^(-iφ)e^(iφ)|ψ|² = |ψ|²
```

#### 3. Superposition Principle
A quantum system can exist in a **linear combination** of states simultaneously:
```
|ψ⟩ = α|ψ₁⟩ + β|ψ₂⟩
```
where |α|² + |β|² = 1 gives probabilities for each component.

**Physical meaning**: Before measurement, the system is genuinely in both states. This is not ignorance of which state it's in, but a fundamental quantum feature.

#### 4. Wave Function Collapse
Upon measurement, the wave function **instantaneously collapses** to one of the eigenstates of the measured observable. This collapse is:
- **Probabilistic**: Outcome determined by |⟨eigenstate|ψ⟩|²
- **Irreversible**: The original superposition is destroyed
- **Instantaneous**: Happens at the moment of measurement

#### 5. Time Evolution
The wave function evolves according to the **time-dependent Schrödinger equation**:
```
iℏ ∂ψ/∂t = Ĥψ
```

where:
- i is the imaginary unit
- ℏ = h/2π (reduced Planck's constant)
- Ĥ is the Hamiltonian operator (total energy)

**For time-independent Hamiltonian**, the solution is:
```
ψ(x,t) = ψ(x,0)e^(-iEt/ℏ)
```
where E is the energy eigenvalue.

### Physical Interpretation

**Born's Probability Interpretation**: |ψ(x,t)|² is the probability density. This means:
- High |ψ|²: Particle likely to be found there
- Low |ψ|²: Particle unlikely to be found there
- ψ = 0: Particle cannot be found there

**Position expectation value**:
```
⟨x⟩ = ∫₋∞^∞ x|ψ(x)|² dx
```

**Momentum expectation value**:
```
⟨p⟩ = ∫₋∞^∞ ψ*(x)(-iℏ ∂/∂x)ψ(x) dx
```

### Example - Particle in a Box
For a particle confined between x = 0 and x = L:

**Energy eigenstate**:
```
ψₙ(x) = √(2/L) sin(nπx/L)
```

**Properties**:
- n = 1, 2, 3, ... (quantum number)
- Energies: Eₙ = n²π²ℏ²/(2mL²)
- Zero probability at walls and nodes
- n-1 nodes inside the box

**Time evolution**:
```
ψₙ(x,t) = √(2/L) sin(nπx/L)e^(-iEₙt/ℏ)
```

### Example - Gaussian Wave Packet
A localized particle:
```
ψ(x,0) = (2πσ²)^(-1/4) exp[-(x-x₀)²/(4σ²) + ik₀x]
```

**Features**:
- Centered at x₀
- Width σ (standard deviation)
- Average momentum ℏk₀
- **Spreads over time** due to momentum uncertainty

**Heisenberg uncertainty principle**:
```
σₓ · σₚ ≥ ℏ/2
```

**Physical meaning**: You cannot simultaneously know both the exact position and exact momentum of a particle. The more precisely you know one, the less precisely you can know the other. This is not a limitation of measurement technology—it's a fundamental property of nature.

**Explanation of terms**:
- σₓ = standard deviation of position (how spread out the position measurements are)
- σₚ = standard deviation of momentum  (how spread out the momentum measurements are)
- ℏ = reduced Planck constant (1.055 × 10⁻³⁴ J·s)
- The "≥" means this is a lower bound—you cannot do better than ℏ/2

**Why it exists**: Position and momentum are represented by non-commuting operators: [x̂,p̂] = iℏ. This mathematical non-commutativity directly leads to the uncertainty relation. When operators don't commute, their corresponding observables cannot have simultaneously well-defined values.

**For Gaussian wave packet**: Minimum uncertainty achieved where equality holds: σₓ · σₚ = ℏ/2

**Example**: If you measure an electron's position to within σₓ = 1 nm, then its momentum uncertainty must be at least σₚ ≥ ℏ/(2×10⁻⁹m) ≈ 5×10⁻²⁶ kg·m/s. This momentum uncertainty corresponds to velocity uncertainty of Δv ≈ 50 km/s!

### Computational Representation (Solutions Manual)

**Discretization**: For numerical work, represent ψ(x) on a grid:
```
x₀, x₁, x₂, ..., xₙ with spacing h = (b-a)/n
```

**Vector form**:
```
Ψ = [ψ(x₀), ψ(x₁), ..., ψ(xₙ)]ᵀ
```

**Normalization check**:
```
h·Σᵢ|ψ(xᵢ)|² ≈ 1
```

This converts continuous wave function to finite-dimensional vector for computation.

**Sources**: Solutions Manual (Chapter 1), Quantum Computing for Everyone (Chapter 1-3), Computational Introduction to Quantum Physics

---

## Operators as Matrices

### Definition
In quantum mechanics, **physical observables** (measurable quantities) are represented by **Hermitian operators**, which can be expressed as **matrices** when working in a discrete basis. An operator Ô acts on quantum states to produce new states: Ô|ψ⟩ = |φ⟩.

### Mathematical Properties

#### 1. Hermitian (Self-Adjoint) Operators
An operator Ô is **Hermitian** if Ô = Ô†, where † denotes the conjugate transpose.

**Key properties** (Solutions Manual Exercise 1.5.1-1.5.3):

**Real eigenvalues**:
```
Ô|ψₙ⟩ = λₙ|ψₙ⟩  →  λₙ ∈ ℝ
```
All measurement outcomes (eigenvalues) are real numbers.

**Orthogonal eigenvectors**:
```
⟨ψₘ|ψₙ⟩ = δₘₙ
```
Eigenvectors corresponding to different eigenvalues are orthogonal.

**Completeness**:
```
∑ₙ |ψₙ⟩⟨ψₙ| = Î
```
Eigenvectors form a complete basis (any state can be expanded).

**Proof that eigenvalues are real** (from Solutions Manual):
```
⟨ψ|Ô|ψ⟩ = λ⟨ψ|ψ⟩  (from eigenvalue equation)
⟨ψ|Ô†|ψ⟩ = λ*⟨ψ|ψ⟩  (taking conjugate)

Since Ô = Ô†:
λ⟨ψ|ψ⟩ = λ*⟨ψ|ψ⟩
→ λ = λ*  (since ⟨ψ|ψ⟩ > 0)
→ λ ∈ ℝ
```

#### 2. Matrix Representation

**In discrete basis {|n⟩}**, operator Ô becomes matrix:
```
Ôₙₘ = ⟨n|Ô|m⟩
```

**Action on state** |ψ⟩ = ∑ₙ cₙ|n⟩:
```
Ô|ψ⟩ = ∑ₙₘ cₘÔₙₘ|n⟩
```

**Matrix multiplication**:
```
(Ô|ψ⟩)ₙ = ∑ₘ Ôₙₘψₘ
```

### Common Quantum Operators

#### 1. Position Operator (x̂)

**Continuous basis**:
```
x̂|x'⟩ = x'|x'⟩
```
Eigenvalues: All real numbers x' ∈ ℝ

**Matrix element**:
```
⟨x|x̂|x'⟩ = x'δ(x - x')
```

**Expectation value** (Solutions Manual Exercise 1.5.2):
```
⟨x⟩ = ∫ ψ*(x) · x · ψ(x) dx
```

**Example calculation** for hydrogen atom ground state ψ₁₀₀(r):
```
⟨r⟩ = ∫₀^∞ r · |ψ₁₀₀(r)|² · 4πr² dr
    = ∫₀^∞ r³ · (1/πa₀³)e^(-2r/a₀) · 4π dr
    = 3a₀/2
```
(where a₀ = Bohr radius)

#### 2. Momentum Operator (p̂)

**In position basis**:
```
p̂ = -iℏ ∂/∂x
```

**Matrix element**:
```
⟨x|p̂|ψ⟩ = -iℏ ∂ψ/∂x
```

**Expectation value** (Solutions Manual Exercise 1.5.2):
```
⟨p⟩ = ∫ ψ*(x) · (-iℏ ∂/∂x) · ψ(x) dx
```

**Hermiticity check**:
```
⟨φ|p̂ψ⟩ = ∫ φ* · (-iℏ∂ψ/∂x) dx
        = -iℏ[φ*ψ]^∞_{-∞} + ∫ (iℏ∂φ*/∂x) · ψ dx
        = ⟨p̂φ|ψ⟩  (boundary terms vanish)
```
Therefore p̂† = p̂ (Hermitian).

**Commutator with position**:
```
[x̂, p̂] = x̂p̂ - p̂x̂ = iℏ
```
This is the **canonical commutation relation** - foundation of Heisenberg uncertainty principle.

#### 3. Hamiltonian Operator (Ĥ)

**Total energy operator**:
```
Ĥ = T̂ + V̂ = p̂²/2m + V(x̂)
```

**Time-independent Schrödinger equation**:
```
Ĥ|ψₙ⟩ = Eₙ|ψₙ⟩
```

**Matrix form for particle in box** (from Solutions Manual):
```
Ĥₙₘ = ⟨n|(-ℏ²/2m)∂²/∂x² + V(x)|m⟩
```

**Example** - Hydrogen atom Hamiltonian:
```
Ĥ = -ℏ²/2mₑ ∇² - e²/4πε₀r
```

Eigenvalues: Eₙ = -13.6 eV / n²

#### 4. Pauli Matrices (Spin-½)

**The fundamental operators** for qubits (from Quantum Computing for Everyone):

**σₓ (Pauli-X / NOT gate)**:
```
σₓ = [0  1]
     [1  0]
```
Flips |0⟩ ↔ |1⟩

**σᵧ (Pauli-Y)**:
```
σᵧ = [0  -i]
     [i   0]
```

**σᵨ (Pauli-Z)**:
```
σᵨ = [1   0]
     [0  -1]
```
Phase flip: |1⟩ → -|1⟩

**Properties**:
```
σₓ² = σᵧ² = σᵨ² = I  (involutory)
{σᵢ, σⱼ} = 2δᵢⱼI     (anticommute)
[σᵢ, σⱼ] = 2iεᵢⱼₖσₖ  (commutator relations)
```

**Any 2×2 Hermitian matrix** can be expanded:
```
Ô = a₀I + a₁σₓ + a₂σᵧ + a₃σᵨ
```
This forms a complete basis for qubit operators.

### Spectral Decomposition

**Any Hermitian operator** can be written:
```
Ô = ∑ₙ λₙ|ψₙ⟩⟨ψₙ|
```

This is the **spectral theorem**.

**Example** - Pauli-Z decomposition:
```
σᵨ = 1·|0⟩⟨0| + (-1)·|1⟩⟨1|
   = |0⟩⟨0| - |1⟩⟨1|
```

Eigenvalues: +1 (for |0⟩), -1 (for |1⟩)

**Measurement interpretation**:
Measuring σᵨ on state |ψ⟩ = α|0⟩ + β|1⟩:
- Result +1 with probability |α|²
- Result -1 with probability |β|²
- State collapses to |0⟩ or |1⟩

### Expectation Values

**General formula** (Solutions Manual):
```
⟨Ô⟩ = ⟨ψ|Ô|ψ⟩ = ∑ₙ |cₙ|²λₙ
```

where |ψ⟩ = ∑ₙ cₙ|ψₙ⟩ (expansion in eigenbasis).

**Physical interpretation**: Average of many measurements on identically prepared systems.

**Example** - Energy measurement:
```
⟨Ĥ⟩ = ∫ ψ*(x)Ĥψ(x) dx
```

For stationary state |ψₙ⟩:
```
⟨Ĥ⟩ = Eₙ  (definite energy)
```

For superposition |ψ⟩ = (|ψ₁⟩ + |ψ₂⟩)/√2:
```
⟨Ĥ⟩ = (E₁ + E₂)/2  (average energy)
```

### Uncertainty Principle (Solutions Manual Exercise 1.5.4)

**General uncertainty relation** for operators Â and B̂:
```
ΔA · ΔB ≥ ½|⟨[Â,B̂]⟩|
```

where ΔA = √(⟨Â²⟩ - ⟨Â⟩²) is standard deviation.

**Position-momentum uncertainty**:
```
Δx · Δp ≥ ℏ/2
```

**Derivation outline**:
1. Define ΔÂ = Â - ⟨Â⟩
2. Use Cauchy-Schwarz inequality
3. Apply [x̂,p̂] = iℏ

**Example verification** - Gaussian wave packet:
```
ψ(x) = (1/πσ²)^(1/4) exp(-x²/2σ²)

Δx = σ/√2
Δp = ℏ/σ√2

→ Δx·Δp = ℏ/2  (minimum uncertainty)
```

### Computational Implementation

**Matrix operations in Python** (from Solutions Manual computational guidance):

```python
import numpy as np

# Define Pauli matrices
sigma_x = np.array([[0, 1], [1, 0]])
sigma_y = np.array([[0, -1j], [1j, 0]])
sigma_z = np.array([[1, 0], [0, -1]])

# Verify Hermitian property
assert np.allclose(sigma_x, sigma_x.conj().T)

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eigh(sigma_z)
# Returns: eigenvalues = [-1, 1]
#          eigenvectors[:,0] = |1⟩, eigenvectors[:,1] = |0⟩

# Calculate expectation value
psi = np.array([1, 1])/np.sqrt(2)  # |+⟩ state
expectation = psi.conj().T @ sigma_z @ psi
# Returns: 0 (equal superposition)
```

### Connection to Quantum Gates

**Unitary operators**: Evolution operators must preserve normalization.
```
Û†Û = I
```

**Relation to Hermitian operators** (from QC for Everyone):
```
Û = e^(-iÔt/ℏ)
```

Any unitary can be generated from Hermitian operator.

**Example gates**:
- X gate = exp(-iπσₓ/2)
- Z gate = exp(-iπσᵨ/2)  
- Hadamard = exp(-iπ(σₓ+σᵨ)/(2√2))

**Sources**: Solutions Manual Exercises 1.5.1-1.5.4, Quantum Computing for Everyone

---

σᵧ = -i|0⟩⟨1| + i|1⟩⟨0| = [0 -i]
                            [i  0]

σᵧ = |0⟩⟨0| - |1⟩⟨1| = [1  0]
                         [0 -1]
```

**Sources**: Lecture notes, Quantum Computing textbooks

---

## The Time Propagator

### Definition
The time propagator (or time evolution operator) U(t,t₀) describes how a quantum state evolves from time t₀ to time t. For time-independent Hamiltonians:

```
U(t,t₀) = e^(-iH(t-t₀)/ℏ)
```

### Key Concepts

#### Unitarity: U†U = I
**Physical requirement**: Time evolution must preserve probability (normalization of wave function).

**Mathematical statement**: The time propagator U is a **unitary operator**, meaning:
```
U†U = UU† = I
```

**Consequence**: If |ψ(t₀)⟩ is normalized, then |ψ(t)⟩ = U|ψ(t₀)⟩ is also normalized:
```
⟨ψ(t)|ψ(t)⟩ = ⟨ψ(t₀)|U†U|ψ(t₀)⟩ = ⟨ψ(t₀)|ψ(t₀)⟩ = 1
```

**Physical meaning**: Total probability is conserved—the particle doesn't disappear or duplicate.

#### Time Evolution: |ψ(t)⟩ = U(t,t₀)|ψ(t₀)⟩
**How states change in time**: Given initial state |ψ(t₀)⟩, the state at later time t is obtained by applying the time propagator.

**For time-independent Hamiltonian**:
```
U(t,t₀) = e^(-iĤ(t-t₀)/ℏ)
```

**Exponential of operator** defined by Taylor series:
```
e^(-iĤt/ℏ) = I - (iĤt/ℏ) + (iĤt/ℏ)²/2! - (iĤt/ℏ)³/3! + ...
```

**Properties**:
- U(t₀,t₀) = I (identity at initial time)
- U(t₂,t₀) = U(t₂,t₁)U(t₁,t₀) (composition property)
- U⁻¹(t,t₀) = U(t₀,t) (reversible evolution)

#### Time-Ordering Operator 𝒯
**Problem**: For time-dependent Hamiltonians Ĥ(t), exponential formula doesn't work directly because Ĥ(t₁) and Ĥ(t₂) at different times don't commute.

**Solution**: Time-ordering operator 𝒯 arranges operators in chronological order:
```
U(t,t₀) = 𝒯 exp[-i/ℏ ∫ₜ₀ᵗ Ĥ(t')dt']
```

**What 𝒯 does**: In any product of operators at different times, 𝒯 puts latest time on the left:
```
𝒯[Ĥ(t₁)Ĥ(t₂)] = { Ĥ(t₁)Ĥ(t₂)  if t₁ > t₂
                  { Ĥ(t₂)Ĥ(t₁)  if t₂ > t₁
```

**Physical meaning**: Evolution respects causality—later events come after earlier ones.

#### Trotter Formula (Approximation)
**Problem**: If Hamiltonian has multiple non-commuting parts (e.g., Ĥ = Â + B̂ with [Â,B̂] ≠ 0), then:
```
e^(Â+B̂) ≠ e^Â e^B̂  (in general)
```

**Trotter formula**: For small time steps Δt:
```
e^(-i(Â+B̂)Δt/ℏ) ≈ e^(-iÂΔt/ℏ) e^(-iB̂Δt/ℏ) + O((Δt)²)
```

**Application**: Split evolution into many small steps:
```
U(t) ≈ [e^(-iÂΔt/ℏ) e^(-iB̂Δt/ℏ)]^(t/Δt)
```

**Use in quantum computing**: Digital quantum simulation—decompose complex evolution into sequence of simple gates.

**Error**: Goes to zero as Δt → 0 (more steps = more accurate).

### Example - Qubit Rotation
For a two-level system (qubit) with Hamiltonian H = ωσᵧ/2:
```
U(t) = e^(-iωtσᵧ/2) = cos(ωt/2)I - i sin(ωt/2)σᵧ
```

**Derivation using Pauli matrix properties**:
Since σᵧ² = I:
```
e^(-iωtσᵧ/2) = Σₙ (-iωtσᵧ/2)ⁿ/n!
             = [1 - (ωt/2)²/2! + ...] I + [-iωt/2 + (iωt/2)³/3! - ...] σᵧ
             = cos(ωt/2)I - i sin(ωt/2)σᵧ
```

**Physical interpretation**: This describes **rotation about the z-axis** in the Bloch sphere.

**What happens to states**:
- Initial state |0⟩ evolves to: cos(ωt/2)|0⟩ - i sin(ωt/2)|1⟩
- Initial state |1⟩ evolves to: -i sin(ωt/2)|0⟩ + cos(ωt/2)|1⟩

**Bloch sphere picture**: The state vector rotates around the z-axis with angular frequency ω.

**At special times**:
- t = 0: U = I (no change)
- t = π/ω: U = -iσᵧ (X gate, bit flip)
- t = 2π/ω: U = -I (full rotation, global phase)

**Application**: This is how quantum gates are implemented physically—apply Hamiltonian for specific time to get desired rotation.

**Sources**: Quantum Computing textbooks, QAOA lecture notes

---

## Scattering and Tunneling

### Definition
**Scattering** describes how quantum particles interact with potentials and change their trajectory or transmission properties. **Tunneling** is the uniquely quantum phenomenon where particles can penetrate through potential barriers that would be classically forbidden (regions where E < V).

### Mathematical Framework

#### Rectangular Potential Well (Solutions Manual Exercise 3.1.1)

**Potential**:
```
V(x) = { -V₀   for |x| ≤ w/2
         0     for |x| > w/2
```

**General solution** for energy ε < 0 (bound states):

**Region I** (x < -w/2):
```
ψ(x) = Be^(+κx)  where κ = √(-2mε)/ℏ
```

**Region II** (|x| ≤ w/2):
```
ψ(x) = C cos(kx) + D sin(kx)  where k = √(2m(ε+V₀))/ℏ
```

**Region III** (x > w/2):
```
ψ(x) = Be^(-κx)
```

**Key constraint**: Wave function must be normalizable → exponentially growing parts excluded.

#### Symmetric vs Anti-symmetric Solutions

**Symmetric** states ψₛ(-x) = ψₛ(x):
```
ψₛ(x) = { Be^(κx)     for x < -w/2
          C cos(kx)   for |x| ≤ w/2
          Be^(-κx)    for x > w/2
```

**Continuity conditions** at x = w/2:
```
C cos(kw/2) = Be^(-κw/2)
-Ck sin(kw/2) = -Bκe^(-κw/2)
```

**Energy quantization condition**:
```
κ cos(kw/2) = k sin(kw/2)
```

**Anti-symmetric** states ψₐ(-x) = -ψₐ(x):
```
ψₐ(x) = { Be^(κx)     for x < -w/2
          D sin(kx)   for |x| ≤ w/2
          -Be^(-κx)   for x > w/2
```

**Energy quantization condition**:
```
κ sin(kw/2) = -k cos(kw/2)
```

### Quantum Tunneling

#### Physical Mechanism
**Classical forbidden region**: Where particle energy E < potential V(x).
- Classically: Particle reflects 100%
- Quantum mechanically: Particle can "tunnel" through

**Wave function behavior in barrier**:
```
ψ(x) ∝ e^(-κx)  where κ = √(2m(V-E))/ℏ
```

Exponential decay, not oscillatory (unlike classical allowed region).

#### Transmission Coefficient

**For rectangular barrier** of height V₀ and width a:

**Low energy** (E << V₀):
```
T ≈ e^(-2κa)  where κ = √(2m(V₀-E))/ℏ
```

**Exact formula** (including oscillations):
```
T = [1 + (V₀² sinh²(κa))/(4E(V₀-E))]^(-1)
```

**Key dependencies**:
1. **Barrier width**: T ∝ e^(-2κa) → exponentially decreases with width
2. **Barrier height**: κ ∝ √(V₀-E) → higher barriers suppress tunneling
3. **Particle mass**: κ ∝ √m → heavier particles tunnel less

#### Example Calculation (Solutions Manual style)

**Given**: Barrier V₀ = 4 eV, width w = 5 Å, particle with E = -3.85 eV (bound state)

**Step 1**: Calculate κ and k
```
κ = √(2m|E|)/ℏ ≈ 3.17 Å⁻¹
k = √(2m(E+V₀))/ℏ ≈ 0.73 Å⁻¹
```

**Step 2**: Check quantization condition
```
κ cos(kw/2) ≈ k sin(kw/2)
3.17 cos(1.83) ≈ 0.73 sin(1.83)
```

**Step 3**: Number of bound states
Determined by roots of quantization equation. For V₀ = 4, w = 5:
- 3 symmetric states
- 2 anti-symmetric states
- Total: **5 bound states**

### Computational Approach (Exercise 3.1.2)

**Matrix diagonalization method**:

1. **Discretize space**: x₁, x₂, ..., xₙ with spacing h
2. **Construct Hamiltonian matrix**:
```
Hᵢⱼ = (-ℏ²/2m) · (δᵢ,ⱼ₊₁ - 2δᵢⱼ + δᵢ,ⱼ₋₁)/h² + V(xᵢ)δᵢⱼ
```
3. **Diagonalize**: Find eigenvalues (energies) and eigenvectors (wave functions)

**Normalization**: Numerical eigenvectors need adjustment:
```
ψ_numerical → ψ_normalized/√h
```

**Smoothed potential** for numerical stability:
```
V(x) = -V₀/2 · [1 + tanh(s(x+w/2))] · [1 - tanh(s(x-w/2))]
```
Parameter s controls smoothness (s=100 ≈ sharp corners).

### Node Theorem

**Number of nodes** (zeros) in eigenfunction = energy level index - 1

For rectangular well:
- Ground state (n=0): 0 nodes
- First excited (n=1): 1 node  
- Second excited (n=2): 2 nodes

This is the **"quantum guitar" analogy** - higher energy modes have more nodes, like higher harmonics on a string.

### Reflection and Transmission

**Conservation law**:
```
T + R = 1
```
where:
- T = transmission coefficient (probability of transmission)
- R = reflection coefficient (probability of reflection)

**Current conservation** (from continuity equation):
```
j_incident = j_transmitted + j_reflected
```

**Probability current**:
```
j(x) = (ℏ/2mi)[ψ*(∂ψ/∂x) - (∂ψ*/∂x)ψ]
```

### Resonant Tunneling

**Special case**: When barrier contains a quantum well.

**Resonance condition**: E ≈ Eₙ (discrete energy level inside well)
- Transmission dramatically enhanced
- Can reach T ≈ 1 (perfect transmission!)

**Physical picture**: Particle resonantly couples to quasi-bound state inside well.

**Application**: Resonant tunneling diodes (RTD)

### Physical Applications

#### 1. Scanning Tunneling Microscope (STM)
- **Principle**: Tunneling current exponentially sensitive to tip-sample distance
- **Resolution**: Atomic scale imaging
- **Current**: I ∝ e^(-2κd) where d = tip-sample gap

#### 2. Alpha Decay
**Gamow model**: Alpha particle trapped in nucleus by potential barrier.
- **Decay rate**: Γ ∝ e^(-2κa) 
- **Lifetime**: τ = ℏ/Γ
- Explains huge variation in decay rates (10⁻⁶ to 10¹⁷ years!)

#### 3. Quantum Dots
- Electrons confined in 3D "artificial atoms"
- Tunnel coupling controls charging energy
- Applications: Single-electron transistors, qubits

#### 4. Field Emission
- Electrons tunnel through surface potential barrier
- Applied electric field reduces barrier
- **Fowler-Nordheim equation**: Current exponential in field

### Comparison: Classical vs Quantum

**Particle approaching barrier** (E < V₀):

**Classical prediction**:
```
P_transmission = 0  (complete reflection)
```

**Quantum prediction**:
```
P_transmission = T > 0  (some tunneling)
```

**Experimental verification**: 
- Photoemission from metals
- Alpha decay lifetimes
- STM imaging
- All confirm quantum tunneling!

### Example Problem

**Question**: Electron with E = 2 eV encounters barrier V₀ = 4 eV, width a = 1 nm. Calculate transmission probability.

**Solution**:
```
κ = √(2mₑ(V₀-E))/ℏ
  = √(2 × 9.11×10⁻³¹ kg × 2 eV × 1.6×10⁻¹⁹ J/eV) / (1.055×10⁻³⁴ J·s)
  ≈ 7.26 × 10⁹ m⁻¹

T ≈ e^(-2κa) 
  = e^(-2 × 7.26×10⁹ × 10⁻⁹)
  ≈ e^(-14.5)
  ≈ 5 × 10⁻⁷
```

**Result**: About 1 in 2 million particles tunnel through.

**Sources**: Solutions Manual Chapter 3 (Exercises 3.1.1-3.1.3), Computational Introduction to Quantum Physics

---

## Time-Independent Quantum Physics

### Definition
Time-independent quantum physics deals with systems where the Hamiltonian does not explicitly depend on time, leading to stationary states with definite energies.

### Key Concepts

#### Time-Independent Schrödinger Equation: Ĥψ = Eψ
**Eigenvalue equation** for energy. When the Hamiltonian Ĥ doesn't depend explicitly on time, we can separate variables and get this simpler equation.

**Full form**:
```
-ℏ²/(2m) d²ψ/dx² + V(x)ψ = Eψ
```

**What it means**: Find functions ψ(x) and values E such that applying the energy operator gives back the same function times a constant (the energy).

**Solutions**: Give us all possible energy levels and their corresponding wave functions.

#### Stationary States: |ψ(t)⟩ = e^(-iEt/ℏ)|ψ(0)⟩
**Definition**: States whose probability distribution |ψ|² does NOT change with time.

**Why "stationary"**: The time dependence is just a phase factor e^(-iEt/ℏ). When you calculate probability |ψ(x,t)|², the time-dependent phases cancel:
```
|ψ(x,t)|² = |ψ(x)|²|e^(-iEt/ℏ)|² = |ψ(x)|²
```

**Physical meaning**: The system is in equilibrium—measurements give the same statistics at all times. The particle isn't "stationary" (not moving), but its probability distribution is stationary (unchanging).

#### Energy Eigenstates: Form a complete basis
**Completeness**: The set of all energy eigenstates {|ψₙ⟩} spans the entire Hilbert space. ANY quantum state can be written as:
```
|ψ⟩ = Σₙ cₙ|ψₙ⟩
```

**Orthonormality**: ⟨ψₘ|ψₙ⟩ = δₘₙ (different energy states are orthogonal)

**Time evolution**: If you know coefficients cₙ at t=0, evolution is simple:
```
|ψ(t)⟩ = Σₙ cₙe^(-iEₙt/ℏ)|ψₙ⟩
```

Each energy eigenstate just picks up its own phase factor!

#### Bound States: Discrete energy spectrum (E < 0)
**Definition**: Particle is confined to finite region—cannot escape to infinity.

**Characteristics**:
- Negative total energy (by convention, with V→0 as x→∞)
- Wave function goes to zero at infinity (normalizable)
- **Discrete** energy values: E₁, E₂, E₃, ... (quantized!)
- Labeled by quantum numbers: n, l, m, ...

**Examples**:
- Electron in atom
- Particle in potential well
- Molecular vibrations

**Why discrete**: Boundary conditions (ψ→0 at infinity) only allow specific wavelengths, like standing waves on a string.

#### Continuum States: Continuous energy spectrum (E > 0)
**Definition**: Particle has enough energy to escape—not bound.

**Characteristics**:
- Positive total energy (E > 0)
- Wave function extends to infinity (not normalizable in standard sense)
- **Continuous** range of energies (any E > 0 allowed)
- Describes scattering, free particles

**Examples**:
- Free electron
- Scattering from potential
- Ionization (electron escaping atom)

**Normalization**: Use δ-function normalization: ⟨ψₖ|ψₖ'⟩ = δ(k-k')

### Example
Harmonic oscillator energy levels:
```
Eₙ = ℏω(n + 1/2), n = 0, 1, 2, ...
```

**Sources**: Computational Introduction to Quantum Physics

---

## Quantization

### Definition
Quantization is the process of transitioning from a classical system to a quantum system, where continuous variables become discrete and observables become operators.

### Key Concepts

#### Canonical Quantization: From Classical to Quantum
**The recipe** for turning classical mechanics into quantum mechanics:

**Step 1**: Start with classical observables (position x, momentum p)

**Step 2**: Promote them to operators with "hats":
- Position: x → x̂ (multiplication operator)
- Momentum: p → p̂ = -iℏ∂/∂x (differential operator)

**Step 3**: Replace Poisson brackets with commutators:
```
Classical: {x, p} = ∂x/∂x · ∂p/∂p - ∂x/∂p · ∂p/∂x = 1
Quantum:   [x̂, p̂] = x̂p̂ - p̂x̂ = iℏ
```

**The factor iℏ**: Bridges classical and quantum worlds. As ℏ→0, quantum mechanics reduces to classical.

**Step 4**: Classical Hamiltonian H(x,p) → Quantum Hamiltonian Ĥ(x̂,p̂):
```
Classical: H = p²/(2m) + V(x)
Quantum:   Ĥ = p̂²/(2m) + V(x̂) = -ℏ²/(2m)∂²/∂x² + V(x)
```

**Why it works**: Preserves fundamental structure (symplectic geometry → Hilbert space structure)

**Ordering ambiguity**: In classical mechanics xp = px, but in quantum mechanics x̂p̂ ≠ p̂x̂. For products like xp, we typically symmetrize: (x̂p̂ + p̂x̂)/2.

#### Energy Quantization: Discrete Energy Levels
**Why energy is quantized in bound systems**:

1. **Boundary conditions**: ψ must vanish at walls or infinity
2. **Wave equation**: Like standing waves—only certain patterns fit
3. **Mathematical result**: Eigenvalue equation has discrete solutions

**General pattern**:
```
Eₙ ~ n² for "boxes" (particle in box)
Eₙ ~ n for harmonic oscillators
Eₙ ~ 1/n² for Coulomb potentials (atoms)
```

**Physical consequences**:
- Atomic emission spectra (discrete wavelengths)
- Stability of matter (can't continuously radiate)
- Periodic table structure
- Molecular vibration modes

**Example - Particle in 1D box** (length L):
```
ψₙ(x) = √(2/L) sin(nπx/L)
Eₙ = n²π²ℏ²/(2mL²)  with n = 1,2,3,...
```
The "1" in the ground state (n=1) prevents E=0—quantum systems have **zero-point energy**.

#### Angular Momentum Quantization
**Key equations**:
```
L̂² |l,m⟩ = ℏ²l(l+1) |l,m⟩  (magnitude squared)
L̂ᵧ |l,m⟩ = ℏm |l,m⟩         (z-component)
```

**Quantum numbers**:
- **l** = 0, 1, 2, 3, ... (orbital angular momentum quantum number)
  - l = 0: s orbital (spherical)
  - l = 1: p orbital (dumbbell)
  - l = 2: d orbital (cloverleaf)
  - l = 3: f orbital (complex)

- **m** = -l, -l+1, ..., l-1, l (magnetic quantum number)
  - 2l+1 possible values
  - Different orientations of angular momentum

**Key insight**: You can know the magnitude |L| and one component (usually Lᵧ) precisely, but NOT all three components simultaneously because [L̂ₓ, L̂ᵧ] = iℏL̂ᵨ ≠ 0.

**Classical vs Quantum**:
- **Classical**: Angular momentum vector L⃗ has definite direction
- **Quantum**: Cannot specify all three components—only magnitude and one component

**Physical picture**: Angular momentum vector precesses around z-axis—only its z-component and magnitude are well-defined.

### Example
Bohr's model of hydrogen atom:
```
Eₙ = -13.6 eV/n², n = 1, 2, 3, ...
```

**Sources**: Computational Introduction to Quantum Physics

---

## The Variational Principle

### Definition
The variational principle states that for any trial wave function |ψ⟩, the expectation value of the Hamiltonian provides an upper bound to the ground state energy:

```
E₀ ≤ ⟨ψ|Ĥ|ψ⟩/⟨ψ|ψ⟩
```

### Key Concepts

#### Ground State Optimization: Find |ψ⟩ that minimizes ⟨Ĥ⟩
**Goal**: Find the wave function that gives the lowest possible energy.

**Why it works**: The variational principle guarantees that any trial function gives energy ≥ true ground state energy. So by minimizing ⟨Ĥ⟩, we approach the true ground state.

**Procedure**:
1. Choose a family of trial functions |ψ(α₁, α₂, ...)⟩ with adjustable parameters
2. Calculate energy functional: E(α₁, α₂, ...) = ⟨ψ|Ĥ|ψ⟩/⟨ψ|ψ⟩
3. Find parameters that minimize E
4. Result approximates ground state

**Quality of approximation**: Depends on how flexible your trial function family is. More parameters → better approximation (but harder to optimize).

#### Variational Parameters: Optimize parameters in parametrized trial functions
**Trial functions** typically have adjustable parameters, like:

**Example 1 - Gaussian for harmonic oscillator**:
```
ψ(x; α) = (α/π)^(1/4) e^(-αx²/2)
```
Optimize width parameter α.

**Example 2 - Linear combination**:
```
|ψ(c₁, c₂, ...)⟩ = c₁|φ₁⟩ + c₂|φ₂⟩ + ... + cₙ|φₙ⟩
```
Optimize coefficients cᵢ (this is the Rayleigh-Ritz method).

**Example 3 - Quantum circuit** (VQE):
```
|ψ(θ)⟩ = U(θ)|0⟩
```
where U(θ) is parametrized quantum circuit, optimize angles θ.

**Optimization methods**:
- Analytical (calculus): ∂E/∂αᵢ = 0
- Numerical: Gradient descent, BFGS, Nelder-Mead
- Quantum-classical hybrid: VQE uses classical optimizer + quantum measurements

#### Rayleigh-Ritz Method: Systematic variational approach
**Specific implementation** of variational principle using basis expansion.

**Setup**: Choose orthonormal basis {|φ₁⟩, |φ₂⟩, ..., |φₙ⟩}

**Ansatz**: 
```
|ψ⟩ = Σᵢ cᵢ|φᵢ⟩
```

**Matrix formulation**: Define Hamiltonian matrix:
```
Hᵢⱼ = ⟨φᵢ|Ĥ|φⱼ⟩
```

**Variational problem becomes**: Find eigenvectors of H matrix
```
Minimize: E = Σᵢⱼ cᵢ*Hᵢⱼcⱼ / Σᵢ|cᵢ|²
```

**Solution**: Solve eigenvalue problem HC = EC
- Lowest eigenvalue = best approximation to ground state energy
- Higher eigenvalues approximate excited states

**Advantage**: Reduces quantum problem to linear algebra (matrix diagonalization).

#### Applications
1. **Quantum Chemistry**: 
   - Molecular orbital theory (LCAO method)
   - Electronic structure calculations
   - Hartree-Fock method

2. **Many-Body Physics**:
   - Mean-field theories
   - Density functional theory (DFT)
   - Variational Monte Carlo

3. **QAOA** (Quantum Approximate Optimization Algorithm):
   - Parametrized quantum circuits
   - Optimize expectation value of problem Hamiltonian
   - Hybrid quantum-classical algorithm

4. **Machine Learning**:
   - Variational quantum algorithms for ML
   - Quantum neural networks
   - Parameter optimization in quantum models

### Example - Variational Quantum Eigensolver (VQE)
**Goal**: Find ground state energy of molecule/system using quantum computer.

**Why VQE**: Exact diagonalization impossible for large systems (Hilbert space grows exponentially). VQE provides approximate solution with fewer quantum resources.

**Algorithm Steps**:

1. **Prepare parametrized state** |ψ(θ)⟩ on quantum computer
   ```
   |ψ(θ)⟩ = U(θ)|0...0⟩
   ```
   where U(θ) is a parametrized quantum circuit (ansatz)
   
   **Common ansatzes**:
   - **Hardware-efficient**: Use native gates of quantum computer
   - **Chemistry-inspired**: Unitary Coupled Cluster (UCC)
   - **Layered**: Alternating layers of rotation and entanglement gates

2. **Measure energy** ⟨ψ(θ)|Ĥ|ψ(θ)⟩
   
   **Hamiltonian decomposition**: Express Ĥ as sum of Pauli strings:
   ```
   Ĥ = Σᵢ αᵢ Pᵢ   where Pᵢ are products of Pauli operators
   ```
   
   **Energy estimation**:
   ```
   ⟨Ĥ⟩ = Σᵢ αᵢ⟨Pᵢ⟩   (measure each Pauli term separately)
   ```
   
   Each ⟨Pᵢ⟩ requires:
   - Prepare |ψ(θ)⟩
   - Rotate to appropriate measurement basis
   - Measure qubits many times
   - Compute average

3. **Classical optimizer adjusts θ** to minimize energy
   
   **Optimization methods**:
   - **Gradient-free**: COBYLA, Nelder-Mead, Powell (good for noisy quantum hardware)
   - **Gradient-based**: Parameter-shift rule for gradients, BFGS (when gradients available)
   - **Adaptive**: Rotosolve, SPSA (Simultaneous Perturbation Stochastic Approximation)
   
   **Update rule** (example - gradient descent):
   ```
   θₙₑw = θₒₗd - η ∇θ⟨Ĥ⟩
   ```
   where η is learning rate

4. **Repeat until convergence**
   
   **Convergence criteria**:
   - Energy change < ε: |E(θₙ) - E(θₙ₋₁)| < 10⁻⁶
   - Gradient norm small: ||∇θE|| < 10⁻⁴
   - Max iterations reached
   
   **Typical run**: 100-1000 iterations depending on problem size

**Output**: 
- Approximation to ground state energy: E₀ ≈ ⟨ψ(θ*)|Ĥ|ψ(θ*)⟩
- Approximation to ground state: |ψ₀⟩ ≈ |ψ(θ*)⟩

**Advantages of VQE**:
- **NISQ-friendly**: Tolerant of noise (variational bound still valid)
- **Shallow circuits**: Can use circuits within current hardware capabilities
- **Hybrid**: Leverages both quantum (state preparation + measurement) and classical (optimization)

**Challenges**:
- **Barren plateaus**: Gradients vanish exponentially in some landscapes
- **Local minima**: Optimization can get stuck
- **Measurement cost**: Many measurements needed for accurate energy
- **Ansatz selection**: Need good initial guess for circuit structure

**Example application - H₂ molecule**:
```
Hamiltonian (2 qubits):
Ĥ = -1.05·I + 0.39·Z₀ - 0.39·Z₁ - 0.01·Z₀Z₁ + 0.18·X₀X₁

Ansatz (single layer):
|ψ(θ)⟩ = e^(-iθ₁X₀X₁) Rᵧ(θ₂)|0⟩₀ Rᵧ(θ₃)|0⟩₁

Result: E₀ ≈ -1.86 Hartree (chemical accuracy!)
```

**Sources**: QAOA lecture notes, variational quantum algorithms, quantum chemistry literature

---

## Spin, Pauli Matrices, and the Pauli Principle

### Definition
**Spin** is an intrinsic form of angular momentum carried by elementary particles—a purely quantum mechanical property with no classical analog. For spin-1/2 particles (electrons, qubits), spin is mathematically described using **Pauli matrices**. Unlike orbital angular momentum, spin does not correspond to actual physical rotation.

### Historical Foundation: Stern-Gerlach Experiment (1922)

**Setup** (from Quantum Computing for Everyone, Chapter 1):
- Silver atoms sent through non-uniform magnetic field
- Vee-shaped magnets create stronger force from south magnet
- Atoms deflect based on magnetic moment orientation

**Classical prediction**: Continuous distribution (atoms can have any orientation)
**Quantum result**: **Only two dots** on detector screen
- Maximum upward deflection
- Maximum downward deflection  
- **NO intermediate values**

**Interpretation**: Magnetic moment (and hence spin) is **quantized** - can only be in discrete orientations.

### Electron Spin Measurements

**Key insight**: Electron behaves as **tiny magnet** with two possible alignments in any chosen direction.

**Notation** (from QC for Everyone):
- **N** = North pole in specified direction  
- **S** = South pole in specified direction
- **θ°** = angle from vertical (clockwise)

**Examples**:
```
Spin N at 0°:   North pointing up
Spin S at 0°:   South pointing up (= North pointing down)
Spin N at 90°:  North pointing right
Spin S at 90°:  South pointing right (= North pointing left)
```

**Measurement outcome**: Always one of two opposite alignments along measurement axis.

### Pauli Matrices

**The three Pauli matrices** are fundamental operators for spin-1/2:

**σₓ (Pauli-X / NOT gate)**:
```
σₓ = [0  1]
     [1  0]
```

**σᵧ (Pauli-Y)**:
```
σᵧ = [0  -i]
     [i   0]
```

**σᵨ (Pauli-Z)**:
```
σᵨ = [1   0]
     [0  -1]
```

### Properties of Pauli Matrices

**Involutory** (self-inverse):
```
σₓ² = σᵧ² = σᵨ² = I
```

**Eigenvalues**: All have eigenvalues **±1**
```
σᵨ|0⟩ = +1|0⟩  (spin up)
σᵨ|1⟩ = -1|1⟩  (spin down)
```

**Anticommutation**:
```
{σᵢ, σⱼ} = σᵢσⱼ + σⱼσᵢ = 2δᵢⱼI
```

**Commutation relations**:
```
[σₓ, σᵧ] = 2iσᵨ
[σᵧ, σᵨ] = 2iσₓ
[σᵨ, σₓ] = 2iσᵧ
```

Compact form:
```
[σᵢ, σⱼ] = 2iεᵢⱼₖσₖ
```
where εᵢⱼₖ is the Levi-Civita symbol.

**Completeness**: Any 2×2 Hermitian matrix can be expanded:
```
Ĥ = a₀I + a₁σₓ + a₂σᵧ + a₃σᵨ
```

### Quantum Clock Analogy (QC for Everyone)

**Imagine**: Clock face, but you can't see it—you can only ask questions.

**Allowed question**: "Is the hand pointing at hour X?"

**Classical clock answer**: Usually "no" (hand rarely exactly on hour)

**Quantum clock answer**: Either:
- "Yes, pointing at X"
- "No, pointing at opposite direction (X ± 6 hours)"

**No other answers possible!**

**Example**:
- Ask: "Pointing at 12?" → Answer: "Yes" or "Pointing at 6"
- Ask: "Pointing at 3?" → Answer: "Yes" or "Pointing at 9"

This perfectly models electron spin measurement!

### Sequential Measurements (Critical Observations)

#### 1. Same Direction → Same Result
**Experiment**: Measure spin at 0°, then measure again at 0°

**Result**: **Always identical outcome**
- If first measurement gives N → second gives N
- If first measurement gives S → second gives S

**Interpretation**: Measurement produces **definite state** (eigenstate).

**For quantum clock**: Ask "Pointing at 12?" twice → get same answer both times.

#### 2. Perpendicular Directions → Random Result
**Experiment**: Measure spin at 0°, then measure at 90°

**Result**: **50% N, 50% S** (completely random)
- First result gives **no information** about second
- Sequence unpredictable

**For quantum clock**: Ask "Pointing at 12?" then "Pointing at 3?" → Second answer is random (50% at 3, 50% at 9).

#### 3. Measurement Erases Previous Information
**Experiment**: Measure at 0° → measure at 90° → measure at 0° again

**Example sequence**:
```
1st measurement (0°): N
2nd measurement (90°): N  
3rd measurement (0°): N or S (50% each!)
```

**Critical insight**: Third measurement is random even though first was N!

**Conclusion**: Second measurement **destroyed information** about first measurement.

**For quantum clock**: Ask "12?" → "3?" → "12?" 
- First and third answers need NOT match
- Middle question **affected the system**

### Three Profound Implications (from QC for Everyone)

**1. Definite States Exist**
- Repeating same measurement gives same answer
- Not everything is random
- Eigenstates are **real**

**2. True Randomness Exists**
- Not "sensitive dependence on initial conditions"  
- Not "hidden variables we don't know"
- **Fundamental indeterminacy** in nature
- **Einstein's objection**: "God does not play dice"
- **Experiments prove**: Nature IS truly random

**3. Measurements Affect Systems**
- Cannot passively observe quantum systems
- Act of measurement **changes the state**
- Not just practical limitation (like "observing changes it")
- **Fundamental aspect** of quantum mechanics

### Photon Polarization (Physical Demonstration)

**Experimental setup** (QC for Everyone):
- **Polarized film squares** act like Stern-Gerlach for photons
- Each square lets through one polarization, blocks perpendicular

**Experiment 1**: Two squares, same orientation
```
Result: Light passes through (both transmit same polarization)
```

**Experiment 2**: Two squares, perpendicular (90° rotation)
```
Result: NO light passes through overlap
```

**Experiment 3**: Three squares (0°, 45°, 90°)
```
Astounding result: Light DOES pass through all three!
```

**How is this possible?**
- 0° filter: Blocks horizontal, transmits vertical
- 45° filter: Measures in diagonal basis → **randomizes** outcome
- 90° filter: Now has 50% chance to transmit (photons now diagonal)

**Without middle filter**: No transmission (0° and 90° perpendicular)
**With middle filter**: Some transmission (45° breaks the correlation)

This is **directly analogous** to three-measurement spin experiment!

### Rotations Using Pauli Matrices (Lecture Note 10 Nov)

**General rotation operator**:
```
Rᵢ(θ) = e^(-iθσᵢ/2) = cos(θ/2)I - i sin(θ/2)σᵢ
```

**Specific rotations**:
```
Rₓ(θ) = [cos(θ/2)   -i sin(θ/2)]
        [-i sin(θ/2)  cos(θ/2)  ]

Rᵧ(θ) = [cos(θ/2)   -sin(θ/2)]
        [sin(θ/2)    cos(θ/2) ]

Rᵨ(θ) = [e^(-iθ/2)      0     ]
        [0          e^(iθ/2)  ]
```

**Interpretation**: Rotations on **Bloch sphere** (qubit state space).

### Pauli Exclusion Principle

**Statement**: No two identical **fermions** (spin-1/2 particles) can occupy the same quantum state simultaneously.

**Mathematical form**: Multi-fermion wave function must be **antisymmetric** under particle exchange:
```
ψ(r₁, r₂) = -ψ(r₂, r₁)
```

**Consequences**:
1. **Electron configuration** in atoms:
   - 1s: max 2 electrons (opposite spins)
   - 2s: max 2 electrons
   - 2p: max 6 electrons (3 orbitals × 2 spins)

2. **Periodic table structure**:
   - Chemical properties from electron shell filling
   - Valence electrons determine reactivity

3. **Stability of matter**:
   - Prevents collapse of all electrons into lowest state
   - Creates "degeneracy pressure"

4. **Exchange interaction**:
   - Extra energy from quantum statistics
   - Explains ferromagnetism

**Bosons** (integer spin): CAN occupy same state → **Bose-Einstein condensation**

### Spin Measurement - Mathematical Description

**General spin state**:
```
|ψ⟩ = α|↑⟩ + β|↓⟩
```
where |α|² + |β|² = 1 (normalization).

**Measuring σᵨ** (spin in z-direction):
- Outcome **+1** with probability |α|²  → state becomes |↑⟩
- Outcome **-1** with probability |β|²  → state becomes |↓⟩

**Expectation value**:
```
⟨σᵨ⟩ = ⟨ψ|σᵨ|ψ⟩ = |α|² - |β|²
```

**Example**: Equal superposition |+⟩ = (|↑⟩ + |↓⟩)/√2
```
⟨σᵨ⟩ = 0  (average over many measurements)
Measurement outcomes: +1 or -1 (50% each)
```

### Connection to Qubits

**Computational basis**:
```
|0⟩ ≡ |↑⟩ = [1]    |1⟩ ≡ |↓⟩ = [0]
            [0]                [1]
```

**Pauli gates** = quantum logic gates:
- **X gate**: Bit flip (|0⟩ ↔ |1⟩)
- **Y gate**: Bit+phase flip  
- **Z gate**: Phase flip (|1⟩ → -|1⟩)

**Single-qubit gates** generated by Pauli matrices:
```
Any U = e^(iα) e^(-iβσₙ)
```
where σₙ = n·σ⃗ (rotation axis).

### Summary - Why Spin Matters for Quantum Computing

1. **Natural qubit representation**: Electron spin, nuclear spin, photon polarization
2. **Two-level system**: Perfect for binary quantum information
3. **Measurement basis**: Pauli matrices define measurement operators
4. **Gate operations**: Rotations on Bloch sphere = single-qubit gates
5. **Quantum randomness**: Demonstrates fundamental quantum behavior
6. **Experimental accessibility**: Can be measured and controlled

**Sources**: Quantum Computing for Everyone (Chapter 1-2), Lecture notes (Nov 10), quantum mechanics textbooks

---

## Entanglement

### Definition
Quantum entanglement occurs when two or more quantum systems become correlated in such a way that the quantum state of the entire system cannot be described as a product of individual quantum states, even when the systems are separated by large distances. **Entanglement is the most purely quantum of all quantum phenomena.**

From "Quantum Computing for Everyone": *"Qubits can be entangled. When we make a measurement of one of them, it affects the state of the other. This is something that we don't experience in our daily lives, but it is described perfectly by our mathematical model."*

### Mathematical Characterization

**Separable (Non-entangled) state**:
```
|ψ⟩ₐᵦ = |ψₐ⟩ ⊗ |ψᵦ⟩
```
Can be written as a product of individual states.

**Entangled state**:
```
|ψ⟩ₐᵦ ≠ |ψₐ⟩ ⊗ |ψᵦ⟩ for any |ψₐ⟩, |ψᵦ⟩
```
Cannot be factored into individual system states.

### Key Concepts

#### 1. Non-Separability
The defining feature of entanglement. For entangled qubits Alice and Bob share, **there is no way to describe Alice's qubit alone** - you must describe the joint state.

#### 2. Measurement Correlations
**Einstein's "spooky action at a distance"**: Measuring one entangled qubit **instantaneously affects** the state of its partner, regardless of separation distance.

**Example**: For Bell state |Φ⁺⟩ = (|00⟩ + |11⟩)/√2
- Before measurement: Both qubits in superposition
- Alice measures her qubit → gets 0 or 1 (50% each)
- Bob's qubit **immediately** becomes |0⟩ or |1⟩ to match Alice's result
- Correlation: Results always match (both 0 or both 1)

#### 3. Bell States
The **four maximally entangled** two-qubit states form an orthonormal basis:

```
|Φ⁺⟩ = (|00⟩ + |11⟩)/√2  (even parity, no phase)
|Φ⁻⟩ = (|00⟩ - |11⟩)/√2  (even parity, π phase)
|Ψ⁺⟩ = (|01⟩ + |10⟩)/√2  (odd parity, no phase)
|Ψ⁻⟩ = (|01⟩ - |10⟩)/√2  (odd parity, π phase)
```

**Properties**:
- Maximally entangled: Measurement of one qubit gives **maximum information** about the other
- Symmetric/antisymmetric: Under qubit exchange
- Orthogonal: ⟨Φ⁺|Φ⁻⟩ = 0, etc.

#### 4. EPR Paradox
**Einstein-Podolsky-Rosen thought experiment** (1935): Tried to show quantum mechanics was incomplete.

**EPR argument**:
1. If quantum mechanics complete, measuring A gives info about distant B
2. Measurement at A shouldn't affect B (locality)
3. Therefore, B must have had definite value all along (realism)
4. Quantum mechanics doesn't predict definite values → incomplete

**Resolution**: Nature violates local realism. Quantum mechanics is complete, but non-local correlations exist.

#### 5. No-Cloning Theorem
**Cannot create perfect copies of unknown quantum states.**

**Proof sketch**: If cloning were possible:
```
U|ψ⟩|0⟩ = |ψ⟩|ψ⟩ for all |ψ⟩
```

But for |ψ₁⟩ and |ψ₂⟩:
```
⟨ψ₁|ψ₂⟩ = ⟨ψ₁|ψ₂⟩²
```

This only works if ⟨ψ₁|ψ₂⟩ = 0 or 1 (orthogonal or identical).

**Implications**:
- Quantum information is fundamentally different from classical
- Secure quantum communication possible
- Quantum teleportation doesn't violate no-cloning

### Creating Entanglement (Quantum Computing for Everyone, Chapter 4)

**Using CNOT gate**:

```
Step 1: Prepare |00⟩
Step 2: Apply Hadamard to first qubit → (|0⟩ + |1⟩)/√2 ⊗ |0⟩
Step 3: Apply CNOT → (|00⟩ + |11⟩)/√2 = |Φ⁺⟩
```

**Circuit**:
```
|0⟩──H──•──
        │
|0⟩─────X──
```

Result: Bell state |Φ⁺⟩ (maximally entangled)

### Measuring Entangled Qubits

**Different bases yield different correlations** (from QC for Everyone):

For |Φ⁺⟩ = (|00⟩ + |11⟩)/√2:

**Standard basis** (Z-measurement):
- Both measure 0: 50%
- Both measure 1: 50%
- Opposite results: 0%
- **Perfect correlation**

**Hadamard basis** (X-measurement):
First convert: H|Φ⁺⟩ = (|++⟩ + |--⟩)/√2
- Both measure +: 50%
- Both measure -: 50%
- Opposite results: 0%
- **Still perfect correlation**

**Mixed bases** (Alice: Z, Bob: X):
- All four outcomes equally likely (25% each)
- **No correlation** (measurements incompatible)

### Superluminal Communication?

**Question**: If measuring Alice's qubit affects Bob's, can we send information faster than light?

**Answer**: **NO**. Here's why:

1. Bob's individual measurements are random (50% 0, 50% 1)
2. The correlation only appears when Alice and Bob **compare results**
3. Comparison requires **classical communication** (≤ light speed)
4. No way to detect entanglement from one qubit alone

**Mathematical proof**: Bob's reduced density matrix:
```
ρᵦ = Trₐ(|Φ⁺⟩⟨Φ⁺|) = I/2
```
Completely mixed state (maximum entropy) - contains no information.

### Applications of Entanglement

#### 1. Quantum Key Distribution (QKD)
- BB84 protocol: Single qubit security
- **Ekert (E91/BBM92) protocol**: Uses entangled pairs
- Eavesdropping detection through Bell inequality violation

#### 2. Quantum Teleportation
- Transfer quantum state using entanglement + classical bits
- Doesn't violate no-cloning or causality
- Alice destroys original, Bob recreates it

#### 3. Superdense Coding  
- Send 2 classical bits using 1 qubit + shared entanglement
- Doubles classical channel capacity
- Uses 4 Bell states to encode 00, 01, 10, 11

#### 4. Quantum Computing
- **Computational speedup**: Many quantum algorithms exploit entanglement
- Grover's algorithm: Quadratic speedup for search
- Shor's algorithm: Exponential speedup for factoring
- Quantum error correction

### Entanglement and Computation (from QC for Everyone)

**Key insight**: "Quantum computing and classical computing are not two distinct disciplines, but quantum computing is the more fundamental form of computing."

**Entangled qubits represent** exponentially large space:
- n qubits: 2ⁿ dimensional Hilbert space
- n = 3: 8 amplitudes
- n = 300: More states than atoms in universe
- Classical computer can't efficiently simulate

### Bell's Inequality (Chapter 5)

**Tests local realism experimentally**:

**Classical (local realist) prediction**: Certain correlation bounds
**Quantum mechanical prediction**: Violates these bounds

**CHSH inequality** (Clauser-Horne-Shimony-Holt):
```
|E(a,b) - E(a,b') + E(a',b) + E(a',b')| ≤ 2 (classical)
```

**Quantum violation**:
```
Maximum = 2√2 ≈ 2.828
```

**Experiments confirm**: Quantum mechanics is correct, local realism is false.

**Quote from QC for Everyone**: "Bell thought he would be proved correct [that hidden variables explain quantum correlations]. He was wrong."

### Example - Detailed Calculation

**Alice and Bob share** |Φ⁺⟩ = (|00⟩ + |11⟩)/√2

**Alice measures in standard basis**:
```
Result: |0⟩ with prob 1/2, state becomes |00⟩
Result: |1⟩ with prob 1/2, state becomes |11⟩
```

**Bob now has**:
```
|0⟩ if Alice got 0
|1⟩ if Alice got 1
```

Bob's qubit is no longer in superposition! Measurement of Alice's qubit **collapsed** the entangled state.

**Correlation strength**: Measure in different basis θ apart:
```
Correlation = cos²(θ)
```

Maximum correlation (θ=0): 1 (perfect)
No correlation (θ=90°): 0.5 (random)

**Sources**: Quantum Computing for Everyone (Chapters 4-5), lecture notes

---

---

## Dynamics

### Definition
Quantum dynamics describes how quantum systems evolve in time, governed by the time-dependent Schrödinger equation.

### Key Concepts
- **Schrödinger Picture**: States evolve, operators are fixed
- **Heisenberg Picture**: Operators evolve, states are fixed
- **Interaction Picture**: Both states and operators evolve
- **Ehrenfest Theorem**: Quantum expectations follow classical equations
- **Conservation Laws**: Related to symmetries (Noether's theorem)

### Time Evolution
For time-independent Hamiltonian:
```
|ψ(t)⟩ = e^(-iĤt/ℏ)|ψ(0)⟩
```

For time-dependent Hamiltonian:
```
|ψ(t)⟩ = 𝒯exp(-i/ℏ ∫₀ᵗ Ĥ(t')dt')|ψ(0)⟩
```

### Example
Free particle evolution:
- Wave packet spreads over time
- Group velocity: vg = ∂ω/∂k = ℏk/m
- Phase velocity: vp = ω/k = ℏk/2m

**Sources**: Computational Introduction to Quantum Physics

---

## The Adiabatic Theorem

### Definition
The adiabatic theorem states that a quantum system remains in its instantaneous eigenstate if a perturbation acting on it changes slowly enough and there is a gap between the eigenvalue and the rest of the spectrum.

### Key Concepts
- **Adiabatic Condition**: dH/dt << (ΔE)²/ℏ where ΔE is the energy gap
- **Instantaneous Eigenstates**: |n(t)⟩ where H(t)|n(t)⟩ = Eₙ(t)|n(t)⟩
- **Geometric Phase**: Berry phase acquired during adiabatic evolution
- **Avoided Crossings**: Energy levels repel when they would otherwise cross

### Mathematical Statement
If system starts in ground state |ψ(0)⟩ = |0(0)⟩ and H(t) changes slowly:
```
|ψ(t)⟩ ≈ e^(iγ(t))|0(t)⟩
```
where γ(t) is the dynamical phase.

### Example - From Lecture Notes (Nov 3, 2025)
In quantum annealing:
- Start with H(0) = H_init (easy to prepare ground state)
- Evolve slowly to H(t_final) = H_problem
- If adiabatic, system remains in ground state
- Ground state of H_problem encodes solution

**Critical Point**: Must move slowly through avoided crossings to maintain ground state population.

**Sources**: Note 3 Nov 2025, Note 10 Nov 2025

---

## Qubits and Quantum Gates

### Definition
A **qubit** (quantum bit) is the basic unit of quantum information, existing in a superposition of |0⟩ and |1⟩ states. **Quantum gates** are unitary operations that manipulate qubits.

### Qubit Representation
```
|ψ⟩ = α|0⟩ + β|1⟩
```
where |α|² + |β|² = 1

**Bloch Sphere**: Geometric representation where:
- |0⟩ at north pole
- |1⟩ at south pole
- Superpositions on the sphere surface

### Single-Qubit Gates

#### Pauli Gates
```
X = [0 1]  (bit flip)
    [1 0]

Y = [0 -i]
    [i  0]

Z = [1  0]  (phase flip)
    [0 -1]
```

#### Hadamard Gate
```
H = 1/√2 [1  1]
         [1 -1]

H|0⟩ = (|0⟩ + |1⟩)/√2
H|1⟩ = (|0⟩ - |1⟩)/√2
```

#### Phase Gates
```
S = [1 0]  (π/2 phase)
    [0 i]

T = [1  0]  (π/4 phase)
    [0 e^(iπ/4)]
```

#### Rotation Gates (from Note 10 Nov 2025)
```
Rₓ(θ) = cos(θ/2)I - i sin(θ/2)X
Rᵧ(θ) = cos(θ/2)I - i sin(θ/2)Y
Rᵧ(θ) = cos(θ/2)I - i sin(θ/2)Z = [e^(-iθ/2)    0     ]
                                   [   0      e^(iθ/2)]
```

### Two-Qubit Gates

#### CNOT (Controlled-NOT)
```
CNOT = [1 0 0 0]
       [0 1 0 0]
       [0 0 0 1]
       [0 0 1 0]
```
Flips target qubit if control is |1⟩

#### CZ (Controlled-Z)
```
CZ = [1 0 0  0]
     [0 1 0  0]
     [0 0 1  0]
     [0 0 0 -1]
```

#### Two-Qubit Rotations (from Note 10 Nov 2025)
```
e^(-iθZᵢZⱼ) implements ZZ interaction between qubits i and j
```

Circuit implementation:
```
──•────────•──
  │        │
──X──Rz(θ)──X──
```

### Universal Gate Sets
- {H, T, CNOT} is universal for quantum computation
- Any quantum computation can be approximated with these gates
- {Rotation gates, CNOT} also universal

**Sources**: Note 10 Nov 2025, Quantum Computing textbooks

---

## Quantum Key Distribution

### Definition
Quantum Key Distribution (QKD) allows two parties to generate a shared secret key using quantum mechanics, with security guaranteed by the laws of physics rather than computational complexity.

### BB84 Protocol

**Steps**:
1. **Alice** prepares qubits randomly in one of four states:
   - Rectilinear basis: |0⟩, |1⟩
   - Diagonal basis: |+⟩ = (|0⟩+|1⟩)/√2, |-⟩ = (|0⟩-|1⟩)/√2

2. **Alice** sends qubits to Bob through quantum channel

3. **Bob** randomly measures in rectilinear or diagonal basis

4. **Alice and Bob** publicly compare basis choices (not results)

5. Keep bits where bases matched, discard others

6. **Estimate error rate** on subset of remaining bits

7. If error rate low, perform:
   - **Error correction**
   - **Privacy amplification**
   
8. Result: Shared secret key

**Security**: Any eavesdropper disturbs quantum states (no-cloning theorem), detectable as increased error rate.

### BBM92 Protocol (Ekert's Protocol)

**Uses entanglement** (Bell pairs):

1. **Source** creates entangled pairs: |Φ⁺⟩ = (|00⟩ + |11⟩)/√2

2. Alice receives one qubit, Bob receives the other

3. Both measure in randomly chosen bases

4. Compare bases publicly, keep correlated results

5. **Test Bell inequality** on subset to detect eavesdropping

6. If Bell inequality violated (as expected for entangled pairs), proceed with key

**Advantage**: Eavesdropping detection through Bell inequality violation

### Example
Alice sends: |0⟩ (rectilinear)
Bob measures: diagonal basis
Result: Random, discard

Alice sends: |+⟩ (diagonal)
Bob measures: diagonal basis  
Result: |+⟩ with certainty, keep

**Sources**: Quantum Computing textbooks

---

## Superdense Coding

### Definition
Superdense coding allows transmission of 2 classical bits of information by sending only 1 qubit, using a pre-shared entangled pair.

### Protocol

**Setup**: Alice and Bob share Bell state |Φ⁺⟩ = (|00⟩ + |11⟩)/√2

**Encoding** (Alice applies gates based on 2-bit message):
- 00: Apply I → |Φ⁺⟩ = (|00⟩ + |11⟩)/√2
- 01: Apply X → |Ψ⁺⟩ = (|01⟩ + |10⟩)/√2
- 10: Apply Z → |Φ⁻⟩ = (|00⟩ - |11⟩)/√2
- 11: Apply ZX → |Ψ⁻⟩ = (|01⟩ - |10⟩)/√2

**Transmission**: Alice sends her qubit to Bob

**Decoding**: Bob performs Bell state measurement on both qubits to determine which of 4 Bell states → recovers 2 bits

### Circuit
```
Alice's qubit: ───U───────────────
                  │
Bob's qubit:   ───•───CNOT───H───
```
where U ∈ {I, X, Z, ZX}

### Key Insight
- Classical channel: 1 qubit carries 1 bit
- Quantum channel with entanglement: 1 qubit carries 2 bits
- Requires pre-shared entanglement

**Sources**: Quantum Computing textbooks

---

## Quantum Teleportation

### Definition
Quantum teleportation transfers the quantum state of a qubit from one location to another using entanglement and classical communication, without physically transmitting the qubit.

### Protocol

**Initial State**: |ψ⟩ = α|0⟩ + β|1⟩ (unknown state to teleport)

**Resources**: Bell pair |Φ⁺⟩ = (|00⟩ + |11⟩)/√2 shared between Alice and Bob

**Steps**:

1. **Alice** has:
   - Qubit in state |ψ⟩ (to teleport)
   - Her half of |Φ⁺⟩
   
2. **Alice** performs Bell measurement on her two qubits
   - Outcome: one of 4 possibilities (00, 01, 10, 11)
   - Alice's qubit state is destroyed (measurement)

3. **Alice** sends 2 classical bits to Bob (measurement outcome)

4. **Bob** applies correction based on received bits:
   - 00: Apply I (nothing)
   - 01: Apply X
   - 10: Apply Z
   - 11: Apply ZX

5. **Bob's qubit now in state** |ψ⟩ = α|0⟩ + β|1⟩

### Circuit
```
|ψ⟩: ───────•───H───M───╲
            │       │    ╲ classical bits
|Φ⁺⟩: ──────X───────M────╲
                         ╲
Bob:   ─────────────────X──Z──  (conditional gates)
```

### Key Points
- No-cloning theorem not violated (original destroyed)
- Requires classical communication (no faster-than-light)
- Entanglement + 2 classical bits needed
- State transferred without knowing α, β

**Sources**: Quantum Computing textbooks

---

## Quantum Circuits and Algorithms

### Definition
Quantum circuits are sequences of quantum gates acting on qubits, representing quantum algorithms visually and mathematically.

### Circuit Model of Quantum Computing

**Components**:
1. **Initialization**: Prepare qubits in |0⟩
2. **Gate operations**: Apply unitary transformations
3. **Measurement**: Extract classical information

**Circuit Notation**:
- Time flows left to right
- Horizontal lines represent qubits
- Boxes represent gates
- Vertical lines connect multi-qubit gates

### Example Circuit (from Note 10 Nov 2025)
```
|0⟩: ──H──•──────
          │
|0⟩: ─────X──────
```
Creates Bell state |Φ⁺⟩ = (|00⟩ + |11⟩)/√2

### Key Algorithms

#### 1. Deutsch's Algorithm
**Problem**: Determine if f:{0,1}→{0,1} is constant or balanced
**Classical**: 2 queries needed
**Quantum**: 1 query sufficient

#### 2. Deutsch-Jozsa Algorithm  
**Problem**: Generalization to n bits
**Classical**: 2^(n-1) + 1 queries worst case
**Quantum**: 1 query

#### 3. Grover's Algorithm
**Problem**: Search unstructured database of N items
**Classical**: O(N) queries
**Quantum**: O(√N) queries
**Speedup**: Quadratic

#### 4. Shor's Algorithm
**Problem**: Factor integers
**Classical**: Exponential time
**Quantum**: Polynomial time (efficient)
**Impact**: Breaks RSA encryption

### Quantum Advantage
Quantum algorithms can provide:
- **Exponential speedup**: Shor's algorithm
- **Polynomial speedup**: Grover's algorithm
- **Quantum simulation**: Efficient simulation of quantum systems

**Sources**: Lecture notes, Quantum Computing textbooks

---

## Deutsch-Jozsa Algorithm

### Definition
The Deutsch-Jozsa algorithm determines whether a Boolean function f:{0,1}ⁿ→{0,1} is constant (same output for all inputs) or balanced (equal number of 0s and 1s in outputs) with a single query.

### Problem Statement
Given: Black-box (oracle) implementing f(x)
Promised: f is either constant or balanced
Find: Which type is f?

**Classical complexity**: Need to evaluate f for 2^(n-1) + 1 inputs in worst case
**Quantum complexity**: 1 query

### Algorithm Steps

1. **Initialize**: n+1 qubits in state |0⟩⊗ⁿ|1⟩

2. **Hadamard**: Apply H to all qubits
   ```
   |ψ⟩ = 1/√(2^n) Σₓ |x⟩ ⊗ (|0⟩-|1⟩)/√2
   ```

3. **Oracle**: Apply Uₓ: |x⟩|y⟩ → |x⟩|y⊕f(x)⟩
   ```
   |ψ⟩ = 1/√(2^n) Σₓ (-1)^f(x) |x⟩ ⊗ (|0⟩-|1⟩)/√2
   ```

4. **Hadamard**: Apply H to first n qubits

5. **Measure**: Measure first n qubits

### Result
- **All 0s** → f is constant
- **Any 1** → f is balanced

### Circuit
```
|0⟩: ──H────────────H──M
|0⟩: ──H────────────H──M
 ⋮     ⋮      Uₓ     ⋮   ⋮
|0⟩: ──H────────────H──M
|1⟩: ──H────────────────
```

### Why It Works
- Constant f: All amplitudes constructively interfere at |0⟩⊗ⁿ
- Balanced f: Amplitudes destructively interfere at |0⟩⊗ⁿ

**Sources**: Quantum Computing textbooks

---

## Simon's Algorithm

### Definition
Simon's algorithm finds the hidden period s of a function f:{0,1}ⁿ→{0,1}ⁿ that satisfies f(x) = f(y) if and only if x⊕y ∈ {0,s}, providing exponential speedup over classical algorithms.

### Problem Statement
Given: Oracle for function f with hidden string s
Promise: f(x) = f(x⊕s) for all x, and f is one-to-one on different cosets
Find: The secret string s

**Classical complexity**: Exponential (Ω(2^(n/2)))
**Quantum complexity**: Polynomial (O(n))

### Algorithm Steps

1. **Initialize**: 2n qubits in |0⟩⊗²ⁿ

2. **Hadamard**: Apply H⊗ⁿ to first n qubits
   ```
   |ψ⟩ = 1/√(2^n) Σₓ |x⟩|0⟩
   ```

3. **Oracle**: Apply Uₓ: |x⟩|0⟩ → |x⟩|f(x)⟩

4. **Measure second register**: Get some f(x₀)
   State collapses to:
   ```
   |ψ⟩ = 1/√2 (|x₀⟩ + |x₀⊕s⟩)
   ```

5. **Hadamard**: Apply H⊗ⁿ to first register

6. **Measure first register**: Get random y with y·s = 0 (mod 2)

7. **Repeat**: O(n) times to get n linearly independent equations

8. **Solve**: Linear system y₁·s = 0, y₂·s = 0, ..., yₙ·s = 0 for s

### Example
If n=3 and s=110:
- Need 3 measurements giving y₁, y₂, y₃
- Solve system:
  ```
  y₁ · 110 = 0 (mod 2)
  y₂ · 110 = 0 (mod 2)
  y₃ · 110 = 0 (mod 2)
  ```
- Extract s = 110

### Significance
- Foundation for Shor's factoring algorithm
- Demonstrates exponential quantum advantage
- Shows power of quantum interference

**Sources**: Quantum Computing textbooks

---

## Quantum Algorithms and Their Implications

### Computational Complexity Classes

**Classical**:
- P: Problems solvable in polynomial time
- NP: Problems verifiable in polynomial time
- NP-Complete: Hardest problems in NP

**Quantum**:
- BQP: Problems solvable in polynomial time on quantum computer
- BQP contains P
- Relationship between BQP and NP unknown

### Major Quantum Algorithms and Impact

#### 1. Shor's Algorithm (1994)
**Problem**: Integer factorization
**Speedup**: Exponential
**Impact**:
- Breaks RSA, ECC cryptography
- Threatens current internet security
- Motivates post-quantum cryptography
- N-bit number: Classical ~exp(N^(1/3)), Quantum ~N²

#### 2. Grover's Algorithm (1996)
**Problem**: Unstructured search
**Speedup**: Quadratic (√N)
**Impact**:
- Optimal for unstructured search
- Breaks symmetric cryptography (AES needs longer keys)
- Applications: Database search, optimization

#### 3. Quantum Simulation
**Problem**: Simulate quantum systems
**Speedup**: Exponential
**Impact**:
- Drug discovery
- Material science
- Chemistry simulations
- Financial modeling

#### 4. Variational Algorithms (VQE, QAOA)
**Problem**: Optimization, ground state finding
**Advantage**: Near-term quantum computers (NISQ era)
**Impact**:
- Portfolio optimization
- Machine learning
- Quantum chemistry

### Implications

**Cryptography**:
- Post-quantum cryptography development
- Lattice-based, code-based, hash-based schemes
- Quantum key distribution for unconditional security

**Optimization**:
- Supply chain optimization
- Traffic flow
- Resource allocation
- Machine learning training

**Scientific Discovery**:
- Drug design
- Catalyst development
- High-temperature superconductors
- Understanding quantum systems

**Limitations**:
- Not all problems have quantum speedup
- NP-complete problems: No known exponential speedup
- Quantum computers complement, not replace classical

**Sources**: Quantum Computing textbooks, contemporary research

---

## Adiabatic Quantum Computing

### Definition
Adiabatic Quantum Computing (AQC) is a model of quantum computation based on the adiabatic theorem, where the system evolves slowly from an easy initial Hamiltonian to a problem Hamiltonian whose ground state encodes the solution.

### From Lecture Notes (Note 3 Nov 2025, Note 10 Nov 2025)

### Core Principle
**Start** with Hamiltonian H_init whose ground state is easy to prepare
**Evolve** slowly to problem Hamiltonian H_problem  
**End** in ground state of H_problem (solution)

### Mathematical Framework

Time-dependent Hamiltonian:
```
H(t) = (1 - λ(t))H_init + λ(t)H_problem
```

where λ(t) goes from 0 to 1, often called the schedule or protocol.

**Initial** (t=0): H(0) = H_init, λ(0) = 0
**Final** (t=T): H(T) = H_problem, λ(T) = 1

### Initial Hamiltonian (from Note 3 Nov 2025)

Typically:
```
H_init = -Σᵢ σₓⁱ
```

Ground state: |+⟩⊗ⁿ = |+...+⟩ (all qubits in |+⟩ = (|0⟩+|1⟩)/√2)

**Spectrum of H_init**:
- Ground state energy: E = -N
- First excited: E = -N + 2 (one qubit flipped)
- Maximum energy: E = +N

### Problem Hamiltonian

For optimization problems (QUBO, Ising):
```
H_problem = Σᵢⱼ Jᵢⱼ σᵧⁱσᵧʲ + Σᵢ hᵢσᵧⁱ
```

Eigenstates: Computational basis states |b₁b₂...bₙ⟩
Ground state: Encodes optimal solution

### Adiabatic Condition

From lecture notes: **"Change H(t) as slowly as possible"**

Quantitatively:
```
dλ/dt << (ΔE_min)² / ||dH/dλ||
```

where ΔE_min is the minimum energy gap during evolution.

### Avoided Crossings (Note 3 Nov 2025)

**Critical concept**: Energy levels don't cross, they "avoid" each other

```
Energy ↑
        │     ╱╲  ← Avoided crossing
        │    ╱  ╲    (minimum gap)
        │___╱____╲___
        └──────────→ λ(t)
```

**Must move slowly through avoided crossings** to stay in ground state band.

### Annealing Protocols (from Note 3 Nov 2025)

Different schedules λ(t) possible:
- **Linear**: λ(t) = t/T
- **Fast at beginning, slow at end**
- **Slow at beginning, fast at end**

Speed parameter determines success probability.

### Trade-offs (Note 3 Nov 2025)

**Too fast**:
- System can jump to excited states
- Solution quality degrades

**Too slow**:
- Need results quickly (practical constraint)
- Longer time → more noise/decoherence
- Open system effects accumulate

"After some time limit, everything is washed out" - Note 3 Nov 2025

### Optimization Strategy (Note 3 Nov 2025)

Since we don't know:
- Width of avoided crossings
- Location on t-axis
- Optimal speed

**Recipe**: "TUNE THE SPEED AND TRY"
1. Run with different speeds
2. Find speed region where specific solution appears frequently
3. That solution is likely optimal for the QUBO instance

### Computational Equivalence

**Theorem**: Adiabatic Quantum Computing is polynomially equivalent to the gate model (circuit model) of quantum computing.

**Implication**: AQC is universal for quantum computation

### Example Application - Number Partition (Note 3 Nov 2025)

Problem: Partition numbers into two sets with equal sums

1. Formulate as QUBO
2. Map to Ising Hamiltonian H_problem
3. Set up annealing instance
4. Try different protocols and speeds
5. Most frequent outcome is solution

**Sources**: Note 3 Nov 2025, Note 10 Nov 2025

---

## Quantum Annealing

### Definition (from Note 3 Nov 2025)
Quantum Annealing (QA) is a practical implementation of adiabatic quantum computing, designed for solving optimization problems by finding ground states of Ising Hamiltonians.

### QA Workflow (Note 3 Nov 2025)

**Problem**: Find x̄ = argmin C(x) where x ∈ {0,1}ⁿ (QUBO instance)

**Steps**:
1. Map to Ising model: H_p = Σᵢⱼ Jᵢⱼ σᵧⁱσᵧʲ + Σᵢ hᵢσᵧⁱ
2. Define H(t) = μ(t)H_init + H_p
3. Start with μ(0) = large, system in ground state of H_init
4. Slowly decrease μ(t) to 0
5. Measure qubits to get solution

### Time Evolution

Hamiltonian schedule:
```
H(t) = μ(t)H_init + H_p
```

where:
- μ(0) >> 1 (large positive value)
- μ(t_stop) ≈ 0
- H_init = -Σᵢ σₓⁱ

### Stopping Time (Note 3 Nov 2025)

**Practical consideration**: Must stop at some t_stop when μ(t_stop) ≈ 0

**Trade-off**:
1. **Need results**: Can't anneal for years/days
   - Day, hour, minute, second constraints
   
2. **Open system**: Annealer subject to:
   - Environmental noise
   - Cross-talk between qubits
   - Hardware imperfections
   - "The larger the annealing time, the more time for all interference effects"

### Annealing Schedules (Note 3 Nov 2025)

Different protocols possible:

```
μ(t) ↑
     │╲
     │ ╲___      ← Fast decay initially
     │     ───
     └─────────→ t

μ(t) ↑
     │────╲
     │     ╲     ← Slow initially, fast at end
     │      ╲___
     └─────────→ t
```

Can be parametrized by speed: "They are different with respect to e.g. decay fast at beginning, slow at end, etc."

### Spectrum Analysis (Note 3 Nov 2025)

**H_init spectrum**:
- All 2ⁿ computational basis states are eigenstates
- Ground state: |+...+⟩ with E = -N
- Symmetric spectrum around E = 0 (if N even)

**H_p spectrum**:
- Computational basis states are eigenstates
- Energy values correspond to cost function: E = C(x)
- Ground state corresponds to optimal solution
- "We do not know their energies, but that is exactly our optimization problem"

### Real Annealer Hardware (Note 3 Nov 2025)

**Chimera Graph** structure:
- System of N qubits (N ~ 10³ to 5×10³)
- Not all-to-all connectivity
- Near-planar graph topology
- Nodes connected in specific pattern

**Embedding**: Need to map arbitrary problem graph onto Chimera topology

### Comparison to Gate Model

**Adiabatic/Annealing**:
- Continuous time evolution
- Analog process
- Sensitive to noise accumulation
- Good for optimization

**Gate Model**:
- Discrete gate operations
- Digital process
- Error correction possible
- Universal quantum computation

### Practical Recipe (Note 3 Nov 2025)

Since gap widths and locations unknown:

1. **Tune the speed** of annealing
2. **Try different protocols** (schedules)
3. **Look for patterns**: "Find region in parameter space such that some binary combinations appear most of the time"
4. **Hint**: Most frequent result is likely solution
5. **Also play with weights** A and B in objective and penalty parts

### Example - Number Partition (Note 3 Nov 2025)

"Use Number Partition. Numerically simulate QA and explore how it performs for different protocols, different speeds."

**Sources**: Note 3 Nov 2025, Note 10 Nov 2025

---

## QAOA and Variational Circuits

### Definition (from Note 10 Nov 2025)
The Quantum Approximate Optimization Algorithm (QAOA) is a hybrid quantum-classical algorithm that approximates quantum annealing using parametrized quantum circuits, suitable for near-term quantum computers.

### Motivation (Note 10 Nov 2025)

**Challenge with QA on gate-based quantum computer**:
- QA requires continuous time evolution: U = 𝒯exp(-i∫H(t)dt)
- Gate computers only have discrete gates
- Long evolution accumulates errors
- Need way to approximate QA with short circuits

**QAOA Solution**: 
- Discretize time evolution
- Use parametrized gates
- Optimize parameters classically
- Short depth circuits (NISQ-friendly)

### Mathematical Framework

### Problem Setup (Note 10 Nov 2025)

**Given**: QUBO instance
```
x̄ = argmin C(x), x ∈ {0,1}ⁿ
or
x̄ = argmax C(x), x ∈ {0,1}ⁿ
```

**Ising Hamiltonian**:
```
H_p = Σᵢⱼ Jᵢⱼ σᵧⁱσᵧʲ + Σᵢ hᵢσᵧⁱ
```

Ground state |ψ_gs⟩ encodes solution.

### Trotterization (Note 10 Nov 2025)

**Key idea**: Discretize time into P steps

For QA: H(t) = μ(t)H_init + H_p

**Time slicing**:
```
t ∈ [0, t_stop] → {t₁, t₂, ..., t_P}
Δt = t_stop/P
```

**Approximate** time evolution at each step:
```
e^(-iH(tₖ)Δt) ≈ e^(-iH_init μ(tₖ)Δt) e^(-iH_p Δt)
```

This works when Δt << 1 (operators approximately commute for small time).

### Further Approximation (Note 10 Nov 2025)

Since σₓⁱ operators commute, and σᵧⁱσᵧʲ terms commute:

```
e^(-iH_init μΔt) = e^(-iμΔt Σᵢσₓⁱ) = ∏ᵢ e^(-iμΔt σₓⁱ)

e^(-iH_p Δt) = e^(-iΔt(ΣᵢⱼJᵢⱼσᵧⁱσᵧʲ + Σᵢhᵢσᵧⁱ))
             = ∏ᵢⱼ e^(-iΔt Jᵢⱼσᵧⁱσᵧʲ) ∏ᵢ e^(-iΔt hᵢσᵧⁱ)
```

### QAOA Circuit Structure (Note 10 Nov 2025)

**P-layer QAOA circuit**:

1. **Initialize**: |ψ₀⟩ = |+⟩⊗ⁿ (Hadamard on all qubits)

2. **For each layer** p = 1 to P:
   - Apply e^(-iβₚH_init)
   - Apply e^(-iγₚH_p)

3. **Measure** in computational basis

### Parametrized Gates (Note 10 Nov 2025)

**Mixer operator** (from H_init = -Σσₓⁱ):
```
e^(-iβσₓⁱ) = Rₓ(2β)
```

Implemented as rotation gates on each qubit.

**Problem operator** (from H_p):

**Single-qubit terms**:
```
e^(-iγhᵢσᵧⁱ) = Rᵧ(2γhᵢ)
```

**Two-qubit terms** (Note 10 Nov 2025):
```
e^(-iγJᵢⱼσᵧⁱσᵧʲ)
```

Circuit implementation:
```
─i──•────────•──
    │        │
─j──X──Rz(θ)──X──
```
where θ = 2γJᵢⱼ

### Full QAOA Circuit (Note 10 Nov 2025)

```
|0⟩─H─┤        ├─┤        ├─ ··· ─┤        ├─M
|0⟩─H─┤   U_p  ├─┤  U_m   ├─ ··· ─┤  U_m   ├─M
  ⋮    │  (γₚ)  │ │  (βₚ)  │       │  (βₚ)  │  ⋮
|0⟩─H─┤        ├─┤        ├─ ··· ─┤        ├─M
      └────────┘ └────────┘       └────────┘
         ↑          ↑                  ↑
      Problem    Mixer           P layers
```

where:
- U_p(γ) = e^(-iγH_p)
- U_m(β) = e^(-iβH_init)

### Parameters (Note 10 Nov 2025)

**For P layers**: 2P parameters
- γ = (γ₁, γ₂, ..., γₚ)
- β = (β₁, β₂, ..., βₚ)

**Typically restricted** to intervals:
- 0 ≤ γₚ ≤ γₘₐₓ
- 0 ≤ βₚ ≤ βₘₐₓ

### Variational Optimization (Note 10 Nov 2025)

**Goal**: Find optimal parameters (γ*, β*)

**Objective function**:
```
F(γ, β) = ⟨ψ(γ,β)|H_p|ψ(γ,β)⟩
```

**Procedure**:
1. Choose initial parameters (γ⁰, β⁰)
2. Prepare state |ψ(γ,β)⟩ on quantum computer
3. Measure expectation value ⟨H_p⟩
4. Classical optimizer suggests new parameters
5. Repeat until convergence

**Classical optimizers**:
- COBYLA (Constrained Optimization BY Linear Approximation)
- Nelder-Mead
- Gradient descent (with parameter shift rule)

### Approximation Quality (Note 10 Nov 2025)

**Key statement**: 
"For a fixed P, there is a set {γ*, β*} for which circuit with P layers approximate annealing best"

**What does "approximate best" mean?**
"When we measure qubits, most of the times we obtain the solution or near-optimal solution"

**Approximation ratio**:
```
r_P = F(γ*, β*) / E_opt
```
where E_opt is true optimum.

Generally: r₁ < r₂ < r₃ < ... → 1 as P → ∞

### Connection to Quantum Annealing

**QA**: 
- Continuous evolution
- H(t) changes smoothly
- Infinite dimensional parameter space

**QAOA**:
- Discrete layers
- Fixed number P of applications
- Finite dimensional parameter space (2P parameters)
- As P → ∞, QAOA → QA

### Advantages of QAOA (Note 10 Nov 2025)

**vs Full QA**:
- Shorter circuits → less error accumulation
- "On paper [long evolution] is no problem, but in real life hardware... accumulating errors... will wash out everything"

**vs Pure gate model**:
- Problem-inspired ansatz
- Good performance even with small P
- Suitable for NISQ devices

### Practical Implementation (Note 10 Nov 2025)

**Number of layers**: Typically P = 1 to 10
- P = 1: Often gives approximation ratio > 0.6
- Increasing P improves solution quality
- Trade-off with circuit depth/errors

**Parameter optimization**:
- Can be expensive (many quantum circuit evaluations)
- Smart initialization helps
- Parameter transfer between problem instances

### Variational Quantum Algorithms

QAOA is part of broader family of **Variational Quantum Algorithms (VQAs)**:

**General structure**:
1. Parametrized quantum circuit (ansatz)
2. Measurement of cost function
3. Classical optimization of parameters
4. Hybrid quantum-classical loop

**Other VQAs**:
- VQE (Variational Quantum Eigensolver) - chemistry
- QNLP (Quantum Natural Language Processing)
- Quantum machine learning models

### Circuit Example (Note 10 Nov 2025)

For Max-Cut problem on triangle graph:

```
|0⟩─H─Rₓ(2β)─•─────────•─────────M
             │         │
|0⟩─H─Rₓ(2β)─X─Rz(2γ)─X─•───────M
                         │
|0⟩─H─Rₓ(2β)─────────────X─Rz(2γ)─M
```

### Performance Guarantees

**Theorem** (Farhi et al.): For every optimization problem and depth P, there exist parameters that give approximation ratio ≥ some bound.

**For Max-Cut**: Even P=1 gives guaranteed approximation ratio > 0.69

**Sources**: Note 10 Nov 2025 (primary), Note 3 Nov 2025

---

## Summary

This comprehensive guide covers the fundamental concepts of quantum computing from basic quantum physics through advanced quantum algorithms:

**Foundations**: Wave functions, operators, quantum dynamics, and the mathematical framework of quantum mechanics

**Quantum Information**: Qubits, entanglement, quantum gates, and the building blocks of quantum computation

**Quantum Algorithms**: From Deutsch-Jozsa to Shor's algorithm, demonstrating quantum computational advantage

**Optimization**: Adiabatic quantum computing, quantum annealing, and QAOA - bridging theory and near-term practical quantum computing

**Applications**: Cryptography (QKD), communication protocols (teleportation, superdense coding), and optimization problems

The notes particularly emphasize the practical implementation of quantum annealing and QAOA, reflecting the current focus on NISQ (Noisy Intermediate-Scale Quantum) devices and hybrid quantum-classical algorithms.

---

## References

### Primary Sources
- Lecture Notes: August - November 2025 (ACIT3421_exam_prep/LectureNotes/note text/)
- Note 3 Nov 2025: Quantum Annealing Part 2
- Note 10 Nov 2025: Quantum Approximate Optimization Algorithm

### Textbooks
- Quantum Computing for Everyone (ACIT3421_exam_prep/)
- Computational Introduction to Quantum Physics (ACIT3421_exam_prep/)
- Solutions Manual - Computational Introduction to Quantum Physics (ACIT3421_exam_prep/books pensum/)

### Key Papers (Referenced in Course)
- Farhi et al. - QAOA original paper
- Deutsch & Jozsa - Quantum algorithms
- Shor - Factoring algorithm
- Grover - Search algorithm
- Bennett & Brassard - BB84 protocol
- Ekert - BBM92 protocol

---

*Document created: December 9, 2025*
*Course: ACIT4321 Quantum Computing*
*Study guide compiled from lecture notes and course materials*
