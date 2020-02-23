from bs4 import BeautifulSoup
import json
import nltk
import requests
from nltk import pos_tag, word_tokenize
import sys
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from lists import kitchenTools, kitchenTools_two

def getpagelinks(searchpage):
  searchpage = requests.get(searchpage)
  soupsearch = BeautifulSoup(searchpage.content, 'html.parser')
  urls = soupsearch.findAll("a")#.text
  #urls
  links=[]
  #ind = -1
  for tag in urls:
    oneurl=tag.get("href")
    if oneurl:
      if ("/recipe/" in oneurl):
        #if((ind < 0) or ((ind >= 0) and (links[ind] != oneurl))):
        links.append(oneurl)
        #ind += 1
  return links
  
#Ex. searchlink = https://www.allrecipes.com/recipes/87/everyday-cooking/vegetarian/?page=4
def getpagesearch(searchlink):
  searchlist = []
  basesearchurl = searchlink[:-1]
  for x in range(2, 20):
    newsearchlink = basesearchurl + str(x)
    searchlist.append(newsearchlink)
  return searchlist
  
searchlist = getpagesearch("https://www.allrecipes.com/recipes/87/everyday-cooking/vegetarian/?page=4")
allpagelinks = []
for searchlink in searchlist:
  pagelinkslist = getpagelinks(searchlink)
  allpagelinks = allpagelinks + pagelinkslist
#getting rid of duplicate/triplicate links
allpagelinks = set(allpagelinks)
allpagelinks = list(allpagelinks)

allingredients = []
for recipepage in allpagelinks:
  ingredientnamelist = getingredients(recipepage)
  allingredients = allingredients + ingredientnamelist
#removing duplicates
allingredients = set(allingredients)
allingredients = list(allingredients)

#needs work, right now it just changes everything not found in allingredients (vegetarian) list to tofu. This also includes 
#medium carrots and thyme in this recipe: https://www.allrecipes.com/recipe/244700/beef-and-vegetable-soup/ , as well as broth 
def checkIsVeg(recipeurl):
  recipeSoup = getRecipeSoup(recipeurl)
  recipeTitle = recipeSoup.title.string.split('- ')[0]
  ingredientsList = getIngredientsList(recipeSoup)
  ingredients = getIngredientsObject(ingredientsList)
  ingredientnames = []
  for ingreditem in ingredients:
    ingredname = ingreditem['name']
    if ingredname in allingredients:
      ingredientnames.append(ingredname)
    else:
      ingredientnames.append('tofu')
  return ingredientnames
