from bs4 import BeautifulSoup
import json
import requests

requestUrl =  "https://www.allrecipes.com/recipe/175383/shrimp-scampi-with-linguini/?internalSource=previously%20viewed&referringContentType=Homepage&clickId=cardslot%204"

response = requests.get(requestUrl)

# initialize beautiful soup object from web response 
soup = BeautifulSoup(response.text)

# access the recipe title
recipeTitle = soup.title.string


print(soup.encode('utf-8'))
print(response.status_code)
print(recipeTitle)