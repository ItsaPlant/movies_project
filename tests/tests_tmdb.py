from unittest.mock import Mock
import pytest
import tmdb_client

def test_get_poster_url_uses_default_size():
    #data prep
    poster_api_path = "some-poster-patch"
    expected_default_size = "w342"
    #call tested code
    poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
    #porównanie wyników
    assert expected_default_size in poster_url

def get_popular_movies_type_popular():
    movies_list = tmdb_client.get_popular_movies(list_type='popular')
    assert movies_list is not None
    
def test_get_popular_movies(monkeypatch):
    #lista zwracana przez przysłonięte "zapytanie do API"
    mock_movies_list = ['Movie 1', 'Movie 2']

    requests_mock = Mock()
    # Wynik wywołania zapytania do API
    responce = requests_mock.return_value
    #przysłaniamy wynik wywołania metody .json()
    responce.json.return_value = mock_movies_list
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    movies_list = tmdb_client.get_popular_movies(list_type='popular')
    assert movies_list == mock_movies_list

def test_get_single_movie(monkeypatch):
    #lista zwracana przez przysłonięte "zapytanie do API"
    mock_movies_list = ['Movie 1']

    requests_mock = Mock()
    # Wynik wywołania zapytania do API
    responce = requests_mock.return_value
    #przysłaniamy wynik wywołania metody .json()
    responce.json.return_value = mock_movies_list
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    movies_list = tmdb_client.get_single_movie(movie_id=1)
    assert movies_list == mock_movies_list

def test_get_movie_images(monkeypatch):
    #lista zwracana przez przysłonięte "zapytanie do API"
    mock_movies_list = ['Movie 1', 'Movie 2']

    requests_mock = Mock()
    # Wynik wywołania zapytania do API
    responce = requests_mock.return_value
    #przysłaniamy wynik wywołania metody .json()
    responce.json.return_value = mock_movies_list
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    movies_list = tmdb_client.get_movie_images(movie_id=1)
    assert movies_list == mock_movies_list

def test_get_single_movie_cast(monkeypatch):
    #lista zwracana przez przysłonięte "zapytanie do API"
    mock_movies_list = [{'adult': False, 'gender': 0, 'id': 1426170, 'known_for_department': 'Acting', 'name': 'Johnny Sachon', 'original_name': 'Johnny Sachon', 'popularity': 0.612, 'profile_path': None, 'cast_id': 4, 'character': 'Issac', 'credit_id': '5f4c7f0a223a8b0038af579a', 'order': 1}]

    requests_mock = Mock()
    # Wynik wywołania zapytania do API
    responce = requests_mock.return_value
    #przysłaniamy wynik wywołania metody .json()
    responce.json.return_value = mock_movies_list
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    movies_list = tmdb_client.get_single_movie_cast(movie_id=725273, how_many=1)
    assert movies_list == mock_movies_list