# Equivalent Resistance using Graph Theory
# Author: Your Name
# Description: This script calculates the equivalent resistance of a circuit represented as a graph.

import networkx as nx

# -------------------------------
# Helper functions
# -------------------------------

def is_series(G, u, v):
    """
    Returns True if node u and v form a series connection (degree 2 and one edge between them).
    """
    return G.degree[u] == 2 and G.degree[v] == 2 and G.number_of_edges(u, v) == 1

def is_parallel(edges):
    """
    Checks if there are multiple edges between the same pair of nodes (parallel connection).
    """
    return len(edges) > 1

def reduce_series(G):
    """
    Detect and reduce series connections.
    """
    changed = False
    for node in list(G.nodes):
        if G.degree[node] == 2:
            neighbors = list(G.neighbors(node))
            if len(neighbors) == 2 and not G.has_edge(neighbors[0], neighbors[1]):
                r1 = G[node][neighbors[0]]["resistance"]
                r2 = G[node][neighbors[1]]["resistance"]
                G.add_edge(neighbors[0], neighbors[1], resistance=r1 + r2)
                G.remove_node(node)
                changed = True
                break
    return changed

def reduce_parallel(G):
    """
    Detect and reduce parallel connections.
    """
    changed = False
    for u, v in list(G.edges()):
        parallel_edges = [e for e in G.edges(u, data=True) if e[1] == v]
        if len(parallel_edges) > 1:
            total = sum(1 / e[2]["resistance"] for e in parallel_edges)
            G.remove_edges_from([(u, v) for _, _, _ in parallel_edges])
            G.add_edge(u, v, resistance=1 / total)
            changed = True
            break
    return changed

def simplify_circuit(G):
    """
    Iteratively reduce the graph until a single edge remains.
    """
    while True:
        if reduce_series(G):
            continue
        elif reduce_parallel(G):
            continue
        else:
            break
    return G

# -------------------------------
# Example 1: Series Circuit
# -------------------------------
G1 = nx.Graph()
G1.add_edge("A", "B", resistance=5)
G1.add_edge("B", "C", resistance=10)

simplify_circuit(G1)
print("\nExample 1: Series Circuit")
for u, v, data in G1.edges(data=True):
    print(f"Equivalent resistance between {u} and {v}: {data['resistance']} Ohms")

# -------------------------------
# Example 2: Parallel Circuit
# -------------------------------
G2 = nx.MultiGraph()
G2.add_edge("A", "B", resistance=4)
G2.add_edge("A", "B", resistance=6)

# Convert MultiGraph to Graph for compatibility
G2_simple = nx.Graph()
for u, v, data in G2.edges(data=True):
    if G2_simple.has_edge(u, v):
        r1 = G2_simple[u][v]['resistance']
        r2 = data['resistance']
        G2_simple[u][v]['resistance'] = 1 / (1 / r1 + 1 / r2)
    else:
        G2_simple.add_edge(u, v, resistance=data['resistance'])

print("\nExample 2: Parallel Circuit")
simplify_circuit(G2_simple)
for u, v, data in G2_simple.edges(data=True):
    print(f"Equivalent resistance between {u} and {v}: {data['resistance']:.2f} Ohms")

# -------------------------------
# Example 3: Nested Configuration
# -------------------------------
G3 = nx.Graph()
G3.add_edge("A", "B", resistance=3)
G3.add_edge("B", "C", resistance=6)
G3.add_edge("C", "D", resistance=3)
G3.add_edge("A", "D", resistance=6)

print("\nExample 3: Nested Configuration")
simplify_circuit(G3)
for u, v, data in G3.edges(data=True):
    print(f"Equivalent resistance between {u} and {v}: {data['resistance']:.2f} Ohms")

# -------------------------------
# Notes:
# -------------------------------
# - This implementation handles simple series and parallel reductions.
# - For more complex graph topologies with loops and bridges,
#   Kirchhoff's laws and matrix methods (like Laplacian) are more suitable.
# - Can be extended using DFS/BFS to detect subgraphs for reduction.