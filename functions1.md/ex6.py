"""""""
Write a function that accepts a string from the user and 
   - returns a sentence with the words reversed.
   - Example: "We are ready" -> "ready are We"
"""""""

def reverse_sentence(sentence):
    return " ".join(sentence.split()[::-1])

# Example:
sentence = input("Enter a sentence: ")
print(reverse_sentence(sentence))
