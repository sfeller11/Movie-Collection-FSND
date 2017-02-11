import webbrowser


class Movie():
    """This class creates a Movie object containing:

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

    def show_trailer(self):
        # Open webrowser loading YouTube trailer
        webbrowser.open(self.trailer_youtube_url)
