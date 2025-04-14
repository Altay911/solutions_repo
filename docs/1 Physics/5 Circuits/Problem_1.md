import networkx as nx
from collections import defaultdict

class CircuitAnalyzer:
    def __init__(self):
        self.graph = nx.Graph()
    
    def add_resistor(self, node1, node2, resistance):
        """Add a resistor between two nodes with given resistance"""
        self.graph.add_edge(node1, node2, resistance=resistance)
    
    def calculate_equivalent_resistance(self, start_node, end_node):
        """
        Calculate equivalent resistance between two nodes using series-parallel reduction
        Returns the equivalent resistance or None if nodes are disconnected
        """
        working_graph = self.graph.copy()
        
        while True:
            # Check if we've simplified to a single resistor
            if working_graph.number_of_edges() == 1:
                if start_node in working_graph and end_node in working_graph:
                    return working_graph.edges[start_node, end_node]['resistance']
                else:
                    return None  # Nodes are disconnected
            
            # Try series reduction first
            reduced = self._reduce_series(working_graph, start_node, end_node)
            if reduced:
                working_graph = reduced
                continue
            
            # Then try parallel reduction
            reduced = self._reduce_parallel(working_graph)
            if reduced:
                working_graph = reduced
                continue
            
            # If no more reductions possible but still multiple edges
            if working_graph.number_of_edges() > 1:
                print("Warning: Circuit contains non-series-parallel components")
                return None
            
            break
        
        # Final check for direct connection
        if working_graph.has_edge(start_node, end_node):
            return working_graph.edges[start_node, end_node]['resistance']
        return None
    
    def _reduce_series(self, graph, start_node, end_node):
        """
        Reduce series resistors in the graph
        Returns a new simplified graph or None if no series reductions found
        """
        # Find nodes with degree 2 (excluding start and end nodes)
        series_nodes = [
            node for node in graph.nodes()
            if (node != start_node and node != end_node and 
                graph.degree(node) == 2)
        ]
        
        if not series_nodes:
            return None
        
        # Create a copy to modify
        new_graph = graph.copy()
        
        for node in series_nodes:
            # Get the two neighbors
            neighbors = list(new_graph.neighbors(node))
            if len(neighbors) != 2:
                continue
                
            a, b = neighbors
            
            # Calculate combined resistance
            r1 = new_graph.edges[node, a]['resistance']
            r2 = new_graph.edges[node, b]['resistance']
            total = r1 + r2
            
            # Remove the series node and add new resistor
            new_graph.remove_node(node)
            new_graph.add_edge(a, b, resistance=total)
            
            # Only reduce one series at a time to avoid complications
            return new_graph
        
        return None
    
    def _reduce_parallel(self, graph):
        """
        Reduce parallel resistors in the graph
        Returns a new simplified graph or None if no parallel reductions found
        """
        # Find all pairs with multiple edges
        parallel_edges = defaultdict(list)
        for u, v in graph.edges():
            if u > v:  # To avoid duplicate (u,v) and (v,u)
                u, v = v, u
            parallel_edges[(u, v)].append((u, v))
        
        # Find pairs with multiple edges between them
        parallel_pairs = [pair for pair, edges in parallel_edges.items() 
                         if len(edges) > 1]
        
        if not parallel_pairs:
            return None
        
        # Create a copy to modify
        new_graph = graph.copy()
        
        for u, v in parallel_pairs[:1]:  # Only process one pair at a time
            # Get all resistances between u and v
            resistances = []
            for edge in graph.edges(u, data=True):
                if edge[1] == v:
                    resistances.append(edge[2]['resistance'])
            
            # Calculate equivalent parallel resistance
            if len(resistances) > 1:
                inv_total = sum(1/r for r in resistances)
                if inv_total == 0:
                    equivalent = 0  # Short circuit case
                else:
                    equivalent = 1 / inv_total
                
                # Remove all parallel edges and add one equivalent
                new_graph.remove_edges_from(list(graph.edges(u, v)))
                new_graph.add_edge(u, v, resistance=equivalent)
                
                return new_graph
        
        return None


def test_circuits():
    """Test the implementation with example circuits"""
    print("Testing equivalent resistance calculator...\n")
    
    # Example 1: Simple series circuit
    print("Example 1: Simple series circuit (R1 + R2)")
    analyzer = CircuitAnalyzer()
    analyzer.add_resistor('A', 'B', 10)  # R1 = 10Ω
    analyzer.add_resistor('B', 'C', 20)  # R2 = 20Ω
    equivalent = analyzer.calculate_equivalent_resistance('A', 'C')
    print(f"Equivalent resistance between A and C: {equivalent} Ω (Expected: 30 Ω)\n")
    
    # Example 2: Simple parallel circuit
    print("Example 2: Simple parallel circuit (R1 || R2)")
    analyzer = CircuitAnalyzer()
    analyzer.add_resistor('A', 'B', 10)  # R1 = 10Ω
    analyzer.add_resistor('A', 'B', 20)  # R2 = 20Ω
    equivalent = analyzer.calculate_equivalent_resistance('A', 'B')
    print(f"Equivalent resistance between A and B: {equivalent:.2f} Ω (Expected: 6.67 Ω)\n")
    
    # Example 3: Nested series-parallel circuit
    print("Example 3: Nested series-parallel circuit")
    analyzer = CircuitAnalyzer()
    analyzer.add_resistor('A', 'B', 10)  # R1 = 10Ω
    analyzer.add_resistor('B', 'C', 20)  # R2 = 20Ω
    analyzer.add_resistor('B', 'C', 30)  # R3 = 30Ω (parallel with R2)
    analyzer.add_resistor('C', 'D', 40)  # R4 = 40Ω
    equivalent = analyzer.calculate_equivalent_resistance('A', 'D')
    print(f"Equivalent resistance between A and D: {equivalent:.2f} Ω (Expected: 62.00 Ω)\n")


if __name__ == "__main__":
    test_circuits()