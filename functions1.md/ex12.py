"""Define a function histogram() that takes a list of integers and prints a histogram to the screen."""

def histogram(lst):
    for num in lst:
        print("*" * num)

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
histogram(numbers)

# Example:
# Input: 4 9 7
# Output:
# ****
# *********
# *******
