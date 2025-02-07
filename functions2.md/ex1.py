"""Write a function that takes a single movie and returns True if its IMDB score is above 5.5"""

def is_high_imdb(movie):
    return movie["imdb"] > 5.5

# Example:
# Input: {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"}
# Output: True

movie_name = input("Enter movie name: ")
movie = next((m for m in movies if m["name"] == movie_name), None)
if movie:
    print(is_high_imdb(movie))
else:
    print("Movie not found")
