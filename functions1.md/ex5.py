"""""""
Write a function that accepts a string from the user and prints all permutations of that string.
"""""""

from itertools import permutations

def print_permutations(s):
    for perm in permutations(s):
        print("".join(perm))

# Example:
s = input("Enter a string: ")
print_permutations(s)
