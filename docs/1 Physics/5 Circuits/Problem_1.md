function calculateEquivalentResistance(graph):
    while graph has more than 1 node:
        for each edge in graph:
            node1, node2 = edge
            if nodes node1 and node2 are in series:
                R1 = getResistance(node1, node2)
                R2 = getResistance(node2, getNeighbor(node2))
                R_eq = R1 + R2
                mergeNodes(node1, getNeighbor(node2), R_eq)
            else if nodes node1 and node2 are in parallel:
                R1 = getResistance(node1, node2)
                R2 = getResistance(node2, getNeighbor(node2))
                R_eq = 1 / (1/R1 + 1/R2)
                mergeNodes(node1, getNeighbor(node2), R_eq)
    return getFinalResistance(graph)

function getResistance(node1, node2):
    return resistance between node1 and node2

function getNeighbor(node):
    return a neighboring node of the given node

function mergeNodes(node1, node2, R_eq):
    create a new node by merging node1 and node2
    update the graph with new node and resistance R_eq
    remove original nodes and their resistances

function nodes node1 and node2 are in series:
    check if both nodes are connected with no branches in between

function nodes node1 and node2 are in parallel:
    check if both nodes share a common neighbor in the graph

function getFinalResistance(graph):
    return the resistance of the final simplified circuit
idk