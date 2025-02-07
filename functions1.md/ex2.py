"""Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature.
The following formula is used for the conversion: C = (5 / 9) * (F – 32)"""

def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
print(fahrenheit_to_celsius(fahrenheit), "Celsius")

# Example:
# Input: 100
# Output: 37.77777777777778 Celsius

