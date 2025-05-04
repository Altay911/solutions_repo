Problem 3: Trajectories of a Freely Released Payload Near Earth
Analysis of Possible Trajectories
When a payload is released near Earth, its trajectory is determined by its initial velocity and position relative to Earth's gravitational field. The possible trajectories are:

Elliptical Orbit: If the payload's velocity is below escape velocity but sufficient to overcome atmospheric drag (at higher altitudes), it will enter an elliptical orbit around Earth.

Circular Orbit: A special case of elliptical orbit where the initial velocity is exactly perpendicular to the gravitational force at the right magnitude for a circular path.

Parabolic Trajectory: If the payload reaches exactly escape velocity, it will follow a parabolic path, theoretically never returning.

Hyperbolic Trajectory: For velocities exceeding escape velocity, the payload will follow a hyperbolic path and escape Earth's gravity.

Suborbital/Reentry: If the velocity is too low to maintain orbit, the payload will follow a suborbital trajectory and reenter Earth's atmosphere.

Key Physics Principles
Newton's Law of Gravitation:

F
=
G
m
1
m
2
r
2
F=G 
r 
2
 
m 
1
​
 m 
2
​
 
​
 
Governs the attractive force between Earth and the payload.

Kepler's Laws:

Orbits are conic sections (ellipses, parabolas, or hyperbolas).

Equal areas are swept in equal times (angular momentum conservation).

Orbital period squared is proportional to semi-major axis cubed (for closed orbits).

Escape Velocity:

v
escape
=
2
G
M
r
v 
escape
​
 = 
r
2GM
​
 
​
 
The minimum speed needed to break free from Earth's gravity.

Numerical Approach (Conceptual)
To simulate the payload's motion, we would numerically solve the equations of motion derived from Newton's laws:

Equations of Motion:

d
2
r
⃗
d
t
2
=
−
G
M
r
3
r
⃗
dt 
2
 
d 
2
  
r
 
​
 =− 
r 
3
 
GM
​
  
r
 
Where 
r
⃗
r
  is the position vector of the payload.

Numerical Integration:

Discretize time into small steps 
Δ
t
Δt.

Use methods like Euler or Runge-Kutta to update velocity and position iteratively:

v
⃗
n
+
1
=
v
⃗
n
+
a
⃗
n
Δ
t
,
r
⃗
n
+
1
=
r
⃗
n
+
v
⃗
n
Δ
t
v
  
n+1
​
 = 
v
  
n
​
 + 
a
  
n
​
 Δt, 
r
  
n+1
​
 = 
r
  
n
​
 + 
v
  
n
​
 Δt
where 
a
⃗
n
=
−
G
M
r
n
3
r
⃗
n
a
  
n
​
 =− 
r 
n
3
​
 
GM
​
  
r
  
n
​
 .

Initial Conditions:

Set initial altitude (
h
h), speed (
v
0
v 
0
​
 ), and flight path angle (
θ
θ) relative to local horizontal.

Convert to Cartesian coordinates for simulation:

r
⃗
0
=
(
R
E
+
h
,
0
)
,
v
⃗
0
=
(
v
0
cos
⁡
θ
,
v
0
sin
⁡
θ
)
r
  
0
​
 =(R 
E
​
 +h,0), 
v
  
0
​
 =(v 
0
​
 cosθ,v 
0
​
 sinθ)
where 
R
E
R 
E
​
  is Earth's radius.

Trajectory Scenarios
Orbital Insertion:

Initial 
v
0
v 
0
​
  close to circular orbit velocity (
v
circ
=
G
M
r
v 
circ
​
 = 
r
GM
​
 
​
 ) results in stable orbits.

Elliptical if 
v
0
≠
v
circ
v 
0
​
 

=v 
circ
​
  or 
θ
≠
0
θ

=0.

Reentry:

Suborbital velocities (
v
0
≪
v
circ
v 
0
​
 ≪v 
circ
​
 ) cause the payload to fall back to Earth.

Escape:

Hyperbolic trajectories occur when 
v
0
≥
v
escape
v 
0
​
 ≥v 
escape
​
 .

Deliverables Outline
Markdown Document:

Explanation of physics principles (gravity, Kepler's laws).

Discussion of trajectory types and conditions.

Pseudocode for numerical simulation (if implementing later).

Graphical Representations:

Sample plots (conceptual) of:

Elliptical vs. circular orbits.

Escape and reentry trajectories.

Effect of varying initial velocity/angle.

Applications:

Payload deployment in missions.

Reentry vehicle design.

Escape trajectories for interplanetary probes.

