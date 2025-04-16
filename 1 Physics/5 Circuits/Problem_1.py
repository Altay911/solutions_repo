# -------------------------------
# Equivalent Resistance Solver
# Using Python – Series & Parallel
# -------------------------------

def combine_series(resistors):
    """
    Combine resistors in series.
    Formula: R_eq = R1 + R2 + ...
    """
    return sum(resistors)

def combine_parallel(resistors):
    """
    Combine resistors in parallel.
    Formula: 1/R_eq = 1/R1 + 1/R2 + ...
    """
    return 1 / sum(1 / r for r in resistors)

def print_result(title, resistance):
    print("===================================")
    print(f"{title}")
    print(f"Equivalent Resistance: {round(resistance, 2)} Ω")
    print("===================================\n")


# -------------------------------
# Example 1: Series
# [5Ω + 10Ω] => 15Ω
# -------------------------------
series_resistors = [5, 10]
result_series = combine_series(series_resistors)
print_result("Example 1: Series [5Ω, 10Ω]", result_series)


# -------------------------------
# Example 2: Parallel
# [4Ω || 6Ω] => 1 / (1/4 + 1/6) = 2.4Ω
# -------------------------------
parallel_resistors = [4, 6]
result_parallel = combine_parallel(parallel_resistors)
print_result("Example 2: Parallel [4Ω, 6Ω]", result_parallel)


# -------------------------------
# Example 3: Nested (2Ω || 2Ω) + 3Ω
# => 1 / (1/2 + 1/2) = 1Ω + 3Ω = 4Ω
# -------------------------------
nested_parallel = combine_parallel([2, 2])
nested_total = combine_series([nested_parallel, 3])
print_result("Example 3: Nested [(2Ω || 2Ω) + 3Ω]", nested_total)


# -------------------------------
# Example 4: Complex Nested
# => (2Ω || 4Ω) + (6Ω || 3Ω)
# => 1.33Ω + 2Ω = 3.33Ω
# -------------------------------
part1 = combine_parallel([2, 4])
part2 = combine_parallel([6, 3])
crazy_result = combine_series([part1, part2])
print_result("Example 4: Complex Nested [(2Ω‖4Ω)+(6Ω‖3Ω)]", crazy_result)
