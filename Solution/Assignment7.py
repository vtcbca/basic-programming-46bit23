def triangle_pattern_format(n):
    for i in range(1, n + 1):
        print("{:>{width}}".format(" ".join(str(x) for x in range(1, 2 * i)), width=2 * n))

# Example usage
n = 3
triangle_pattern_format(n)
