"""Given a list of ints, return True if the array contains a 3 next to a 3 somewhere."""

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print(has_33(numbers))

# Example:
# Input: 1 3 3
# Output: True

