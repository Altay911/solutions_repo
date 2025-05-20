# Kepler's Third Law: Orbital Period and Radius

## Theoretical Foundations

### Derivation of Kepler's Third Law

For a circular orbit with:
- Orbital radius $r$
- Orbital period $T$
- Central mass $M$
- Orbiting mass $m$ (where $m \ll M$)

**Centripetal force = Gravitational force:**

$$ \frac{mv^2}{r} = \frac{GMm}{r^2} $$

**Orbital velocity:**

$$ v = \frac{2\pi r}{T} $$

**Substituting gives Kepler's Third Law:**

$$ T^2 = \left( \frac{4\pi^2}{GM} \right) r^3 $$

### Key Implications

1. **Mass Determination:**
   $$ M = \frac{4\pi^2 r^3}{GT^2} $$

2. **Scale Invariance:**
   The ratio $T^2/r^3$ is constant for all bodies orbiting the same mass

3. **Generalization to Ellipses:**
   Replace $r$ with semi-major axis $a$ for elliptical orbits

## Solar System Examples

| Body | Orbital Radius (AU) | Period (years) | $T^2/a^3$ (yr²/AU³) |
|------|---------------------|----------------|----------------------|
| Mercury | 0.387 | 0.241 | 1.000 |
| Venus | 0.723 | 0.615 | 0.999 |
| Earth | 1.000 | 1.000 | 1.000 |
| Mars | 1.524 | 1.881 | 1.000 |
| Jupiter | 5.203 | 11.86 | 0.999 |

*Data confirms the constant ratio predicted by Kepler*

## Computational Verification

### Circular Orbit Simulation Approach

1. **Numerical Integration:**
   Solve the equations of motion:
   $$ \frac{d^2\mathbf{r}}{dt^2} = -\frac{GM}{r^3}\mathbf{r} $$

2. **Verification Steps:**
   - Simulate orbits with varying $r$
   - Measure resulting periods $T$
   - Plot $T^2$ vs $r^3$ to verify linearity

### Expected Results

1. **Orbit Visualization:**
   - Perfectly circular trajectories
   - Constant orbital velocity

2. **Kepler Verification Plot:**
   - Straight line on $T^2$ vs $r^3$ graph
   - Slope = $4\pi^2/GM$

## Extensions to Real Systems

![alt text](<download (1).png>)
### Elliptical Orbits

1. **Modified Law:**
   $$ T^2 = \left( \frac{4\pi^2}{GM} \right) a^3 $$
   Where $a$ is semi-major axis

2. **Eccentricity Effects:**
   - Period depends only on $a$, not eccentricity
   - Velocity varies throughout orbit

### Binary Systems

For comparable masses $M_1$ and $M_2$:
$$ T^2 = \frac{4\pi^2 a^3}{G(M_1+M_2)} $$

## Practical Applications

1. **Exoplanet Detection:**
   - Measure star's wobble period to determine planet's orbital distance

2. **Satellite Deployment:**
   - Calculate geostationary orbit radius (~42,164 km)

3. **Galactic Dynamics:**
   - Estimate mass distribution in galaxies

## Limitations

1. **Perturbation Effects:**
   - Multi-body systems deviate from ideal law

2. **Relativistic Corrections:**
   - Needed for orbits close to massive objects

3. **Non-Point Masses:**
   - Tidal forces and oblateness affect orbits
![alt text](<download (2).png>)