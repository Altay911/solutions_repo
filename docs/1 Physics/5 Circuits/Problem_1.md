# Problem 1

import networkx as nx
import numpy as np

# Function to calculate the equivalent resistance for series connection
def series_resistance(resistances):
    return sum(resistances)

# Function to calculate the equivalent resistance for parallel connection
def parallel_resistance(resistances):
    return 1 / sum(1 / np.array(resistances))

# Function to simplify the circuit graph by reducing series and parallel combinations
def simplify_graph(circuit_graph):
    for node1, node2, data in list(circuit_graph.edges(data=True)):
        resistance = data['resistance']
        # Check if the two nodes are in series or parallel and simplify accordingly
        if circuit_graph.has_edge(node1, node2):
            # Simplify the series or parallel connection
            pass  # Logic to simplify series or parallel connections

    return circuit_graph

# Main function to calculate the equivalent resistance of the circuit
def calculate_equivalent_resistance(circuit_graph):
    while len(circuit_graph.nodes) > 1:
        circuit_graph = simplify_graph(circuit_graph)
    
    return circuit_graph

# Example: Build a sample circuit graph with resistors between nodes
G = nx.Graph()

# Add edges representing resistors between nodes
G.add_edge('A', 'B', resistance=10)  # Resistor of 10 Ohms between A and B
G.add_edge('B', 'C', resistance=5)   # Resistor of 5 Ohms between B and C
G.add_edge('C', 'D', resistance=10)  # Resistor of 10 Ohms between C and D

# Calculate equivalent resistance
equivalent_resistance = calculate_equivalent_resistance(G)
print(f"Equivalent Resistance: {equivalent_resistance} Ohms")
