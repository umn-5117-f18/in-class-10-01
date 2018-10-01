import os

from flask import Flask, jsonify, redirect, render_template, request, url_for
import psycopg2

import db

app = Flask(__name__)

@app.before_first_request
def initialize():
    db.setup()

@app.route('/')
def home():
    with db.get_db_cursor() as cur:
        cur.execute("SELECT * FROM movie")
        movies = [record for record in cur]
    return render_template("home.html", movies=movies)

@app.route('/movies/<movie_id>')
def movie(movie_id):
    with db.get_db_cursor() as cur:
        cur.execute("SELECT * FROM movie where movie_id=%s", (movie_id,))
        movie = cur.fetchone()
    return render_template("movie.html", movie=movie)

if __name__ == '__main__':
    pass
