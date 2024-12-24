def is_palindrome_loop(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Example usage
input_string = input("Enter a string: ")
print(f"Is '{input_string}' a palindrome? {is_palindrome_loop(input_string)}")
