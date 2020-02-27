from bs4 import BeautifulSoup
import json
import nltk
import requests
from nltk import pos_tag, word_tokenize
import sys
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
import recipeParser
from fractions import Fraction

#Size transformation takes in recipe object

def checkIsInt(key):
  try:
    ind = int(key)
  except ValueError:
    return False
  return True

def checkIsFrac(val):
  try: 
    frac = Fraction(val)
  except ValueError:
    return False
  return True

def doubleSize(recipeObject):
  for k in recipeObject:
    if checkIsInt(k):
      quant = recipeObject[k]['quantity']
      if checkIsInt(quant):
        quant = int(quant)
        recipeObject[k]['quantity'] = str(quant * 2)
      elif checkIsFrac(quant):
        quant = Fraction(quant)
        recipeObject[k]['quantity'] = str(quant * 2)
  return recipeObject

def halfSize(recipeObject):
  for k in recipeObject:
    if checkIsInt(k):
      quant = recipeObject[k]['quantity']
      if checkIsInt(quant):
        quant = int(quant)
        recipeObject[k]['quantity'] = str(Fraction(quant / 2))
      elif checkIsFrac(quant):
        quant = Fraction(quant)
        recipeObject[k]['quantity'] = str(Fraction(quant / 2))
  return recipeObject
