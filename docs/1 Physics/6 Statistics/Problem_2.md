# Central Limit Theorem Simulation Analysis


### Introduction

The Central Limit Theorem (CLT) is a fundamental principle in statistics, asserting that the distribution of the sample mean approximates a normal distribution as the sample size becomes large, regardless of the population's underlying distribution. This property makes the CLT a powerful tool for statistical inference, enabling us to make assumptions about population parameters based on sample data. This analysis explores the CLT through simulations, examining how sampling distributions behave across different population distributions and sample sizes.

### Simulation Methodology

The simulation investigates the CLT by generating sampling distributions of the mean from three distinct population distributions:
- **Uniform Distribution**: Values uniformly distributed between 0 and 10, representing a flat, symmetric distribution.
- **Exponential Distribution**: Values following an exponential distribution with a rate parameter of 1, representing a right-skewed distribution often used to model time between events.
- **Binomial Distribution**: Values from a binomial distribution with 100 trials and a success probability of 0.5, representing a discrete, symmetric distribution for the number of successes.

For each distribution, the process involves:
1. Generating a large population dataset (10,000 samples).
2. Drawing random samples of various sizes (e.g., 5, 10, 30, 50) from the population.
3. Repeating the sampling process 1,000 times to create a sampling distribution of the sample mean.
4. Analyzing the resulting distributions to observe their shape and convergence to normality.

### Results and Analysis

#### Uniform Distribution
- **Population Characteristics**: The uniform distribution has a mean of 5 and a standard deviation of approximately 2.89.
- **Sampling Results**: With a sample size of 5, the sampling distribution of the mean shows some irregularity but is relatively symmetric due to the uniform nature of the population. As the sample size increases to 10, the distribution becomes smoother. By a sample size of 30, it closely resembles a normal distribution, and at 50, the bell-shaped curve is even more pronounced, centered around 5 with a reduced standard deviation.

#### Exponential Distribution
- **Population Characteristics**: The exponential distribution is right-skewed with a mean of 1 and a standard deviation of 1.
- **Sampling Results**: For a sample size of 5, the sampling distribution is noticeably skewed, reflecting the population’s asymmetry. At a sample size of 10, the skewness decreases, and by 30, the distribution begins to resemble a normal curve. At 50, the distribution is nearly symmetric, centered around 1, demonstrating the CLT’s effect on a skewed population.

#### Binomial Distribution
- **Population Characteristics**: The binomial distribution (100 trials, p = 0.5) has a mean of 50 and a standard deviation of 5.
- **Sampling Results**: With a sample size of 5, the sampling distribution appears discrete and stepped, reflecting the binomial nature. As the sample size increases to 10, the steps smooth out. By 30, the distribution takes on a bell shape, and at 50, it is nearly indistinguishable from a normal distribution, centered at 50.

### Parameter Exploration

The simulation highlights how various factors influence the convergence to normality:
- **Sample Size**: Larger sample sizes (e.g., 30 or 50) lead to faster convergence to a normal distribution, as predicted by the CLT. Smaller sizes (e.g., 5) retain more characteristics of the original population.
- **Population Distribution Shape**: Symmetric distributions (uniform, binomial) converge faster than skewed ones (exponential), but all approach normality with sufficient sample sizes.
- **Population Variance**: Distributions with higher variance (e.g., uniform) result in wider sampling distributions, but the standard deviation of the sampling distribution decreases as sample size increases, following the formula *σ/√n*, where *σ* is the population standard deviation and *n* is the sample size.

### Practical Applications

The CLT has wide-ranging applications in real-world scenarios:
- **Statistical Inference in Surveys**: Pollsters use the CLT to estimate population parameters (e.g., average voter preference) from sample means, assuming normality for confidence intervals.
- **Quality Control in Manufacturing**: Manufacturers sample products to assess quality metrics (e.g., average weight of items), relying on the CLT to ensure the sample mean’s distribution is normal for hypothesis testing.
- **Financial Modeling**: In risk analysis, the CLT helps model portfolio returns as normally distributed based on sample data, aiding in predictions of future performance.
- **Medical Research**: Researchers use the CLT to analyze sample means of health metrics (e.g., blood pressure) across populations, enabling generalized conclusions.

### Suggestions for Further Exploration

- **Impact of Extreme Distributions**: Test the CLT with highly skewed or heavy-tailed distributions (e.g., Cauchy) to explore its limitations, as the Cauchy distribution does not have a finite mean or variance, challenging the CLT.
- **Small Sample Behavior**: Investigate how very small sample sizes (e.g., 2 or 3) behave and compare them to theoretical expectations.
- **Multiple Statistics**: Extend the simulation to other statistics (e.g., sample variance or median) to see if they also converge to a normal distribution under similar conditions.
- **Real-World Data**: Apply the CLT simulation to real datasets (e.g., income distributions, biological measurements) to validate its practical utility.

### Conclusion

The simulation effectively demonstrates the Central Limit Theorem’s core principle: the sampling distribution of the mean approaches a normal distribution as the sample size increases, regardless of the population’s original shape. This convergence is evident across uniform, exponential, and binomial distributions, with larger sample sizes producing distributions that are increasingly symmetric and bell-shaped. These findings underscore the CLT’s importance in statistical analysis, providing a foundation for making reliable inferences about population parameters in diverse fields. Further exploration with more complex distributions or real-world data could enhance understanding of the theorem’s practical implications.


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