import datetime
import database

movie_menu = """\nSelect one of the following option:
1) Add new movie.
2) View upcoming movies.
3) View all movies.
4) Watch a movie.
5) View watched movies.
6) Exit.

Select option: """

welcome_message = "Welcome to the Watchlist app!"
print(welcome_message)

database.create_tables()

# add movie
def prompt_add_movie():
    title = input("Movie title: ")
    release_date = input("Release date (dd-mm-YYYY): ")
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    time_stamp = parsed_date.timestamp()

    database.add_movie(title, time_stamp)


# print upcoming list of movies
def print_movies_list(heading, movies):
    print(f"|-------- {heading} Movies --------|")
    for m in movies:
        # parse the timestamp into a datetime object, then converted into a string
        movie_date = datetime.datetime.fromtimestamp(m[1])
        real_date = movie_date.strftime("%b %d %Y")
        print(f"{m[0]} (on {real_date})")
    print("------------------------------------\n")


# mark a movie as watched 
def prompt_watched_movie():
    movie_title = input("Enter movie title you watched: ")
    database.watch_movie(movie_title)

while (user_input := input(movie_menu)) != "6":
    if user_input == "1":
        prompt_add_movie()
    elif user_input == "2":
        movies = database.get_movies(True)
        print_movies_list("Upcoming", movies)
    elif user_input == "3":
        movies = database.get_movies()
        print_movies_list("All", movies)
    elif user_input == "4":
        prompt_watched_movie()
    elif user_input == "5":
        movies = database.get_watched_movies()
        print_movies_list("All", movies)
    else:
        print("You've entered an invalid input, please try again!")