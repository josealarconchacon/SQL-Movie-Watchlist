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

# add movie func
def prompt_add_movie():
    title = input("Movie title: ")
    release_date = input("Release date (dd-mm-YYYY): ")
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    time_stamp = parsed_date.timestamp()

    database.add_movie(title, time_stamp)

while (user_input := input(movie_menu)) != "6":
    if user_input == "1":
        prompt_add_movie()
    elif user_input == "2":
        pass
    elif user_input == "3":
        pass
    elif user_input == "4":
        pass
    elif user_input == "5":
        pass
    else:
        print("You've entered an invalid input, please try again!")