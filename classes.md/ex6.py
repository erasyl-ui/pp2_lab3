"""""""
Write a program which can filter prime numbers in a list by using filter function. 
   - Note: Use lambda to define anonymous function.
"""""""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [10, 3, 5, 8, 19, 25, 31]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))

# Example:
# Input: [10, 3, 5, 8, 19, 25, 31]
# Output: Prime Numbers: [3, 5, 19, 31]

print("Prime Numbers:", prime_numbers)
