#Intro to programming Project 4
#Movie Website

#Import media file which contains the Movie class
import media
#Import fresh_tomatoes which generates the website
import fresh_tomatoes

#Create instances of Movie class for each movie
avatar = media.Movie(\
						"Avatar", #Movie Name
						"A marine on an alien planet", #Movie Description
						"http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg", #Movie poster image
						"http://www.youtube.com/watch?v=-9ceBgWV8io", #Movie trailer
						4, #Star rating (must be 0-5)
						"Released: December 18, 2009" #Release date
					)

major_payne = media.Movie(\
						"Major Payne",
						"A recently discharged Major, finds himself commanding a group of mismatched Cadets.",
						"https://upload.wikimedia.org/wikipedia/en/8/85/Major_Payne.jpg",
						"https://www.youtube.com/watch?v=6Vvlw7uPdn8",
						3,
						"Released: March 24, 1995"
					)

ace_ventura = media.Movie(\
						"Ace Ventura: Pet Detective",
						"A goofy detective specializing in animals goes in search of the missing mascot of the Miami Dolphins.",
						"https://upload.wikimedia.org/wikipedia/en/8/84/Ace_ventura_pet_detective.jpg",
						"https://www.youtube.com/watch?v=cXcH0f2B2vA",
						4,
						"February 4, 1994"
					)

ace_ventura_wnc = media.Movie(\
						"Ace Ventura: When Nature Calls",
						"Ace Ventura, Pet Detective, returns from a spiritual quest to investigate the disappearance of a rare white bat, the sacred animal of a tribe in Africa.",
						"https://upload.wikimedia.org/wikipedia/en/b/b9/AceVenturaWhenNatureCallsposter.jpg",
						"https://www.youtube.com/watch?v=YG28rBUkgf8",
						3,
						"November 10, 1995"
					)

the_blind_side = media.Movie(\
						"The Blind Side",
						"The story of Michael Oher, a homeless and traumatized boy who became an All American football player and first round NFL draft pick with the help of a caring woman and her family.",
						"https://upload.wikimedia.org/wikipedia/en/6/60/Blind_side_poster.jpg",
						"https://www.youtube.com/watch?v=I24d30buecw",
						4,
						"November 20, 2009"
					)

glory = media.Movie(\
						"Glory",
						"Robert Gould Shaw leads the U.S. Civil War's first all-black volunteer company, fighting prejudices from both his own Union Army, and the Confederates.",
						"https://upload.wikimedia.org/wikipedia/en/0/0a/Glory_%281989_film%29_poster.jpg",
						"https://www.youtube.com/watch?v=B7zlcbLLnaE",
						4,
						"February 16, 1990"
					)
#Create a list of the objects to send along to fresh_tomatoes
movies = [avatar, major_payne, ace_ventura, ace_ventura_wnc, the_blind_side, glory]
#Send list of movie objects to fresh tomatoes for processing into a website.
fresh_tomatoes.open_movies_page(movies)
