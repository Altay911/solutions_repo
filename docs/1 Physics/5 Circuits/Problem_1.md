def combine_series(resistors):
    return sum(resistors)

def combine_parallel(resistors):
    return 1 / sum(1 / r for r in resistors)

# ----------- EXAMPLES -----------

# Example 1: Series
series_example = [5, 10]  # R1 + R2
result_series = combine_series(series_example)
print("Example 1: Series [5Ω, 10Ω]")
print(f"Equivalent Resistance: {result_series} Ω")

# Example 2: Parallel
parallel_example = [4, 6]  # 1 / (1/R1 + 1/R2)
result_parallel = combine_parallel(parallel_example)
print("\nExample 2: Parallel [4Ω, 6Ω]")
print(f"Equivalent Resistance: {round(result_parallel, 2)} Ω")

# Example 3: Nested (2 in parallel, then added in series)
# (R1 || R2) + R3 => (1 / (1/2 + 1/2)) + 3 = 1 + 3 = 4
nested_parallel = [2, 2]
parallel_part = combine_parallel(nested_parallel)
result_nested = combine_series([parallel_part, 3])
print("\nExample 3: Nested [(2Ω || 2Ω) + 3Ω]")
print(f"Equivalent Resistance: {result_nested} Ω")
