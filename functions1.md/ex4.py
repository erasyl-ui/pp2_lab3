"""""""
Write a function filter_prime which will take a list of numbers as an argument 
   - and returns only prime numbers from the list.
"""""""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

# Example:
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Prime numbers:", filter_prime(numbers))
