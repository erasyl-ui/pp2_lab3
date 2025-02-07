"""Write a function that takes in a list of integers and returns True if it contains 007 in order"""

def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print(spy_game(numbers))

# Example:
# Input: 1 2 4 0 0 7 5
# Output: True
