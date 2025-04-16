# Equivalent Resistance Using Graph Theory

## Motivation
Calculating the equivalent resistance is a fundamental problem in electrical circuits, essential for understanding and designing efficient systems. Traditional methods, such as iteratively applying series and parallel resistor rules, can become cumbersome when dealing with complex circuits with many components. Graph theory offers a powerful alternative, allowing for a more structured and algorithmic approach to analyzing circuits.

In this approach, the circuit is represented as a graph where:
- **Nodes** correspond to junctions or connection points in the circuit.
- **Edges** represent resistors with weights equal to their resistance values.

This method simplifies even intricate networks and enables automated analysis, which is especially useful in modern applications like circuit simulation, optimization problems, and network design.

## Task Overview

The task at hand is to calculate the **equivalent resistance** of a circuit using graph theory, focusing on the following:

1. **Option 1: Simplified Task – Algorithm Description**
   - We will describe the algorithm for calculating the equivalent resistance using graph theory.
   - Provide pseudocode for the algorithm that:
     - Identifies series and parallel connections.
     - Iteratively reduces the graph until a single equivalent resistance is obtained.
     - Handles nested combinations and ensures that the graph is simplified properly.

2. **Option 2: Advanced Task – Full Implementation** 
   - Implement the algorithm to handle arbitrary resistor configurations, including nested series and parallel connections.
   - Test the implementation on examples like simple series and parallel combinations, nested configurations, and complex graphs with multiple cycles.

---

## Option 1: Simplified Task – Algorithm Description

### Step-by-Step Explanation

1. **Input Representation**:
   - A circuit is represented as a graph \( G(V, E) \), where:
     - \( V \) is the set of vertices (nodes representing junctions).
     - \( E \) is the set of edges (resistors) with weights corresponding to their resistance values.

2. **Identifying Series and Parallel Connections**:
   - **Series Connection**: If two resistors are connected end-to-end (i.e., the two nodes are directly connected without any branching in between), their resistances simply add up. Mathematically:
     \[
     R_{\text{eq}} = R_1 + R_2
     \]
   - **Parallel Connection**: If two resistors are connected in parallel (i.e., both ends of the resistors are connected to the same two nodes), their equivalent resistance is calculated using the formula:
     \[
     \frac{1}{R_{\text{eq}}} = \frac{1}{R_1} + \frac{1}{R_2}
     \]

3. **Graph Reduction Algorithm**:
   - **Detecting Series Connections**: Traverse the graph and identify linear chains of resistors. These can be reduced by summing their resistance values.
   - **Detecting Parallel Connections**: Identify resistors that share the same pair of nodes. Apply the parallel resistance formula to reduce them to a single equivalent resistor.

4. **Handling Nested Combinations**:
   - After reducing series or parallel combinations, the graph may still contain nested combinations. The algorithm should recursively simplify the graph, reducing it step-by-step until only a single equivalent resistance remains.

5. **Termination**:
   - The algorithm continues until the entire graph is reduced to a single node representing the total equivalent resistance.

### Pseudocode

```plaintext
function calculateEquivalentResistance(graph):
    while graph has more than one node:
        for each edge (u, v) in graph:
            if u and v are in series:
                R_series = sum of resistances along the chain
                reduce the edge (u, v) to R_series
            else if u and v are in parallel:
                R_parallel = 1 / (1/R_u + 1/R_v)
                replace the edge (u, v) with R_parallel

    return the resistance value of the final reduced graph
s