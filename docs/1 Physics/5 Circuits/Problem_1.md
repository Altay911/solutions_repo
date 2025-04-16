# ⚡ Equivalent Resistance Using Graph Theory (Simplified)

This Python script calculates **equivalent resistance** for series, parallel, and nested resistor networks using simple functions.

---

## 🔧 Functions

```python
def combine_series(resistors):
    """Returns the sum of all resistors in series."""
    return sum(resistors)

def combine_parallel(resistors):
    """Returns the equivalent resistance of parallel resistors."""
    return 1 / sum(1 / r for r in resistors)

def print_result(title, resistance):
    """Prints a formatted result."""
    print("===================================")
    print(f"{title}")
    print(f"Equivalent Resistance: {round(resistance, 2)} Ω")
    print("===================================\n")
