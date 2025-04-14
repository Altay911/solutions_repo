# Problem 1
# Interference Patterns on a Water Surface

## Motivation

Interference occurs when waves from different sources overlap, forming new patterns on the surface of a medium, such as water. These patterns can illustrate how waves combine in various ways: constructive interference (wave reinforcement) or destructive interference (wave cancellation). Studying these patterns helps us understand fundamental wave behaviors, such as the relationship between wave phase and the effect of multiple sources.

This problem involves analyzing the interference patterns formed on the water surface due to the superposition of waves emitted from point sources placed at the vertices of a regular polygon. By exploring this phenomenon, we gain insight into wave interactions and their real-world applications.

---

## 1. Theoretical Foundation

### Wave Equation

A circular wave on a water surface, originating from a point source, is described by the following equation:

\[
\psi(\mathbf{r}, t) = A \cdot \cos(k r - \omega t + \phi)
\]

Where:
- \( \psi(\mathbf{r}, t) \) is the displacement of the water surface at point \( \mathbf{r} \) and time \( t \)
- \( A \) is the amplitude of the wave
- \( k \) is the wave number, related to the wavelength \( \lambda \), where \( k = \frac{2\pi}{\lambda} \)
- \( \omega \) is the angular frequency, related to the frequency \( f \), where \( \omega = 2\pi f \)
- \( r \) is the distance from the source to the observation point
- \( \phi \) is the initial phase of the wave

### Superposition Principle

The principle of superposition states that when multiple waves overlap, the resulting displacement is the sum of the displacements from all individual waves. Thus, for \( N \) sources located at the vertices of a regular polygon, the total displacement at a point on the surface is:

\[
\Psi(\mathbf{r}, t) = \sum_{i=1}^{N} A_i \cdot \cos(k r_i - \omega t + \phi_i)
\]

Where:
- \( N \) is the number of sources (vertices of the polygon)
- \( A_i \), \( r_i \), and \( \phi_i \) are the amplitude, distance, and initial phase of the wave from the \( i^{th} \) source, respectively.

### Interference Patterns

- **Constructive Interference**: Occurs when the waves from different sources are in phase, leading to wave reinforcement and higher displacement.
- **Destructive Interference**: Occurs when the waves are out of phase, leading to wave cancellation and lower displacement.

The interference pattern depends on the relative phase and position of the sources and the observation point.

---

## 2. Simulation and Visualization

### Steps to Implement:
1. **Choose a Regular Polygon**: For simplicity, we will use a square (4 vertices).
2. **Position the Sources**: The point sources are placed at the vertices of the square.
3. **Write the Wave Equations**: For each source, the wave will follow the equation described above.
4. **Apply Superposition**: Sum the contributions from all sources at each point on the water surface.
5. **Analyze the Resulting Pattern**: Observe regions of constructive and destructive interference.

---

## 3. Python Implementation

Below is a Python script that simulates the interference pattern of waves emitted from the vertices of a square (or any regular polygon). It uses the **matplotlib** library for visualization and **numpy** for numerical calculations.

```python
import numpy as np
import matplotlib.pyplot as plt

# Constants
A = 1        # Amplitude of the waves
k = 2 * np.pi / 1.0  # Wave number (assuming wavelength = 1 meter)
omega = 2 * np.pi  # Angular frequency (assuming frequency = 1 Hz)
phi = 0      # Initial phase of the waves

# Set up the grid for the water surface
x_max, y_max = 10, 10  # Size of the water surface grid (10m x 10m)
x = np.linspace(-x_max, x_max, 500)
y = np.linspace(-y_max, y_max, 500)
X, Y = np.meshgrid(x, y)

# Define the number of sources and their positions for a square
N_sources = 4  # Number of sources (vertices of a square)
radius = 5     # Distance from the center to the sources

# Positions of the sources (vertices of a square)
angles = np.linspace(0, 2 * np.pi, N_sources, endpoint=False)
source_positions = np.array([radius * np.cos(angles), radius * np.sin(angles)])

# Superposition of waves from all sources
def wave_sum(X, Y, source_positions, A, k, omega, phi):
    total_displacement = np.zeros(X.shape)
    
    for i in range(N_sources):
        # Calculate distance from each source to each point on the grid
        r = np.sqrt((X - source_positions[0, i])**2 + (Y - source_positions[1, i])**2)
        
        # Calculate the wave displacement for this source
        displacement = A * np.cos(k * r - omega * 0 + phi)  # Assuming t = 0 for simplicity
        total_displacement += displacement  # Sum the displacements
    
    return total_displacement

# Calculate the wave displacement on the water surface
Z = wave_sum(X, Y, source_positions, A, k, omega, phi)

# Plotting the interference pattern
plt.figure(figsize=(8, 6))
plt.contourf(X, Y, Z, cmap='seismic', levels=np.linspace(-4, 4, 50))
plt.colorbar(label='Displacement')
plt.title('Interference Pattern of Waves from Square Sources')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.show()


YEPP
