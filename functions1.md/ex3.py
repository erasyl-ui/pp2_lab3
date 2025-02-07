"""""""
Solve the classic puzzle: 
   - There are 35 heads and 94 legs among the chickens and rabbits in a farm. 
   - Find out how many rabbits and how many chickens there are.
   - Create function: solve(numheads, numlegs)
"""""""

def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (chickens * 2 + rabbits * 4) == numlegs:
            return chickens, rabbits

# Example:
heads = int(input("Enter number of heads: "))
legs = int(input("Enter number of legs: "))
chickens, rabbits = solve(heads, legs)
print(f"Chickens: {chickens}, Rabbits: {rabbits}")
