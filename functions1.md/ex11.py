"""""""
Write a function that checks whether a word or phrase is palindrome or not. 
    - Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam.
"""""""

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# Example:
word = input("Enter a word or phrase: ")
print("Palindrome:", is_palindrome(word))
