// Equivalent Resistance Calculation Using Graph Theory

// A function to calculate the equivalent resistance of a circuit graph
// where graph represents a network of resistors

// Example structure for graph: graph[node] = {neighbor1: resistance1, neighbor2: resistance2, ...}

function calculate_equivalent_resistance(graph) {
    // Step 1: Iterate over the graph while there is more than one node
    while (graph.size() > 1) {
        for (each pair of connected nodes (node1, node2)) {
            // Step 2: Check if the two resistors are in series
            if (is_series(graph, node1, node2)) {
                // Combine the resistors in series: R_eq = R1 + R2
                R_eq = graph[node1][node2] + graph[node2][node1];
                // Remove the pair and add the equivalent resistor
                remove_resistor(graph, node1, node2);
                add_resistor(graph, node1, node2, R_eq);
            }
            // Step 3: Check if the two resistors are in parallel
            else if (is_parallel(graph, node1, node2)) {
                // Combine the resistors in parallel: 1/R_eq = 1/R1 + 1/R2
                R_eq = 1 / (1 / graph[node1][node2] + 1 / graph[node2][node1]);
                // Remove the pair and add the equivalent resistor
                remove_resistor(graph, node1, node2);
                add_resistor(graph, node1, node2, R_eq);
            }
        }
    }

    // Step 4: Once reduced to one node, return the equivalent resistance
    return graph[remaining_node][remaining_node];
}

// Helper function to check if two resistors are in series
function is_series(graph, node1, node2) {
    // Resistors are in series if they are connected with no other junction
    return (graph[node1][node2] && graph[node2][node1]);
}

// Helper function to check if two resistors are in parallel
function is_parallel(graph, node1, node2) {
    // Resistors are in parallel if they are connected to the same pair of nodes
    return (graph[node1][node2] && graph[node2][node1]);
}

// Helper function to remove a resistor from the graph
function remove_resistor(graph, node1, node2) {
    delete graph[node1][node2];
    delete graph[node2][node1];
}

// Helper function to add a resistor to the graph
function add_resistor(graph, node1, node2, resistance) {
    graph[node1][node2] = resistance;
    graph[node2][node1] = resistance;
}
