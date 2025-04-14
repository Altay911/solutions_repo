function calculate_equivalent_resistance(graph):
    while number of nodes in graph > 1:
        for each edge in graph:
            node1, node2 = edge
            if is_series(node1, node2, graph):
                R1 = graph[node1][node2].resistance
                R2 = graph[node2][neighbors(node2)[0]].resistance
                R_eq = R1 + R2
                replace_series_connection(node1, neighbors(node2)[0], R_eq, graph)
            else if is_parallel(node1, node2, graph):
                R1 = graph[node1][node2].resistance
                R2 = graph[node2][neighbors(node2)[0]].resistance
                R_eq = 1 / (1/R1 + 1/R2)
                replace_parallel_connection(node1, neighbors(node2)[0], R_eq, graph)
    return graph[remaining_node].resistance

function is_series(node1, node2, graph):
    return len(neighbors(node1)) == 1 and len(neighbors(node2)) == 1

function is_parallel(node1, node2, graph):
    return common_neighbor_exists(node1, node2, graph)

function replace_series_connection(node1, node2, R_eq, graph):
    merge_nodes(node1, node2, R_eq, graph)
    remove_old_edges(node1, node2, graph)

function replace_parallel_connection(node1, node2, R_eq, graph):
    merge_nodes(node1, node2, R_eq, graph)
    remove_old_edges(node1, node2, graph)

function merge_nodes(node1, node2, R_eq, graph):
    new_node = combine(node1, node2)
    graph.add_node(new_node)
    graph.add_edge(node1, new_node, R_eq)
    graph.add_edge(new_node, neighbors(node2)[0], graph[node2][neighbors(node2)[0]].resistance)

function remove_old_edges(node1, node2, graph):
    graph.remove_edge(node1, node2)
    graph.remove_edge(node2, neighbors(node2)[0])

function common_neighbor_exists(node1, node2, graph):
    return exists(common neighbor between node1 and node2 in graph)
