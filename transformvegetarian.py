from bs4 import BeautifulSoup
import json
import nltk
import requests
from nltk import pos_tag, word_tokenize
import sys
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from lists import kitchenTools, kitchenTools_two
import random
import recipeParser
import sizetransform

#vegsublist = ['tofu', 'tempeh', 'seitan']

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

#Use getpagesearch to get a list of pages with vegetarian recipes
#That's the input to getVegIngreds
#Then, use getpagelinks to get all of the recipe links out of each searchpage
#Then, get all the ingredients from each recipe using getingredients, and add them to the list of allingredients
def getingredients(recipeurl):
  recipeSoup = recipeParser.getRecipeSoup(recipeurl)
  ingredientsList = recipeParser.getIngredientsList(recipeSoup)
  ingredients = recipeParser.getIngredientsObject(ingredientsList)
  ingredientnames = []
  for ingreditem in ingredients:
    ingredname = ingreditem['name']
    ingredientnames.append(ingredname)
  return ingredientnames
  
def getVegIngreds(searchPageList):
  allpagelinks = []
  for searchlink in searchPageList:
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
  return allingredients

#searchlist = getpagesearch("https://www.allrecipes.com/recipes/87/everyday-cooking/vegetarian/?page=4")
#vegingreds = getVegIngreds(searchlist)

def changeToVeg(recipeObject, vegingredlist, vegsubs):
  for k in recipeObject:
    if sizetransform.checkIsInt(k):
      ingredname = recipeObject[k]['name'].lower()
      if not(ingredname in vegingredlist):
        if ('grill' in recipeObject['primaryMethods']) or ('grill' in recipeObject['primaryMethods']) or ('grill' in recipeObject['tools']):
          newname = 'tempeh'
        elif (('broth' in ingredname) or ('stock' in ingredname)):
          newname = 'vegetable broth'
        else:
          newname = random.choice(vegsubs)
        #ingredientnames.append('tofu') #TODO make here random component from ingredDict
        recipeObject[k]['name'] = newname
  return recipeObject
