import os

from flask import Flask, abort, jsonify, redirect, render_template, request, url_for
import psycopg2

import db

app = Flask(__name__)

@app.before_first_request
def initialize():
    db.setup()

@app.route('/')
def home():
    with db.get_db_cursor() as cur:
        # TODO
        movies = None
    return render_template("home.html", movies=movies)

@app.route('/movies/<movie_id>')
def movie(movie_id):
    with db.get_db_cursor() as cur:
        # TODO
        movie = None

    # TODO 404 if not found

    return render_template("movie.html", movie=movie)

@app.route('/genres/<genre>')
def genre(genre):
    with db.get_db_cursor() as cur:
        cur.execute("SELECT * FROM movie where genre=%s", (genre,))
        movies = [record for record in cur]
    return render_template("home.html", movies=movies)

@app.route('/search')
def search():
    query = request.args.get('query')
    if not query:
        redirect('home')

    with db.get_db_cursor() as cur:
        # TODO like query
        movies = None
    return render_template("home.html", movies=movies)


if __name__ == '__main__':
    pass
