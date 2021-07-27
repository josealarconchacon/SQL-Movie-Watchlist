# create table query
CREATE_Movies_table = """CREATE TABLE IF NOT EXISTS movies (
    title TEXT,
    release_timestamp REAL,
    watched INTEGER
);"""

# insert movies
INSERT_MOVIES = "INSERT INTO movies (title, release_timestamp, watched) VALUES (?,?,0);"
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
# select the upcoming movies
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > ?;"
SELECT_WATCHED_MOVIES = "SELECT * FROM movies WHERE watched = 1;"