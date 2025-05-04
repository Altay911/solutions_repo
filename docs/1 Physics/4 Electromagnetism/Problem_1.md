<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lorentz Force Simulator</title>
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
  </style>
</head>
<body>
  <h1>Lorentz Force Particle Simulator</h1>
  
  <div class="simulation">
    <h2>1. Uniform Magnetic Field (Circular Motion)</h2>
    <p>Particle moves in a circle when <strong>v ⊥ B</strong>:</p>
    <div class="formula">
      F = q(v × B) ⇒ r = mv/(qB) (Larmor radius)
    </div>
    <canvas id="uniformB" width="500" height="300"></canvas>
    <div class="controls">
      <div class="control-group">
        <label for="charge">Charge (q):</label>
        <input type="number" id="charge" value="-1" step="0.1">
      </div>
      <div class="control-group">
        <label for="mass">Mass (m):</label>
        <input type="number" id="mass" value="1" step="0.1">
      </div>
      <div class="control-group">
        <label for="bField">B-field (B):</label>
        <input type="number" id="bField" value="1" step="0.1">
      </div>
    </div>
    <button onclick="startUniformBSimulation()">Start Simulation</button>
  </div>

  <div class="simulation">
    <h2>2. Crossed E and B Fields (Drift Motion)</h2>
    <p>Particle drifts with velocity <strong>E × B/B²</strong>:</p>
    <div class="formula">
      v<sub>drift</sub> = (E × B) / B²
    </div>
    <canvas id="crossedFields" width="500" height="300"></canvas>
    <div class="controls">
      <div class="control-group">
        <label for="eField">E-field (E):</label>
        <input type="number" id="eField" value="0.5" step="0.1">
      </div>
      <div class="control-group">
        <label for="bFieldCrossed">B-field (B):</label>
        <input type="number" id="bFieldCrossed" value="1" step="0.1">
      </div>
    </div>
    <button onclick="startCrossedFieldsSimulation()">Start Simulation</button>
  </div>

  <div class="simulation">
    <h2>3. Combined E and B Fields (Complex Motion)</h2>
    <p>Particle follows helical/spiral paths:</p>
    <div class="formula">
      F = q(E + v × B)
    </div>
    <canvas id="combinedFields" width="500" height="300"></canvas>
    <div class="controls">
      <div class="control-group">
        <label for="eFieldCombined">E-field (E):</label>
        <input type="number" id="eFieldCombined" value="0.2" step="0.1">
      </div>
      <div class="control-group">
        <label for="bFieldCombined">B-field (B):</label>
        <input type="number" id="bFieldCombined" value="0.5" step="0.1">
      </div>
    </div>
    <button onclick="startCombinedFieldsSimulation()">Start Simulation</button>
  </div>

  <h2>Physics Explained</h2>
  <h3>Key Concepts</h3>
  <ul>
    <li><strong>Larmor Radius (r)</strong>: Radius of circular motion in B-field. Depends on m, v, q, B.</li>
    <li><strong>Drift Velocity</strong>: In crossed fields, particles drift perpendicular to both E and B.</li>
    <li><strong>Helical Motion</strong>: If v has components both parallel and perpendicular to B.</li>
  </ul>

  <h3>Applications</h3>
  <ul>
    <li><strong>Cyclotrons</strong>: Use uniform B-fields to accelerate particles.</li>
    <li><strong>Mass Spectrometers</strong>: Separate ions by q/m ratio using r ∝ m/q.</li>
  </ul>

  <script>
    // Uniform B-field simulation
    function startUniformBSimulation() {
      const canvas = document.getElementById('uniformB');
      const ctx = canvas.getContext('2d');
      const charge = parseFloat(document.getElementById('charge').value);
      const mass = parseFloat(document.getElementById('mass').value);
      const bField = parseFloat(document.getElementById('bField').value);

      let x = 100, y = 150, vx = 3 * Math.abs(charge), vy = 0;
      const radius = Math.abs((mass * vx) / (charge * bField)) * 10;

      ctx.clearRect(0, 0, canvas.width, canvas.height);
      
      function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // Draw B-field direction (into the screen)
        ctx.fillStyle = 'blue';
        ctx.fillText('B (into screen)', 20, 20);
        
        // Draw particle
        ctx.beginPath();
        ctx.arc(x, y, 5, 0, Math.PI * 2);
        ctx.fillStyle = charge < 0 ? 'red' : 'blue';
        ctx.fill();
        
        // Update position (circular motion)
        x = 250 + radius * Math.cos(Date.now() * 0.005 * (Math.abs(charge * bField) / mass));
        y = 150 + radius * Math.sin(Date.now() * 0.005 * (Math.abs(charge * bField) / mass));
        
        requestAnimationFrame(animate);
      }
      animate();
    }

    // Crossed E and B fields simulation
    function startCrossedFieldsSimulation() {
      const canvas = document.getElementById('crossedFields');
      const ctx = canvas.getContext('2d');
      const eField = parseFloat(document.getElementById('eField').value);
      const bField = parseFloat(document.getElementById('bFieldCrossed').value);

      let x = 50, y = 150;
      const driftVelocity = (eField / bField) * 10;

      ctx.clearRect(0, 0, canvas.width, canvas.height);
      
      function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // Draw E and B fields
        ctx.fillStyle = 'blue';
        ctx.fillText(`E (→): ${eField}`, 20, 20);
        ctx.fillText(`B (into screen): ${bField}`, 20, 40);
        
        // Draw particle
        ctx.beginPath();
        ctx.arc(x, y, 5, 0, Math.PI * 2);
        ctx.fillStyle = 'green';
        ctx.fill();
        
        // Update position (drift + circular)
        x += driftVelocity * 0.05;
        if (x > canvas.width) x = 0;
        y = 150 + 30 * Math.sin(Date.now() * 0.005 * bField);
        
        requestAnimationFrame(animate);
      }
      animate();
    }

    // Combined E and B fields simulation
    function startCombinedFieldsSimulation() {
      const canvas = document.getElementById('combinedFields');
      const ctx = canvas.getContext('2d');
      const eField = parseFloat(document.getElementById('eFieldCombined').value);
      const bField = parseFloat(document.getElementById('bFieldCombined').value);

      let x = 50, y = 150, z = 0;
      const driftVelocity = (eField / bField) * 5;

      ctx.clearRect(0, 0, canvas.width, canvas.height);
      
      function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // Draw particle (projected to 2D)
        ctx.beginPath();
        ctx.arc(x, y, 5, 0, Math.PI * 2);
        ctx.fillStyle = 'purple';
        ctx.fill();
        
        // Update position (complex motion)
        x += driftVelocity * 0.03;
        y = 150 + 40 * Math.sin(Date.now() * 0.003 * bField);
        if (x > canvas.width) x = 0;
        
        requestAnimationFrame(animate);
      }
      animate();
    }
  </script>
</body>
</html>