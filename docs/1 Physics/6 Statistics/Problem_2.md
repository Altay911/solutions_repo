# Estimating Pi using Monte Carlo Methods

## Motivation
Monte Carlo simulations are a powerful class of computational techniques that use randomness to solve problems or estimate values. One of the most elegant applications of Monte Carlo methods is estimating the value of Pi through geometric probability. By randomly generating points and analyzing their positions relative to a geometric shape, we can approximate Pi in an intuitive and visually engaging way.

This problem connects fundamental concepts of probability, geometry, and numerical computation. It also provides a gateway to understanding how randomness can be harnessed to solve complex problems in physics, finance, and computer science. The Monte Carlo approach to Pi estimation highlights the versatility and simplicity of this method while offering practical insights into convergence rates and computational efficiency.

## Task Overview

### Part 1: Estimating Pi Using a Circle

#### 1. Theoretical Foundation:
Explain how the ratio of points inside a circle to the total number of points in a square can be used to estimate Pi. Derive the formula for Pi based on a unit circle.

#### 2. Simulation:
- Generate random points in a 2D square bounding a unit circle.
- Count the number of points falling inside the circle.
- Estimate Pi based on the ratio of points inside the circle to the total points.

#### 3. Visualization:
Create a plot showing the randomly generated points, distinguishing those inside and outside the circle.

#### 4. Analysis:
- Investigate how the accuracy of the estimate improves as the number of points increases.
- Discuss the convergence rate and computational considerations for this method.

### Part 2: Estimating Pi Using Buffon’s Needle

#### 1. Theoretical Foundation:
- Describe Buffon’s Needle problem, where Pi can be estimated based on the probability of a needle crossing parallel lines on a plane.
- Derive the formula for Pi using this method.

#### 2. Simulation:
- Simulate the random dropping of a needle on a plane with parallel lines.
- Count the number of times the needle crosses a line.
- Estimate Pi based on the derived formula.

#### 3. Visualization:
Create a graphical representation of the simulation, showing the needle positions relative to the lines.

#### 4. Analysis:
- Explore how the number of needle drops affects the estimate’s accuracy.
- Compare the convergence rate of this method to the circle-based approach.

## Deliverables:
1. A Markdown document with:
   - Clear explanations of the methods and formulas.
   - A discussion of theoretical foundations and results.
   
2. Python scripts or notebooks implementing the simulations, including:
   - Code for the circle-based Monte Carlo method.
   - Code for Buffon’s Needle method.

3. Graphical outputs:
   - Plots showing random points for the circle-based method.
   - Visualizations of needle positions for Buffon’s Needle.

4. Analysis:
   - Tables or graphs showing the convergence of estimated Pi as a function of the number of iterations for both methods.
   - A comparison of the methods in terms of accuracy and computational efficiency.

## Hints and Resources:
- Use Python libraries such as **NumPy** for random number generation and **Matplotlib** for visualizations.
- For the circle-based method, ensure the random points are uniformly distributed within the square.
- For Buffon’s Needle, pay attention to geometric constraints, such as the relationship between the needle length and the distance between lines.
- Start with a small number of iterations to validate the implementation, then increase the sample size to observe convergence.
