import tmdb_client
import random

data = (tmdb_client.get_popular_movies()['results'])
print(random.choices(data, k=3))