def factorial_while(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

# Example usage
n = 5
print(f"Factorial of {n} is {factorial_while(n)}")
