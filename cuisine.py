# look at recipes similar to current one and find ways to transform them
# Mainly for transforming cuisines
from collections import Counter
from recipeParser import main as recipe
from lists import cuisines

class Cuisine:
	'''
	Attempts to classify the recipe as a certain cuisine and makes a tranformation
	to another kind
	Takes in a master recipe dict with all parsed data about the recipe
	'''
	def __init__(self, recipe):
		self.data = recipe	
	
	def classify(self):
		print (self.data)


base_url = 'https://www.allrecipes.com/recipe/245705/baked-chicken-alfredo/'

data = recipe(base_url)

cuisine = Cuisine(data)
cuisine.classify()