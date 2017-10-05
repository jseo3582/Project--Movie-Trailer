import webbrowser


class Movie():

    # centents are defined here
    def __init__(
        self, 
        movie_title,
        movive_storyline,
        poster_image,
        trailer_youtube):
    self.title = movie_title
    self.storyline = movive_storyline
    self.poster_image_url = poster_image
    self.trailer_youtube_url = trailer_youtube

    # open webbrowser when check the poster
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
