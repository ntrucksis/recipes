from bs4 import BeautifulSoup
import json
import requests

requestUrl =  "https://www.allrecipes.com/recipe/175383/shrimp-scampi-with-linguini/print/?recipeType=Recipe&servings=4&isMetric=false"

request = requests.get(requestUrl)

# json.parse wasn't working, this just prints the whole html doc
jsonResponse = json.dumps(request.text)

responseSoup = BeautifulSoup(request.text).encode('utf-8')

print(responseSoup)
