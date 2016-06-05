# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

import webbrowser

class Movie():
    """ This is provides a way to store movie related information.
    This class including movie title, storyline, poster picture and Youtube trailer.
    """
    
    VALID_RATINGS = ["G","PG","PG-13","R"]
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        # initialize instance of class Movie


    def show_trailer(self):
        """show_trailer() is for open the trailer url in the web brower
        when the string run the web browser will be opened
        """
        webbrowser.open(self.trailer_youtube_url) 
