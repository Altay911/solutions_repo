# --------------------------
# Equivalent Resistance using Graph Theory
# --------------------------

import networkx as nx

def is_series(G, u, v):
    return G.degree[u] == 2 and G.degree[v] == 2 and G.number_of_edges(u, v) == 1

def reduce_series(G):
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
    changed = False
    seen = set()
    for u, v in list(G.edges()):
        if (u, v) in seen or (v, u) in seen:
            continue
        parallel_edges = [e for e in G.edges(u, data=True) if e[1] == v]
        if len(parallel_edges) > 1:
            total = sum(1 / e[2]["resistance"] for e in parallel_edges)
            G.remove_edges_from([(u, v) for _, _, _ in parallel_edges])
            G.add_edge(u, v, resistance=1 / total)
            changed = True
            break
        seen.add((u, v))
    return changed

def simplify_circuit(G):
    while True:
        if reduce_series(G):
            continue
        elif reduce_parallel(G):
            continue
        else:
            break
    return G

# --------------------------
# EXAMPLES
# --------------------------

# Example 1: Series
G1 = nx.Graph()
G1.add_edge("A", "B", resistance=5)
G1.add_edge("B", "C", resistance=10)

print("Example 1: Series")
simplify_circuit(G1)
for u, v, data in G1.edges(data=True):
    print(f"Equivalent resistance between {u} and {v}: {data['resistance']} Ohms")

# Example 2: Parallel
G2 = nx.MultiGraph()
G2.add_edge("A", "B", resistance=4)
G2.add_edge("A", "B", resistance=6)

G2_simple = nx.Graph()
for u, v, data in G2.edges(data=True):
    if G2_simple.has_edge(u, v):
        r1 = G2_simple[u][v]['resistance']
        r2 = data['resistance']
        G2_simple[u][v]['resistance'] = 1 / (1 / r1 + 1 / r2)
    else:
        G2_simple.add_edge(u, v, resistance=data['resistance'])

print("\nExample 2: Parallel")
simplify_circuit(G2_simple)
for u, v, data in G2_simple.edges(data=True):
    print(f"Equivalent resistance between {u} and {v}: {data['resistance']:.2f} Ohms")

# Example 3: Nested
G3 = nx.Graph()
G3.add_edge("A", "B", resistance=3)
G3.add_edge("B", "C", resistance=6)
G3.add_edge("C", "D", resistance=3)
G3.add_edge("A", "D", resistance=6)

print("\nExample 3: Nested Configuration")
simplify_circuit(G3)
for u, v, data in G3.edges(data=True):
    print(f"Equivalent resistance between {u} and {v}: {data['resistance']:.2f} Ohms")
