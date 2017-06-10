import webbrowser

class Movie():
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, star_rating, release_date):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.star_rating = star_rating
		self.release_date = release_date
		if not 0 <= self.star_rating <= 5: raise Exception('Star rating must be between 0 and 5.')
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)