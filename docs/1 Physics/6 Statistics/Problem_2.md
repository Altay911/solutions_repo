<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Monte Carlo π Estimation</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      max-width: 900px;
      margin: 0 auto;
      padding: 20px;
      background-color: #f5f5f5;
      color: #333;
    }
    h1, h2, h3 {
      color: #2c3e50;
    }
    .simulation {
      background: white;
      border-radius: 8px;
      padding: 20px;
      margin: 20px 0;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    canvas {
      background: #eee;
      display: block;
      margin: 10px auto;
      border: 1px solid #ccc;
    }
    .controls {
      display: flex;
      flex-wrap: wrap;
      gap: 15px;
      margin: 15px 0;
    }
    .control-group {
      flex: 1;
      min-width: 200px;
    }
    label {
      display: block;
      margin: 5px 0;
      font-weight: bold;
    }
    input, select {
      width: 100%;
      padding: 8px;
      margin-bottom: 10px;
      border: 1px solid #ddd;
      border-radius: 4px;
    }
    button {
      background: #3498db;
      color: white;
      border: none;
      padding: 10px 15px;
      border-radius: 4px;
      cursor: pointer;
      font-size: 16px;
    }
    button:hover {
      background: #2980b9;
    }
    .formula {
      background: #f8f9fa;
      padding: 10px;
      border-left: 4px solid #3498db;
      margin: 10px 0;
      font-family: monospace;
    }
    .results {
      font-weight: bold;
      color: #e74c3c;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      margin: 10px 0;
    }
    th, td {
      border: 1px solid #ddd;
      padding: 8px;
      text-align: left;
    }
    th {
      background-color: #f2f2f2;
    }
  </style>
</head>
<body>
  <h1>Estimating π Using Monte Carlo Methods</h1>
  
  <div class="simulation">
    <h2>Part 1: Circle-Based Method</h2>
    <h3>Theory</h3>
    <p>For a unit circle inside a 2×2 square:</p>
    <div class="formula">
      Area of circle = πr² = π (since r=1)<br>
      Area of square = 4<br>
      ⇒ π ≈ 4 × (points inside circle / total points)
    </div>
    <canvas id="circleCanvas" width="400" height="400"></canvas>
    <div class="controls">
      <div class="control-group">
        <label for="circlePoints">Number of Points:</label>
        <input type="number" id="circlePoints" value="1000" min="100" step="100">
      </div>
    </div>
    <button onclick="runCircleSimulation()">Run Simulation</button>
    <div class="results">
      Estimated π: <span id="piEstimate">—</span><br>
      Points inside: <span id="pointsInside">0</span>/<span id="totalPoints">0</span>
    </div>
  </div>

  <div class="simulation">
    <h2>Part 2: Buffon’s Needle Method</h2>
    <h3>Theory</h3>
    <p>For needles of length L and line spacing D:</p>
    <div class="formula">
      π ≈ (2 × L × total throws) / (D × number of crosses)
    </div>
    <canvas id="needleCanvas" width="400" height="200"></canvas>
    <div class="controls">
      <div class="control-group">
        <label for="needleThrows">Number of Throws:</label>
        <input type="number" id="needleThrows" value="100" min="10" step="10">
      </div>
      <div class="control-group">
        <label for="needleLength">Needle Length (L):</label>
        <input type="number" id="needleLength" value="1" step="0.1" min="0.1">
      </div>
      <div class="control-group">
        <label for="lineSpacing">Line Spacing (D):</label>
        <input type="number" id="lineSpacing" value="2" step="0.1" min="1">
      </div>
    </div>
    <button onclick="runNeedleSimulation()">Run Simulation</button>
    <div class="results">
      Estimated π: <span id="piNeedleEstimate">—</span><br>
      Crosses: <span id="needleCrosses">0</span>/<span id="needleThrowsCount">0</span>
    </div>
  </div>

  <h2>Analysis</h2>
  <h3>Convergence Comparison</h3>
  <table>
    <tr>
      <th>Method</th>
      <th>Convergence Rate</th>
      <th>Computational Cost</th>
    </tr>
    <tr>
      <td>Circle</td>
      <td>~1/√N (Slow)</td>
      <td>Low (O(N))</td>
    </tr>
    <tr>
      <td>Buffon’s Needle</td>
      <td>~1/√N (Slow)</td>
      <td>Medium (O(N))</td>
    </tr>
  </table>

  <script>
    // Circle-Based Method
    function runCircleSimulation() {
      const canvas = document.getElementById('circleCanvas');
      const ctx = canvas.getContext('2d');
      const nPoints = parseInt(document.getElementById('circlePoints').value);
      const center = canvas.width / 2;
      const radius = canvas.width / 2 - 10;

      // Draw square and circle
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.strokeStyle = '#000';
      ctx.strokeRect(10, 10, canvas.width - 20, canvas.height - 20);
      ctx.beginPath();
      ctx.arc(center, center, radius, 0, Math.PI * 2);
      ctx.stroke();

      let inside = 0;
      for (let i = 0; i < nPoints; i++) {
        const x = Math.random() * (canvas.width - 20) + 10;
        const y = Math.random() * (canvas.height - 20) + 10;
        const distance = Math.sqrt((x - center) ** 2 + (y - center) ** 2);

        if (distance <= radius) {
          ctx.fillStyle = 'red';
          inside++;
        } else {
          ctx.fillStyle = 'blue';
        }
        ctx.fillRect(x - 1, y - 1, 2, 2);
      }

      const piEstimate = 4 * (inside / nPoints);
      document.getElementById('piEstimate').textContent = piEstimate.toFixed(6);
      document.getElementById('pointsInside').textContent = inside;
      document.getElementById('totalPoints').textContent = nPoints;
    }

    // Buffon’s Needle Method
    function runNeedleSimulation() {
      const canvas = document.getElementById('needleCanvas');
      const ctx = canvas.getContext('2d');
      const nThrows = parseInt(document.getElementById('needleThrows').value);
      const L = parseFloat(document.getElementById('needleLength').value);
      const D = parseFloat(document.getElementById('lineSpacing').value);

      // Draw parallel lines
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.strokeStyle = '#000';
      for (let y = 20; y < canvas.height; y += D * 20) {
        ctx.beginPath();
        ctx.moveTo(0, y);
        ctx.lineTo(canvas.width, y);
        ctx.stroke();
      }

      let crosses = 0;
      for (let i = 0; i < nThrows; i++) {
        const x1 = Math.random() * canvas.width;
        const y1 = Math.random() * canvas.height;
        const angle = Math.random() * Math.PI;
        const x2 = x1 + L * 20 * Math.cos(angle);
        const y2 = y1 + L * 20 * Math.sin(angle);

        // Check for line crossings
        let crossed = false;
        for (let lineY = 20; lineY < canvas.height; lineY += D * 20) {
          if ((y1 < lineY && y2 >= lineY) || (y1 >= lineY && y2 < lineY)) {
            crossed = true;
            break;
          }
        }

        ctx.beginPath();
        ctx.moveTo(x1, y1);
        ctx.lineTo(x2, y2);
        ctx.strokeStyle = crossed ? 'red' : 'blue';
        ctx.stroke();

        if (crossed) crosses++;
      }

      const piEstimate = (2 * L * nThrows) / (D * crosses);
      document.getElementById('piNeedleEstimate').textContent = isFinite(piEstimate) ? piEstimate.toFixed(6) : "∞";
      document.getElementById('needleCrosses').textContent = crosses;
      document.getElementById('needleThrowsCount').textContent = nThrows;
    }
  </script>

  <h2>Key Observations</h2>
  <ul>
    <li><strong>Circle Method</strong>: Simple but requires many points for accuracy (10,000+ for 2 decimal places).</li>
    <li><strong>Buffon’s Needle</strong>: Geometric constraints (L ≤ D) improve efficiency but still slow convergence.</li>
    <li>Both methods demonstrate the "law of large numbers" in action.</li>
  </ul>
</body>
</html>