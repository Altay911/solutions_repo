<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Circuit Resistance Calculator</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>Equivalent Resistance Calculator</h1>
        
        <div class="controls">
            <div class="input-group">
                <label for="node1">Node 1:</label>
                <input type="text" id="node1" placeholder="A">
            </div>
            
            <div class="input-group">
                <label for="node2">Node 2:</label>
                <input type="text" id="node2" placeholder="B">
            </div>
            
            <div class="input-group">
                <label for="resistance">Resistance (Ω):</label>
                <input type="number" id="resistance" placeholder="100" step="0.1" min="0">
            </div>
            
            <button id="addResistor">Add Resistor</button>
            <button id="calculate">Calculate Equivalent Resistance</button>
            <button id="reset">Reset Circuit</button>
        </div>
        
        <div class="visualization">
            <div id="circuit-diagram"></div>
            <div id="result"></div>
        </div>
        
        <div class="instructions">
            <h3>How to use:</h3>
            <ol>
                <li>Enter two node names and a resistance value</li>
                <li>Click "Add Resistor" to add to the circuit</li>
                <li>Repeat until your circuit is complete</li>
                <li>Enter start and end nodes below</li>
                <li>Click "Calculate Equivalent Resistance"</li>
            </ol>
            
            <div class="end-nodes">
                <div class="input-group">
                    <label for="startNode">Start Node:</label>
                    <input type="text" id="startNode" placeholder="A">
                </div>
                
                <div class="input-group">
                    <label for="endNode">End Node:</label>
                    <input type="text" id="endNode" placeholder="B">
                </div>
            </div>
        </div>
    </div>
    
    <script src="script.js"></script>
</body>
</html>