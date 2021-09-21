from flask import Flask, render_template
import tmdb_client

app = Flask(__name__)

@app.route("/")
def homepage():
    movies = tmdb_client.get_popular_movies()['results'][:8]
    return render_template("homepage.html", movies=movies)

if __name__ == '__main__':
    app.run(debug=True)