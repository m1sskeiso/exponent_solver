# Recursive function to calculate powers
def power(base, exponent):
    # Base case: Any number raised to the power of 0 is 1
    if exponent == 0:
        return 1
    # Recursive case: Multiply base by the result of power(base, exponent - 1)
    else:
        return base * power(base, exponent - 1)

# Example usage:
result = power(2, 7)
print("2^7 =", result)
