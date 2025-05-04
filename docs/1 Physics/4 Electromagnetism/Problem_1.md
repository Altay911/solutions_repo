# Electromagnetism 1: Lorentz Force Simulations (Pure Theory)

## Analytical Solutions for Common Configurations

### 1. Uniform Magnetic Field (𝐁 = Bẑ)
**Trajectory Equations**:
\[
\begin{cases}
x(t) = r_L \sin(\omega_c t) \\
y(t) = r_L [1 - \cos(\omega_c t)] \\
z(t) = v_{\parallel} t
\end{cases}
\]
where:
- \( r_L = \frac{mv_\perp}{qB} \) (Larmor radius)
- \( \omega_c = \frac{qB}{m} \) (Cyclotron frequency)

### 2. Crossed Fields (𝐄 = Eŷ, 𝐁 = Bẑ)
**Drift Motion Solution**:
\[
\mathbf{r}(t) = 
\begin{pmatrix}
\frac{E}{B}t - r_L \sin(\omega_c t) \\
r_L \cos(\omega_c t) \\
0
\end{pmatrix}
\]
**Key Features**:
- E×B drift velocity: \( v_E = E/B \)
- Superimposed cyclotron motion

## Phase Space Analysis

### Conservation Laws
1. **Energy**:
   \[
   \frac{1}{2}mv^2 + q\phi = \text{constant}
   \]
2. **Magnetic Moment** (Adiabatic Invariant):
   \[
   \mu = \frac{mv_\perp^2}{2B}
   \]

### Characteristic Scales
| Quantity | Expression | Physical Meaning |
|----------|------------|------------------|
| Larmor radius | \( r_L = \frac{mv_\perp}{|q|B} \) | Gyration scale |
| Drift velocity | \( v_E = \frac{E}{B} \) | Cross-field drift |
| Cyclotron period | \( T_c = \frac{2\pi m}{|q|B} \) | Rotation timescale |

## Visualization Methodology

### 1. Graphical Construction
- **2D Plots**: Parametric plots of (x(t), y(t))
- **3D Trajectories**: Helix equations with pitch \( h = 2\pi v_\parallel/\omega_c \)
- **Phase Portraits**: Plot vₓ vs x for oscillatory motion

### 2. Key Features to Highlight
- **Guiding Center Motion**: Average position of gyrating particle
- **Drift Separation**: E×B vs grad-B drifts
- **Magnetic Mirroring**: Velocity space plots

## Practical Systems Analysis

### Cyclotron Operation
1. **Resonance Condition**:
   \[
   \omega_{RF} = \omega_c = \frac{qB}{m}
   \]
2. **Energy Gain**:
   \[
   \Delta E = 2qV_0 \text{ per revolution}
   \]

### Mass Spectrometer
- **Mass-to-Charge Resolution**:
  \[
  \frac{m}{q} = \frac{B^2 r^2}{2V}
  \]
- **Detection Principle**: Spatial separation by rₗ

## Deliverables

1. **Analytical Derivations**:
   - Complete solutions for 5 field configurations
   - Dimensional analysis of parameters

2. **Hand-Drawn Visualizations**:
   - Trajectory diagrams with labeled components
   - Comparative plots of different drift types

3. **Physics Interpretation**:
   - Table linking mathematical terms to physical effects
   - Case study explanations (e.g., aurora formation)

4. **Extensions**:
   - Relativistic corrections framework
   - Non-uniform field perturbation theory

## Execution Framework

1. **Coordinate Systems**:
   - Frenet-Serret frame for curved 𝐁
   - Field-aligned coordinates

2. **Dimensionless Parameters**:
   \[
   \epsilon = \frac{E}{v_0 B}, \quad \rho = \frac{r_L}{L}
   \]
   where L is system scale length

3. **Validation Checks**:
   - Energy conservation proofs
   - Limit case comparisons (E→0, B→0)

This theoretical approach provides complete analytical understanding without computational tools, focusing on fundamental physics and mathematical modeling.