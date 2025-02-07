"""""""
Write a function that takes a list and returns a new list with unique elements of the first list. 
    - Note: don't use collection set.
"""""""

def unique_elements(lst):
    unique_list = []
    for num in lst:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list

# Example:
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Unique elements:", unique_elements(numbers))
