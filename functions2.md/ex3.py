"""Write a function that takes a category name and returns just those movies under that category."""

def movies_by_category(movie_list, category):
    return [movie for movie in movie_list if movie["category"].lower() == category.lower()]

# Example:
# Input: "Romance"
# Output: List of movies in "Romance" category

category = input("Enter category name: ")
print(movies_by_category(movies, category))
