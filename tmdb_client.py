import random
import requests

api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmNjY2OThiM2U2MThhNmNiYWU4ZDViYWE4YzJlODBkMSIsInN1YiI6IjYxNDljZDM3ZDZjMzAwMDAyYTQ2MWE4YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.eOu24_4pF0SitW_gYiGnXuIw6sN6rVtwZP3IpKlgW80"


def get_popular_movies(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()
    
def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"   

def get_movies(how_many, list_type):
    #list_type_check(list_type) zablokowane, ponieważ nei ma m dostępu do listy rodzajów filmow z API
    data = get_popular_movies(list_type)['results']
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

def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

#nie mogę znaleźć odpowiedniego endpointu - ale powinno działać
def get_genres():
    endpoint = "https://api.themoviedb.org/3/genre/movie/list"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    response = response.json()['genres'] ###dostosować nazwę słownika
    #response = [response['name'] for response in response]   ###wyłuskać odpowiednie zasoby
    return response

def get_genre_movies(collection_id):
    # collection_dict = {genre['name']:genre['id']}    ###stworzyć sownik 'nazwa': id
    # collection_id = collection_dict[genre]            ###wybrać odpowiednie id z listy, uprzednio dodać wymagany parametr w funkcji na podstawie wyboru przycisku
    endpoint = f"https://api.themoviedb.org/3/collection/{collection_id}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json(), collection_dict

def get_movies_by_genre(how_many, genre):
    data = get_genre_movies(genre)['results']
    return random.sample(data, k=len(data))[:how_many]

def list_type_check(list_type):
    genres = get_genres()
    genres = [genres['name'] for genres in genres]    ###stworzyć sownik 'nazwa': id
    for genre in genres:
        if list_type == genre:
            return True
        get_movies(how_many=8, list_type="popularr")
    return genres
