"""""""
Read in a Fahrenheit temperature. 
   - Calculate and display the equivalent centigrade temperature. 
   - Formula: C = (5 / 9) * (F – 32)
"""""""

def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

# Example:
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
print(fahrenheit_to_celsius(fahrenheit), "Celsius")
