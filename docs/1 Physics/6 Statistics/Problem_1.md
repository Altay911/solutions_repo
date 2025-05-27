# Central Limit Theorem Simulation Analysis

### Introduction

The Central Limit Theorem (CLT) is a cornerstone of probability and statistics, stating that the sampling distribution of the sample mean approaches a normal distribution as the sample size increases, regardless of the population's original distribution. This simulation explores this phenomenon using various population distributions—uniform, exponential, and binomial—to provide an intuitive understanding of the CLT through computational experiments.

![alt text](<download (10).png>)

### Simulation Methodology

The simulation involves the following steps for each distribution:
- Generate a large dataset representing the population.
- Randomly sample data with different sample sizes (e.g., 5, 10, 30, 50).
- Repeat the sampling process multiple times to create a sampling distribution of the sample mean.
- Visualize the sampling distributions and observe their convergence to a normal distribution.

Three population distributions were selected:
- **Uniform Distribution**: Values are evenly distributed between 0 and 10.
- **Exponential Distribution**: Models time between events, with a rate parameter of 1.
- **Binomial Distribution**: Represents the number of successes in 100 trials, with a success probability of 0.5.

### Results and Analysis

#### Uniform Distribution
- **Population**: Generated with 10,000 samples from a uniform distribution (0 to 10).
- **Sampling**: Sample sizes of 5, 10, 30, and 50 were used, with 1,000 repetitions each.
- **Observation**: The sampling distribution of the mean starts skewed with small sample sizes (e.g., 5) but approaches a normal distribution as the sample size increases to 50, with a mean around 5 and reduced variance.

#### Exponential Distribution
- **Population**: Generated with 10,000 samples from an exponential distribution (rate = 1).
- **Sampling**: Same sample sizes and repetitions as above.
- **Observation**: The original distribution is right-skewed, but the sampling distribution becomes more symmetric and bell-shaped with sample sizes of 30 and 50, centering around 1 (the theoretical mean).

#### Binomial Distribution
- **Population**: Generated with 10,000 samples from a binomial distribution (100 trials, p = 0.5).
- **Sampling**: Same sample sizes and repetitions.
- **Observation**: The sampling distribution shifts from a discrete, binomial-like shape at small sizes to a smooth normal curve at size 50, with a mean near 50 (expected value).

### Parameter Exploration
- **Sample Size Influence**: Larger sample sizes accelerate convergence to normality, with noticeable effects starting at 30.
- **Population Variance**: Higher variance in the population (e.g., exponential) results in a wider sampling distribution, but the CLT still holds as sample size increases.
- **Shape of Original Distribution**: Skewed distributions (exponential) take longer to normalize compared to symmetric ones (uniform), but all converge with sufficient samples.

### Practical Applications
The CLT is crucial in real-world scenarios:
- **Estimating Population Parameters**: Used in surveys to infer population means from sample data.
- **Quality Control in Manufacturing**: Helps assess product consistency using sample means.
- **Predicting Outcomes in Financial Models**: Enables risk assessment based on sample data distributions.

### Conclusion
This simulation confirms the CLT's prediction that the sampling distribution of the mean approaches normality with increasing sample size, regardless of the population distribution. The visualizations highlight this convergence, aligning with theoretical expectations and underscoring the theorem's significance in statistical inference.
