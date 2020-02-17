from bs4 import BeautifulSoup
import json
import requests
from nltk import pos_tag, word_tokenize
import sys

requestUrl = input("Enter the Url of Recipe Page: ")
# requestUrl =  "https://www.allrecipes.com/recipe/175383/shrimp-scampi-with-linguini/?internalSource=previously%20viewed&referringContentType=Homepage&clickId=cardslot%204"

response = requests.get(requestUrl)

# initialize beautiful soup object from web response 
soup = BeautifulSoup(response.text, features="lxml")

# access & format the recipe title
recipeTitle = soup.title.string.split('-')[0]

# access & format the ingredients list
ingredients = soup.find_all("li", class_="checkList__line")
ingredientsResult = []
for ingredient in ingredients:
    ingredientsResult.append(ingredient.label.text)
    
# cut off the "add more ingredients" text from the page
ingredientsResult = ingredientsResult[:len(ingredientsResult)-3]

# build up lists of ingredient names, quanities, measurements
name = []
quantity = []
measurement = []
preparation = []
descriptor = []

for indx in range(len(ingredientsResult)):
    tokenized = pos_tag(word_tokenize(ingredientsResult[indx]))
    for word in tokenized:
        if word[1] == 'CD':
            quantity.append(word[0])
        elif word[1] == 'NN':
            if word[0] not in ['package', 'cup', 'teaspoon', 'tablespoon', 'ounce']:
                name.append(word[0])
            else:
                measurement.append(word[0])
        elif word[1] == 'VBD':
            preparation.append(word[0])
        elif word[1] == 'JJ':
            descriptor.append(word[0])

# http response code for debugging
# print(response.status_code)

# tkn = pos_tag(word_tokenize(ingredientsResult[3]))

print(recipeTitle)

print("\nLIST OF INGREDIENTS FOR RECIPE")

for i in range(len(ingredientsResult)):
    print(ingredientsResult[i])

print("\nNAMES")
print(name)

print("\nQUANTITIES")
print(quantity)
 
print("\nMEASUREMENTS")
print(measurement)

print("\nPREPERATIONS")
print(preparation)

print("\nDESCRIPTORS")
print(descriptor)

# print(tkn)