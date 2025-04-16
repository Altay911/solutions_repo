# --------------------------------------------
# Equivalent Resistance Calculator (No Imports)
# --------------------------------------------

def combine_series(resistors):
    """Add resistors in series: R = R1 + R2 + ..."""
    return sum(resistors)

def combine_parallel(resistors):
    """Add resistors in parallel: 1/R = 1/R1 + 1/R2 + ..."""
    return 1 / sum(1 / r for r in resistors)

def print_result(title, resistance):
    print(f"{title}\nEquivalent Resistance: {round(resistance, 2)} Ω\n")

# -------------------
# Examples
# -------------------

# Example 1: Series
series_resistors = [5, 10]  # 5Ω + 10Ω
result_series = combine_series(series_resistors)
print_result("Example 1: Series [5Ω, 10Ω]", result_series)

# Example 2: Parallel
parallel_resistors = [4, 6]  # 1 / (1/4 + 1/6)
result_parallel = combine_parallel(parallel_resistors)
print_result("Example 2: Parallel [4Ω, 6Ω]", result_parallel)

# Example 3: Nested (Parallel inside Series)
# (2Ω || 2Ω) + 3Ω
nested_parallel = combine_parallel([2, 2])  # = 1Ω
nested_total = combine_series([nested_parallel, 3])  # = 4Ω
print_result("Example 3: Nested [(2Ω || 2Ω) + 3Ω]", nested_total)

# Example 4: Crazy One - ((2Ω || 4Ω) + (6Ω || 3Ω)) in series
part1 = combine_parallel([2, 4])  # = 1.33
part2 = combine_parallel([6, 3])  # = 2.0
crazy_result = combine_series([part1, part2])  # = 3.33
print_result("Example 4: Nested [(2||4)+(6||3)]", crazy_result)
