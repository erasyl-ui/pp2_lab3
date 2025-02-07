"""Write a function that returns a sublist of movies with an IMDB score above 5.5"""

def high_imdb_movies(movie_list):
    return [movie for movie in movie_list if movie["imdb"] > 5.5]

# Example:
# Input: movies (full list)
# Output: List of movies with IMDB > 5.5

print(high_imdb_movies(movies))
