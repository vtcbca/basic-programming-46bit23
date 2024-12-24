def pattern_string_multiplication(n):
    for i in range(1, n + 1):
        print(" ".join("*" * i))

# Example usage
rows = 4
pattern_string_multiplication(rows)
