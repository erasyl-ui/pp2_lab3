"""Write a function that takes a category and computes the average IMDB score."""

def average_imdb_by_category(movie_list, category):
    category_movies = [movie for movie in movie_list if movie["category"].lower() == category.lower()]
    if not category_movies:
        return 0
    return sum(movie["imdb"] for movie in category_movies) / len(category_movies)

# Example:
# Input: "Romance"
# Output: Average IMDB score of "Romance" category movies

category = input("Enter category name: ")
print("Average IMDB score for", category, ":", average_imdb_by_category(movies, category))
