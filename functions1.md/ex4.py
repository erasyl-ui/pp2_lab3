"""You are given list of numbers separated by spaces. Write a function filter_prime which 
will take list of numbers as an argument and returns only prime numbers from the list."""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Prime numbers:", filter_prime(numbers))

# Example:
# Input: 10 3 5 8 19 25 31
# Output: Prime numbers: [3, 5, 19, 31]
