"""Write a function that accepts a string from the user, return a sentence with the words reversed.
Example: We are ready -> ready are We"""

def reverse_sentence(sentence):
    return " ".join(sentence.split()[::-1])

sentence = input("Enter a sentence: ")
print(reverse_sentence(sentence))

# Example:
# Input: We are ready
# Output: ready are We
