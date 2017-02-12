# -----------------------------------------------------------------------------
# Name:        entertainment_center
# Purpose:     This module creates instances of the class 'movie' in 'media',
#              collcets them in a list and then opens a webbrowser displaying
#              a newley created html with the movie collection.
#
# Author:      Stephan Feller
# Created:     12.02.2017
# -----------------------------------------------------------------------------

import fresh_tomatoes
import media


# Create instances of 'movie' class located in 'media'
print("Creating movie objects...\n")
toy_story = media.Movie(
                "Toy Story",  # Movie title
                "A story of a boy and his toys that come to life",  # Storyline
                "https://images-na.ssl-images-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_SY1000_SX670_AL_.jpg",  # NOQA
                "https://www.youtube.com/watch?v=4KPTXpQehio")  # YouTube URL

avatar = media.Movie(
                "Avatar",  # Movie title
                "A marine on an alien planet",  # Storyline
                "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_.jpg",  # NOQA
                "https://www.youtube.com/watch?v=1FcaRebb-bM")  # YouTube URL

school_of_rock = media.Movie(
                "School of Rock",  # Movie title
                "After being kicked out of a rock band, Dewey Finn becomes a "
                "substitute teacher of a strict elementary private school, "
                "only to try and turn it into a rock band.",  # Storyline
                "https://images-na.ssl-images-amazon.com/images/M/MV5BMjEwOTMzNjYzMl5BMl5BanBnXkFtZTcwNjczMTQyMQ@@._V1_.jpg",  # NOQA
                "https://www.youtube.com/watch?v=3PsUJFEBC74")  # YouTube URL

midnight_in_paris = media.Movie(
                "Midnight in Paris",  # Movie title
                "While on a trip to Paris with his fianc?e's family, a "
                "nostalgic screenwriter finds himself mysteriously going back "
                "to the 1920s everyday at midnight.",  # Storyline
                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg?",  # NOQA
                "https://www.youtube.com/watch?v=BYRWfS2s2v4")  # YouTube URL

hunger_games = media.Movie(
                "Hunger Games",  # Movie title
                "Katniss Everdeen voluntarily takes her younger sister's "
                "place in the Hunger Games, a televised competition in which "
                "two teenagers from each of the twelve Districts of Panem are "
                "chosen at random to fight to the death.",  # Storyline
                "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",  # NOQA
                "https://www.youtube.com/watch?v=4S9a5V9ODuY")  # YouTube URL

pulp_fiction = media.Movie(
                "Pulp Fiction",  # Movie title
                "The lives of two mob hit men, a boxer, a gangster's wife, and"
                " a pair of diner bandits intertwine in four tales of violence"
                " and redemption.",  # Storyline
                "https://images-na.ssl-images-amazon.com/images/M/MV5BMTkxMTA5OTAzMl5BMl5BanBnXkFtZTgwNjA5MDc3NjE@._V1_SY1000_CR0,0,673,1000_AL_.jpg",  # NOQA
                "https://www.youtube.com/watch?v=s7EdQ4FqbhY")  # YouTube URL

# Create 'movies' list containing movie objects
print("\nCreating movies list...")
movies = [toy_story, avatar, school_of_rock, midnight_in_paris,
          hunger_games, pulp_fiction]

# Run method 'open_movies' to create and open 'fresh_tomatoes.html'
print("\nOpening movie collection in browser ...")
fresh_tomatoes.open_movies_page(movies)
