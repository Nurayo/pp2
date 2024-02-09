#1
def is_high_imdb(movie):
    return movie.get("imdb", 0) > 5.5
movie_example = {
    "name": "Usual Suspects",
    "imdb": 7.0,
    "category": "Thriller"
}
result = is_high_imdb(movie_example)
print(result)

#2
def high_imdb_movies(movie_list):
    return [movie for movie in movie_list if movie.get("imdb", 0) > 5.5]

movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
]
result = high_imdb_movies(movies)
print(result)

#3
def filter(movies, category):
    return [movie for movie in movies if movie['category'] == category]

category_name = "Romance"
romance_movies = filter(movies, category_name)
print(romance_movies)

#4
def average_imdb_score(movies):
    if not movies:
        return 0.0
    total_score = sum(movie['imdb'] for movie in movies)
    average_score = total_score / len(movies)
    return average_score

average_score = average_imdb_score(movies)
print("Average IMDb score:", average_score)


#5
def average_score_by_category(movies, category):
    category_movies = [movie['imdb'] for movie in movies if movie['category'] == category]

    if not category_movies:
        return 0.0

    average_score = sum(category_movies) / len(category_movies)
    return average_score

category_name = "Romance"
average_score = average_score_by_category(movies, category_name)
print(f"Average IMDb score for {category_name} movies:", average_score)
