import random
import requests

api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmNjY2OThiM2U2MThhNmNiYWU4ZDViYWE4YzJlODBkMSIsInN1YiI6IjYxNDljZDM3ZDZjMzAwMDAyYTQ2MWE4YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.eOu24_4pF0SitW_gYiGnXuIw6sN6rVtwZP3IpKlgW80"


def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()
    
def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"   

def get_movies(how_many):
    data = get_popular_movies()['results']
    return random.sample(data, k=len(data))[:how_many]

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_single_movie_cast(movie_id, how_many):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()['cast'][:how_many]