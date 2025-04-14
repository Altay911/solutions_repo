class ResistanceCalculator {
    constructor() {
        this.resistors = [];
        this.nodes = new Set();
    }

    addResistor(node1, node2, resistance) {
        this.resistors.push({ node1, node2, resistance });
        this.nodes.add(node1);
        this.nodes.add(node2);
        this.updateCircuitDiagram();
    }

    reset() {
        this.resistors = [];
        this.nodes = new Set();
        this.updateCircuitDiagram();
        document.getElementById('result').innerHTML = '';
    }

    calculateEquivalentResistance(startNode, endNode) {
        // Simple series-parallel calculation for demonstration
        // In a real app, you would implement proper graph algorithms
        
        // Check if nodes exist
        if (!this.nodes.has(startNode) || !this.nodes.has(endNode)) {
            return "Error: One or both nodes don't exist in the circuit";
        }

        // Get all resistors between the two nodes (simple parallel case)
        const directResistors = this.resistors.filter(r => 
            (r.node1 === startNode && r.node2 === endNode) || 
            (r.node1 === endNode && r.node2 === startNode)
        );

        // Get all paths between nodes (simple series case)
        const paths = this.findPaths(startNode, endNode);

        if (directResistors.length > 0) {
            // Parallel resistors
            const equivalent = this.calculateParallel(directResistors.map(r => r.resistance));
            return `Equivalent resistance between ${startNode} and ${endNode}: <strong>${equivalent.toFixed(2)} Ω</strong> (parallel)`;
        } else if (paths.length > 0) {
            // Series resistors (just take first path for demo)
            const path = paths[0];
            let total = 0;
            for (let i = 0; i < path.length - 1; i++) {
                const node1 = path[i];
                const node2 = path[i + 1];
                const resistor = this.resistors.find(r => 
                    (r.node1 === node1 && r.node2 === node2) || 
                    (r.node1 === node2 && r.node2 === node1)
                );
                if (resistor) {
                    total += resistor.resistance;
                }
            }
            return `Equivalent resistance between ${startNode} and ${endNode}: <strong>${total.toFixed(2)} Ω</strong> (series)`;
        } else {
            return "No connection found between the specified nodes";
        }
    }

    findPaths(startNode, endNode) {
        // Simplified path finding for demonstration
        const paths = [];
        const visited = new Set();
        
        const dfs = (current, path) => {
            if (current === endNode) {
                paths.push([...path]);
                return;
            }
            
            visited.add(current);
            
            for (const resistor of this.resistors) {
                if (resistor.node1 === current && !visited.has(resistor.node2)) {
                    path.push(resistor.node2);
                    dfs(resistor.node2, path);
                    path.pop();
                } else if (resistor.node2 === current && !visited.has(resistor.node1)) {
                    path.push(resistor.node1);
                    dfs(resistor.node1, path);
                    path.pop();
                }
            }
            
            visited.delete(current);
        };
        
        dfs(startNode, [startNode]);
        return paths;
    }

    calculateParallel(resistances) {
        if (resistances.length === 0) return 0;
        const invSum = resistances.reduce((sum, r) => sum + 1 / r, 0);
        return 1 / invSum;
    }

    updateCircuitDiagram() {
        const diagram = document.getElementById('circuit-diagram');
        diagram.innerHTML = '';

        if (this.resistors.length === 0) {
            diagram.innerHTML = '<p>No resistors added yet</p>';
            return;
        }

        // Group resistors by connection
        const connections = {};
        this.resistors.forEach(resistor => {
            const key = [resistor.node1, resistor.node2].sort().join('-');
            if (!connections[key]) {
                connections[key] = [];
            }
            connections[key].push(resistor);
        });

        // Display each connection
        for (const key in connections) {
            const [node1, node2] = key.split('-');
            const resistors = connections[key];
            
            const connectionDiv = document.createElement('div');
            connectionDiv.style.margin = '10px 0';
            
            // Display node
            const node1Span = document.createElement('span');
            node1Span.className = 'node';
            node1Span.textContent = node1;
            connectionDiv.appendChild(node1Span);
            
            // Display resistor(s)
            if (resistors.length === 1) {
                const resistorSpan = document.createElement('span');
                resistorSpan.className = 'resistor';
                resistorSpan.textContent = `${resistors[0].resistance}Ω`;
                resistorSpan.title = `${node1}-${node2}: ${resistors[0].resistance}Ω`;
                connectionDiv.appendChild(resistorSpan);
            } else {
                const parallelDiv = document.createElement('div');
                parallelDiv.style.display = 'inline-block';
                parallelDiv.style.margin = '0 10px';
                parallelDiv.style.borderLeft = '2px solid #999';
                parallelDiv.style.borderRight = '2px solid #999';
                parallelDiv.style.padding = '0 10px';
                
                resistors.forEach(resistor => {
                    const resistorSpan = document.createElement('div');
                    resistorSpan.className = 'resistor';
                    resistorSpan.textContent = `${resistor.resistance}Ω`;
                    resistorSpan.title = `${node1}-${node2}: ${resistor.resistance}Ω`;
                    parallelDiv.appendChild(resistorSpan);
                });
                
                connectionDiv.appendChild(parallelDiv);
            }
            
            // Display node
            const node2Span = document.createElement('span');
            node2Span.className = 'node';
            node2Span.textContent = node2;
            connectionDiv.appendChild(node2Span);
            
            diagram.appendChild(connectionDiv);
        }
    }
}

// Initialize calculator
const calculator = new ResistanceCalculator();

// Set up event listeners
document.getElementById('addResistor').addEventListener('click', () => {
    const node1 = document.getElementById('node1').value.trim() || 'A';
    const node2 = document.getElementById('node2').value.trim() || 'B';
    const resistance = parseFloat(document.getElementById('resistance').value) || 100;
    
    calculator.addResistor(node1, node2, resistance);
    
    // Clear inputs
    document.getElementById('node1').value = '';
    document.getElementById('node2').value = '';
    document.getElementById('resistance').value = '';
    document.getElementById('node1').focus();
});

document.getElementById('calculate').addEventListener('click', () => {
    const startNode = document.getElementById('startNode').value.trim();
    const endNode = document.getElementById('endNode').value.trim();
    
    if (!startNode || !endNode) {
        alert('Please enter both start and end nodes');
        return;
    }
    
    const result = calculator.calculateEquivalentResistance(startNode, endNode);
    document.getElementById('result').innerHTML = result;
});

document.getElementById('reset').addEventListener('click', () => {
    calculator.reset();
});

// Initialize with an example circuit
calculator.addResistor('A', 'B', 10);
calculator.addResistor('B', 'C', 20);
calculator.addResistor('A', 'C', 30);