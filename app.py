import datetime
import database

movie_menu = """\nSelect one of the following option:
1) Add new movie.
2) View upcoming movies.
3) View all movies.
4) Watch a movie.
5) View watched movies.
6) Add user to system.
7) Exit.

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
    for _id, title, release_date in movies:
        # parse the timestamp into a datetime object, then converted into a string
        movie_date = datetime.datetime.fromtimestamp(release_date)
        real_date = movie_date.strftime("%b %d %Y")
        print(f"{_id}: {title} (on {real_date})")
    print("------------------------------------\n")


#printing the watched movie data
def print_watched_movie_list(username, movies):
    print(f"------- {username}'s watched movies -------")
    for m in movies:
        print(f"{m[1]}")

    print("---------------------------------------\n")


# mark a movie as watched 
def prompt_watched_movie():
    username = input("Enter Username: ")
    movie_id = input("Enter Movie ID: ")
    database.watch_movie(username, movie_id)


def prompt_add_user():
    username = input("Enter username: ")
    database.add_user(username)



while (user_input := input(movie_menu)) != "7":
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
        username = input("Username: ")
        movies = database.get_watched_movies(username)
        print_watched_movie_list(username, movies)
    elif user_input == "6":
        prompt_add_user()
    else:
        print("You've entered an invalid input, please try again!")