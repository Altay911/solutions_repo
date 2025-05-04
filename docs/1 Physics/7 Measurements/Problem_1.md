<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pendulum Gravity Measurement</title>
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
    #pendulumCanvas {
      background: #fff;
    }
  </style>
</head>
<body>
  <h1>Measuring Earth's Gravitational Acceleration (<i>g</i>) with a Pendulum</h1>
  
  <div class="simulation">
    <h2>Procedure</h2>
    <h3>Materials</h3>
    <ul>
      <li>String (1–1.5 m)</li>
      <li>Small weight (e.g., keys, coin bag)</li>
      <li>Stopwatch (smartphone timer)</li>
      <li>Ruler (resolution: ±0.5 cm)</li>
    </ul>

    <h3>Setup</h3>
    <ol>
      <li>Attach weight to string and fix to a support.</li>
      <li>Measure pendulum length <i>L</i> (suspension point to center of mass).</li>
    </ol>

    <div class="controls">
      <div class="control-group">
        <label for="pendulumLength">Pendulum Length <i>L</i> (m):</label>
        <input type="number" id="pendulumLength" value="1.0" step="0.01" min="0.1">
        <label for="lengthUncertainty">Uncertainty Δ<i>L</i> (m):</label>
        <input type="number" id="lengthUncertainty" value="0.005" step="0.001" min="0">
      </div>
    </div>

    <canvas id="pendulumCanvas" width="400" height="300"></canvas>
    <button onclick="startPendulum()">Start Oscillations</button>
    <button onclick="stopPendulum()">Stop</button>
  </div>

  <div class="simulation">
    <h2>Data Collection</h2>
    <p>Measure time for 10 oscillations (<i>T<sub>10</sub></i>), repeat 10 times:</p>
    <div class="controls">
      <div class="control-group">
        <label for="timeInput">Time for 10 Oscillations (s):</label>
        <input type="number" id="timeInput" step="0.01" placeholder="Enter measured time">
        <button onclick="addTimeData()">Add Data</button>
      </div>
    </div>

    <table id="timeDataTable">
      <thead>
        <tr>
          <th>Trial</th>
          <th><i>T<sub>10</sub></i> (s)</th>
        </tr>
      </thead>
      <tbody></tbody>
    </table>

    <button onclick="calculateResults()">Calculate <i>g</i></button>
  </div>

  <div class="simulation">
    <h2>Results</h2>
    <div class="formula">
      <p>Period: <i>T</i> = <i>T<sub>10</sub></i>/10</p>
      <p>Gravity: <i>g</i> = 4π²<i>L</i>/<i>T</i>²</p>
      <p>Uncertainty: Δ<i>g</i> = <i>g</i> × √[(Δ<i>L</i>/<i>L</i>)² + (2Δ<i>T</i>/<i>T</i>)²]</p>
    </div>

    <div class="results">
      <p>Mean <i>T<sub>10</sub></i>: <span id="meanT10">—</span> ± <span id="deltaT10">—</span> s</p>
      <p>Period <i>T</i>: <span id="periodT">—</span> ± <span id="deltaT">—</span> s</p>
      <p>Calculated <i>g</i>: <span id="gValue">—</span> ± <span id="deltaG">—</span> m/s²</p>
      <p>Standard <i>g</i>: 9.81 m/s² | Error: <span id="errorG">—</span>%</p>
    </div>
  </div>

  <div class="simulation">
    <h2>Analysis</h2>
    <h3>Uncertainty Sources</h3>
    <ul>
      <li><strong>Δ<i>L</i></strong>: Ruler resolution (±0.5 cm).</li>
      <li><strong>Δ<i>T</i></strong>: Reaction time and stopwatch precision.</li>
    </ul>

    <h3>Discussion</h3>
    <p>Compare your result with 9.81 m/s². Key factors affecting accuracy:</p>
    <ul>
      <li>Air resistance (neglected in simple pendulum theory).</li>
      <li>Amplitude (should be <15° for simple harmonic motion).</li>
      <li>String mass and weight distribution.</li>
    </ul>
  </div>

  <script>
    // Pendulum Animation
    let pendulumInterval;
    const canvas = document.getElementById('pendulumCanvas');
    const ctx = canvas.getContext('2d');
    let angle = 0.2; // Small initial angle (<15°)
    let angularVelocity = 0;
    const damping = 0.995; // Simulate air resistance

    function drawPendulum() {
      const length = parseFloat(document.getElementById('pendulumLength').value) * 100;
      const pivotX = canvas.width / 2;
      const pivotY = 50;
      const bobX = pivotX + length * Math.sin(angle);
      const bobY = pivotY + length * Math.cos(angle);

      ctx.clearRect(0, 0, canvas.width, canvas.height);
      
      // Draw string
      ctx.beginPath();
      ctx.moveTo(pivotX, pivotY);
      ctx.lineTo(bobX, bobY);
      ctx.stroke();

      // Draw bob
      ctx.beginPath();
      ctx.arc(bobX, bobY, 15, 0, Math.PI * 2);
      ctx.fillStyle = '#3498db';
      ctx.fill();
    }

    function updatePendulum() {
      const L = parseFloat(document.getElementById('pendulumLength').value);
      const g = 9.81;
      const angularAcceleration = -g / L * Math.sin(angle);
      
      angularVelocity += angularAcceleration * 0.05;
      angularVelocity *= damping;
      angle += angularVelocity * 0.05;

      drawPendulum();
    }

    function startPendulum() {
      if (pendulumInterval) clearInterval(pendulumInterval);
      angle = 0.2;
      pendulumInterval = setInterval(updatePendulum, 20);
    }

    function stopPendulum() {
      clearInterval(pendulumInterval);
    }

    // Data Analysis
    const timeData = [];

    function addTimeData() {
      const time = parseFloat(document.getElementById('timeInput').value);
      if (isNaN(time)) return;

      timeData.push(time);
      updateTimeTable();
      document.getElementById('timeInput').value = '';
    }

    function updateTimeTable() {
      const tableBody = document.querySelector('#timeDataTable tbody');
      tableBody.innerHTML = '';
      timeData.forEach((time, index) => {
        const row = document.createElement('tr');
        row.innerHTML = `<td>${index + 1}</td><td>${time.toFixed(2)}</td>`;
        tableBody.appendChild(row);
      });
    }

    function calculateResults() {
      if (timeData.length === 0) return;

      const L = parseFloat(document.getElementById('pendulumLength').value);
      const deltaL = parseFloat(document.getElementById('lengthUncertainty').value);

      // Calculate mean and standard deviation of T10
      const meanT10 = timeData.reduce((sum, val) => sum + val, 0) / timeData.length;
      const stdT10 = Math.sqrt(timeData.reduce((sum, val) => sum + Math.pow(val - meanT10, 2), 0) / timeData.length);
      const deltaT10 = stdT10 / Math.sqrt(timeData.length);

      // Calculate period T and its uncertainty
      const T = meanT10 / 10;
      const deltaT = deltaT10 / 10;

      // Calculate g and its uncertainty
      const g = 4 * Math.PI ** 2 * L / T ** 2;
      const deltaG = g * Math.sqrt((deltaL / L) ** 2 + (2 * deltaT / T) ** 2);

      // Update results
      document.getElementById('meanT10').textContent = meanT10.toFixed(2);
      document.getElementById('deltaT10').textContent = deltaT10.toFixed(2);
      document.getElementById('periodT').textContent = T.toFixed(3);
      document.getElementById('deltaT').textContent = deltaT.toFixed(3);
      document.getElementById('gValue').textContent = g.toFixed(2);
      document.getElementById('deltaG').textContent = deltaG.toFixed(2);
      
      const error = Math.abs((g - 9.81) / 9.81 * 100);
      document.getElementById('errorG').textContent = error.toFixed(1);
    }

    // Initialize
    drawPendulum();
  </script>
</body>
</html>