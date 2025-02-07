"""""""
4. Write the definition of a Point class. Objects from this class should have:
   - A method show to display the coordinates of the point.
   - A method move to change these coordinates.
   - A method dist that computes the distance between 2 points.
"""""""

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point Coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

# Example:
# Input: Point(3, 4), Point(6, 8)
# Output: Distance: 5.0

x1, y1 = map(float, input("Enter first point (x1 y1): ").split())
x2, y2 = map(float, input("Enter second point (x2 y2): ").split())
p1 = Point(x1, y1)
p2 = Point(x2, y2)
print("Distance:", p1.dist(p2))
