"""""""
Write a function that computes the volume of a sphere given its radius.
"""""""

import math

def sphere_volume(radius):
    return (4/3) * math.pi * (radius ** 3)

# Example:
radius = float(input("Enter the radius: "))
print("Volume of the sphere:", sphere_volume(radius))
