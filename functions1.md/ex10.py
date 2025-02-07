"""Write a Python function that takes a list and returns a new list with unique elements of the first list. 
Note: don't use collection set."""

def unique_elements(lst):
    unique_list = []
    for num in lst:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Unique elements:", unique_elements(numbers))

# Example:
# Input: 1 2 2 3 4 4 5
# Output: [1, 2, 3, 4, 5]

