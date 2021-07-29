import datetime
from os import pathconf_names
import sqlite3
from sqlite3.dbapi2 import Cursor

# create table query
CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies (
    title TEXT,
    release_timestamp REAL
);"""

CREATE_WATCHLIST_TABLE = """CREATE TABLE IF NOT EXISTS watched (
    watcher_name TEXT,
    title TEXT
);"""


# insert movies
INSERT_MOVIES = "INSERT INTO movies (title, release_timestamp) VALUES (?,?,0);"
# delete
DELETE_MOVIES = "DELETE FROM movies WHERE title = ?;"
#select
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
# select the upcoming movies
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > ?;"
SELECT_WATCHED_MOVIES = "SELECT * FROM watched WHERE watcher_name = ?;"
# insert 
INSERT_WATCHED_MOVIES = "INSERT INTO watched (watcher_name, title) VALUES (?,?);"
# Update
SET_MOVIE_WATCHED = "UPDATE movies SET watched = 1 WHERE title = ?;"

connection = sqlite3.connect("myMovieData.db")

def create_tables():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)
        connection.execute(CREATE_WATCHLIST_TABLE)

def add_movie(title, release_timestamp):
    with connection:
        connection.execute(INSERT_MOVIES, (title, release_timestamp))

def get_movies(upcoming=False):
    with connection:
        cursor = connection.cursor()
        # if upcoming = True
        if upcoming:
            today_timestamp = datetime.datetime.today().timestamp()
            cursor.execute(SELECT_UPCOMING_MOVIES, (today_timestamp,))
        else:
            cursor.execute(SELECT_ALL_MOVIES)
        return cursor.fetchall()

def watch_movie(username, title):
    with connection:
        connection.execute(DELETE_MOVIES, (title,))
        connection.execute(INSERT_WATCHED_MOVIES, (username, title))

def get_watched_movies():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_WATCHED_MOVIES)
        return cursor.fetchall()