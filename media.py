# -----------------------------------------------------------------------------
# Name:        media
# Purpose:     Class defintion for instances of 'movie'
#
# Author:      Stephan Feller
# Created:     12.02.2017
# -----------------------------------------------------------------------------
import webbrowser


class Movie():
    """
    This class creates a Movie object containing:

    Attributes:
        movie_title (str): Movie itle
        movie_storyline (str): Storyline
        poster_image (str): Poster image URL
        trailer_youtube (str): YouTube trailer URL
    Method:
        show_trailer: Open YouTube trailer in webrowser
    """

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        # Define instance variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

        print("   "+self.title+" - OK!")

    def show_trailer(self):
        # Loading YouTube trailer in webbrowser
        webbrowser.open(self.trailer_youtube_url)
