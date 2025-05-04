# Electromagnetism: Lorentz Force Analysis  
**Pure theoretical approach - No simulations required**  

## Fundamental Equation  
The Lorentz force governs charged particle motion:  
\[
\mathbf{F} = q(\mathbf{E} + \mathbf{v} \times \mathbf{B})
\]

## Key Cases & Solutions  

### 1. Pure Magnetic Field (𝐁 only)
**Trajectory**: Circular/helical motion  
- **Larmor radius**:  
  \[
  r_L = \frac{mv_\perp}{|q|B}
  \]  
- **Cyclotron frequency**:  
  \[
  \omega_c = \frac{|q|B}{m}
  \]  

### 2. Crossed Fields (𝐄 ⊥ 𝐁)
**Trajectory**: Cycloid + Drift  
- **E×B drift velocity**:  
  \[
  \mathbf{v}_E = \frac{\mathbf{E} \times \mathbf{B}}{B^2}
  \]  
- **Position functions**:  
  \[
  x(t) = v_E t - r_L \sin(\omega_c t)
  \]
  \[
  y(t) = r_L \cos(\omega_c t)
  \]

## Reference Table  
| Quantity         | Formula                          | Units    |  
|------------------|----------------------------------|----------|  
| Larmor radius    | \( r_L = \frac{mv_\perp}{|q|B} \) | meters   |  
| Gyration period  | \( T_c = \frac{2\pi}{\omega_c} \) | seconds  |  
| Drift velocity   | \( v_E = E/B \)                   | m/s      |  

## Step-by-Step Derivations  

### Circular Motion Proof  
1. Centripetal force = Lorentz force:  
   \[
   \frac{mv_\perp^2}{r} = qv_\perp B
   \]  
2. Solve for radius:  
   \[
   r_L = \frac{mv_\perp}{qB}
   \]

### E×B Drift Proof  
1. Time-average of oscillatory terms → 0  
2. Residual motion:  
   \[
   \mathbf{v}_E = \frac{\mathbf{E} \times \mathbf{B}}{B^2}
   \]

## Applications  
- **Particle accelerators**: Cyclotron resonance at \( \omega = \omega_c \)  
- **Mass spectrometry**: Spatial separation by \( r_L \)  
- **Plasma confinement**: Drift currents in tokamaks  

## Deliverables  
1. **Analytical solutions** for 3+ field configurations  
2. **Hand-drawn diagrams** of trajectories  
3. **Physical interpretation** of all terms  
4. **Real-world system** examples  
