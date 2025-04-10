# Problem 1

import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # gravitational acceleration (m/s^2)
v0 = 20   # initial velocity (m/s)
angles = np.linspace(0, 90, num=100)  # angles from 0 to 90 degrees

# Function to calculate range
def projectile_range(v0, theta, g=9.81):
    theta_rad = np.radians(theta)
    return (v0**2 * np.sin(2 * theta_rad)) / g

# Compute range for each angle
ranges = projectile_range(v0, angles)

# Plot range vs angle
plt.figure(figsize=(8, 5))
plt.plot(angles, ranges, label=f'v0 = {v0} m/s', color='b')
plt.xlabel("Angle of Projection (degrees)")
plt.ylabel("Range (m)")
plt.title("Projectile Range as a Function of Angle")
plt.legend()
plt.grid()
plt.show()

# Function to compute projectile motion trajectory
def projectile_trajectory(v0, theta, g=9.81):
    theta_rad = np.radians(theta)
    t_flight = (2 * v0 * np.sin(theta_rad)) / g
    t = np.linspace(0, t_flight, num=100)
    x = v0 * np.cos(theta_rad) * t
    y = v0 * np.sin(theta_rad) * t - 0.5 * g * t**2
    return x, y

# Plot projectile motion for a few angles
plt.figure(figsize=(8, 5))
for theta in [15, 30, 45, 60, 75]:
    x, y = projectile_trajectory(v0, theta)
    plt.plot(x, y, label=f'{theta}°')

plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Distance (m)")
plt.title("Projectile Motion Trajectories")
plt.legend()
plt.grid()
plt.show()



# Discussion
print("The maximum range occurs at 45 degrees, as expected from the analytical solution.")

![download](https://github.com/user-attachments/assets/94ddaa11-82e6-40bd-9acf-74ff3bb98d0d)
![download](https://github.com/user-attachments/assets/97208085-cb8e-4816-84a3-a8cfc8cb7c23)
