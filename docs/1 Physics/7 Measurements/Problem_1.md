
# Exploring the Central Limit Theorem through Simulations


### Introduction

The Central Limit Theorem (CLT) is a foundational concept in statistics, stating that the distribution of the sample mean will approximate a normal distribution as the sample size grows, regardless of the shape of the population distribution. This property allows statisticians to make inferences about population parameters using sample data, even when the population distribution is unknown or non-normal. This analysis examines the CLT through simulations, focusing on how sampling distributions evolve with different population distributions and sample sizes.

### Simulation Setup

To explore the CLT, simulations were conducted using three distinct population distributions:
- **Uniform Distribution**: A symmetric distribution with values ranging from 0 to 10.
- **Exponential Distribution**: A right-skewed distribution with a rate parameter of 1, often used to model waiting times.
- **Binomial Distribution**: A discrete distribution representing the number of successes in 100 trials with a success probability of 0.5.

The methodology involves:
1. Generating a population of 10,000 samples for each distribution.
2. Drawing random samples of sizes 5, 10, 30, and 50 from each population.
3. Repeating the sampling process 1,000 times to construct the sampling distribution of the sample mean.
4. Analyzing how these sampling distributions change with sample size and comparing them to the expected normal distribution.

### Analysis of Sampling Distributions

#### Uniform Distribution
The uniform population has a theoretical mean of 5 and a standard deviation of approximately 2.89. With a small sample size of 5, the sampling distribution of the mean shows slight deviations from normality but maintains symmetry due to the uniform population’s flat shape. As the sample size increases to 10, the distribution smoothens. By a sample size of 30, it closely approximates a normal distribution, and at 50, the fit is even tighter, with the mean centered at 5 and a standard deviation that decreases as expected (following *σ/√n*).

#### Exponential Distribution
The exponential population, with a rate of 1, has a mean and standard deviation of 1, and its right-skewed shape poses a challenge for the CLT at small sample sizes. At a sample size of 5, the sampling distribution retains significant skewness. However, by a sample size of 10, the skewness diminishes, and at 30, the distribution begins to resemble a normal curve. At 50, the distribution is nearly symmetric, centered around the population mean of 1, illustrating the CLT’s ability to normalize even skewed distributions with sufficient sample size.

#### Binomial Distribution
The binomial population (100 trials, p = 0.5) has a mean of 50 and a standard deviation of 5. At a sample size of 5, the sampling distribution appears discrete, reflecting the binomial’s stepped nature. As the sample size grows to 10, the discreteness smooths out. By 30, the distribution takes on a bell-shaped form, and at 50, it is nearly indistinguishable from a normal distribution, centered at 50, confirming the CLT’s predictions for discrete distributions.

### Insights from Parameter Variations

The simulations reveal key insights into how different factors affect the CLT’s behavior:
- **Sample Size**: The most significant factor, with larger sample sizes (30 and 50) producing sampling distributions that closely resemble a normal distribution. Smaller sizes (5 and 10) retain more characteristics of the original population, such as skewness or discreteness.
- **Population Shape**: Symmetric distributions (uniform and binomial) converge to normality faster than the skewed exponential distribution. However, all distributions eventually approximate normality with a large enough sample size.
- **Variance Impact**: Populations with higher variance (e.g., uniform) produce wider sampling distributions initially, but the standard deviation of the sampling distribution scales as *σ/√n*, where *σ* is the population standard deviation and *n* is the sample size, leading to tighter distributions as *n* increases.

### Real-World Relevance

The CLT underpins many practical applications in statistics:
- **Public Opinion Polling**: Pollsters rely on the CLT to estimate population opinions (e.g., voting preferences) from sample means, assuming the sampling distribution is normal to construct confidence intervals.
- **Industrial Quality Assurance**: Manufacturers use the CLT to monitor product quality (e.g., average dimensions of parts) by sampling, ensuring consistency across batches.
- **Economic Forecasting**: Economists apply the CLT to model economic indicators (e.g., average consumer spending) based on sample data, aiding in policy decisions.
- **Clinical Trials**: Medical researchers use the CLT to analyze sample means of health outcomes (e.g., cholesterol levels), enabling broader population inferences.

### Ideas for Further Investigation

To deepen understanding of the CLT, consider the following:
- **Non-Standard Distributions**: Explore distributions with extreme properties, such as the Cauchy distribution, which lacks a finite mean and variance, to test the CLT’s boundaries.
- **Very Small Samples**: Examine how the CLT behaves with extremely small sample sizes (e.g., 2 or 3) to understand its limitations.
- **Different Statistics**: Investigate whether other statistics, such as the sample median or variance, also converge to normality under the CLT framework.
- **Applied Contexts**: Use real-world datasets (e.g., income distributions or biological measurements) to test the CLT’s applicability in practical scenarios.

### Conclusion

This analysis of the Central Limit Theorem through simulations confirms its theoretical predictions: the sampling distribution of the mean approaches a normal distribution as the sample size increases, regardless of the population’s original distribution. The uniform, exponential, and binomial distributions each demonstrate this convergence, with larger sample sizes producing more normal-like sampling distributions. These findings highlight the CLT’s robustness and its critical role in enabling statistical inference across diverse fields, from polling to medical research. Further exploration with varied distributions or real-world data could provide additional insights into the theorem’s practical utility.


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