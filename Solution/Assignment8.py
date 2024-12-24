def alphabet_pattern_for(n):
    for i in range(1, n+1):
        # Print leading spaces for alignment
        print(" " * (n - i), end="")
        
        # Print increasing alphabets (A, B, C, ...)
        for j in range(1, i+1):
            print(chr(64 + j), end=" ")
        
        # Print decreasing alphabets (B, A, ...)
        for j in range(i-1, 0, -1):
            print(chr(64 + j), end=" ")
        
        print()  # Move to the next line

# Example usage
n = 3
alphabet_pattern_for(n)
