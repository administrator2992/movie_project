import json
import sys
import requests

def movie_image_search(title):
    response = requests.get(
        f"https://api.themoviedb.org/3/search/movie?api_key={sys.argv[1]}&query={title}"
    )
    data = response.json()
    if len(data['results']) >= 1:
        poster_path = data['results'][0]['poster_path']
    else:
        return 'static/assets/not_found.svg'
    poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
    img_response = requests.head(poster_url)
    if img_response.status_code != 200:
        return 'static/assets/not_found.svg'
    return poster_url

with open('movies.json') as f:
    original_data = json.load(f)

fixture_data = []

for movie in original_data:
    fixture_entry = {
        "model": "movies.movie",
        "pk": movie["id"],
        "fields": {
            "name": movie["name"],
            "description": movie["description"],
            "img_path": movie_image_search(movie["name"]),
            "duration": movie["duration"],
            "genre": ",".join(movie["genre"]),
            "language": movie["language"],
            "mpaa_type": movie["mpaaRating"]["type"],
            "mpaa_label": movie["mpaaRating"]["label"],
            "user_rating": movie["userRating"]
        }
    }
    fixture_data.append(fixture_entry)

with open('movies/fixtures/movies.json', 'w') as f:
    json.dump(fixture_data, f, indent=2)

print("Fixture conversion complete!")
