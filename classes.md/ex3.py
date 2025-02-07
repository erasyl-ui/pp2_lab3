"""""""
3. Define a class named Rectangle which inherits from Shape class from task 2.
   - Class instance can be constructed by a length and width.
   - The Rectangle class has a method which can compute the area.
"""""""

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Example:
# Input: length=4, width=6
# Output: 24

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
rect = Rectangle(length, width)
print("Rectangle Area:", rect.area())
