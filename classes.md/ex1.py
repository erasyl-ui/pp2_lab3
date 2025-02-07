"""""""
1. Define a class which has at least two methods: 
   - getString: to get a string from console input
   - printString: to print the string in upper case.
"""""""

class StringManipulator:
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input("Enter a string: ")

    def printString(self):
        print(self.text.upper())

# Example:
# Input: "hello"
# Output: "HELLO"

str_obj = StringManipulator()
str_obj.getString()
str_obj.printString()
