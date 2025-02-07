"""Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens 
and rabbits in a farm. How many rabbits and how many chickens do we have? create function: 
solve(numheads, numlegs)"""

def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (chickens * 2 + rabbits * 4) == numlegs:
            return chickens, rabbits

heads = int(input("Enter number of heads: "))
legs = int(input("Enter number of legs: "))
chickens, rabbits = solve(heads, legs)
print(f"Chickens: {chickens}, Rabbits: {rabbits}")

# Example:
# Input: 35, 94
# Output: Chickens: 23, Rabbits: 12
