# Problem 1

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Function to generate and visualize sampling distributions
def central_limit_theorem(population_size=10000, sample_sizes=[5, 10, 30, 50], num_samples=1000):
    # 1. Generate large datasets from different distributions
    uniform_population = np.random.uniform(0, 1, population_size)
    exponential_population = np.random.exponential(1, population_size)
    binomial_population = np.random.binomial(10, 0.5, population_size)
    
    # 2. Function to take random samples and calculate the sample means
    def sample_means(population, sample_size, num_samples):
        means = []
        for _ in range(num_samples):
            sample = np.random.choice(population, size=sample_size, replace=False)
            means.append(np.mean(sample))
        return means
    
    # 3. Create plots for each distribution and sample size
    fig, axes = plt.subplots(3, len(sample_sizes), figsize=(15, 12))
    
    for i, sample_size in enumerate(sample_sizes):
        # Uniform distribution sampling
        uniform_means = sample_means(uniform_population, sample_size, num_samples)
        sns.histplot(uniform_means, bins=30, kde=True, ax=axes[0, i])
        axes[0, i].set_title(f'Uniform Distribution - Sample Size {sample_size}')
        
        # Exponential distribution sampling
        exponential_means = sample_means(exponential_population, sample_size, num_samples)
        sns.histplot(exponential_means, bins=30, kde=True, ax=axes[1, i])
        axes[1, i].set_title(f'Exponential Distribution - Sample Size {sample_size}')
        
        # Binomial distribution sampling
        binomial_means = sample_means(binomial_population, sample_size, num_samples)
        sns.histplot(binomial_means, bins=30, kde=True, ax=axes[2, i])
        axes[2, i].set_title(f'Binomial Distribution - Sample Size {sample_size}')
    
    plt.tight_layout()
    plt.show()

# Run the simulation
central_limit_theorem()
