"""Write a function that takes a list of movies and computes the average IMDB score."""

def average_imdb(movie_list):
    if not movie_list:
        return 0
    return sum(movie["imdb"] for movie in movie_list) / len(movie_list)

# Example:
# Input: movies (full list)
# Output: Average IMDB score

print("Average IMDB score:", average_imdb(movies))
