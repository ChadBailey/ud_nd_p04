#Import webbrowser for opening trailer
import webbrowser

class Movie():
	"""
	Movie class
	Used to store attributes of movies to then be processed into an html file using fresh_tomatoes.py
	
	Input:
		Movie title, storyline, image url, trailer url, star rating (integer 0-5), release date
	
	Output:
		None
	
	Methods:
		show_trailer():
			opens youtube trailer URL in a browser
	"""

	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, star_rating, release_date):
		self.title = movie_title #Movie title (string)
		self.storyline = movie_storyline #Movie storyline (string)
		self.poster_image_url = poster_image #Poster image (string)
		self.trailer_youtube_url = trailer_youtube #Youtube trailer url (string)
		self.star_rating = star_rating #Star rating 0-5 (int)
		self.release_date = release_date #Release date (string)
		if not 0 <= self.star_rating <= 5: raise Exception('Star rating must be between 0 and 5.') #Prevent bad input
	def show_trailer(self):
		#Open trailer url
		webbrowser.open(self.trailer_youtube_url)
