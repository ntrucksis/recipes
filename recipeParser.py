from bs4 import BeautifulSoup
import json
import requests
from nltk import pos_tag, word_tokenize
import sys

def getIngredientsObject(ingredientsList):
    ingredients = []
    for i in range(len(ingredientsList)):
        tokenized = pos_tag(word_tokenize(ingredientsList[i]))
        name = ""
        quant = ""
        msmt = ""
        prep = ""
        desc = ""
        q = []
        print(tokenized)
        
        for word in tokenized:
            if word[1] == 'CD':
                q.append(word[0])
                quant += word[0] + " "
            elif word[1] == 'JJ' or word[1] == 'MD':
                if word[0] in ['black', 'olive', 'maple', 'green',  'red', 'white', 'beef', 'garlic', 'sour', 'lemon', 'heavy']:
                    name += word[0] + " "
                else:
                    if word[0] in ['pinch', 'cup', 'can']:
                        msmt+= word[0] + " "
                    elif word[0] in ['frozen']:
                        prep += word[0] + " "
                    else:
                        desc += word[0] + " "
            elif word[1] in ['NN', 'NNS', 'NNP']:
                if word[0] not in ['package', 'cup', 'teaspoon', 'tablespoon', 'ounce', 'teaspoons', 'pound', 'pounds', 'tablespoons', 'pint', 'pinch', 'cups', 'ounces', 'slices']:
                    if word[0] == 'ground':
                        prep += word[0] + " "
                    else:
                        name += word[0] + " "
                else:
                    msmt += word[0] + " "
            elif word[1] in ['VBD', 'VBN', 'VB']:
                if word[0] == 'taste':
                    desc += 'to ' + word[0] + " "
                else:
                    prep += word[0] + " "
        
        if len(q) > 1:
            msmtPart = quant[2:]
            quant = quant[:2]
            msmt = msmtPart + msmt 
            
        name = name[:-1]
        quant = quant[:-1]
        msmt = msmt[:-1]
        prep = prep[:-1]
        desc = desc[:-1]
        
        ingredientObj = {
            "name": f'{name}',
            "quantity": f'{quant}',
            "measurement": f'{msmt}',
            "preparation": f'{prep}',
            "descriptors": f'{desc}'
        }
        
        ingredients.append(ingredientObj)
        
    return ingredients

def getRecipeSoup(recipeUrl):
    # make web request to recipe web page
    response = requests.get(recipeUrl)
    # initialize beautiful soup object from web response 
    soup = BeautifulSoup(response.text, features="lxml")
    return soup

def getIngredientsList(recipeSoup):
    # access & format the ingredients list
    ingredients = recipeSoup.find_all("li", class_="checkList__line")
    ingredientsResult = []
    for ingredient in ingredients:
        ingredientsResult.append(ingredient.label.text)
    # cut off the "add more ingredients" text from the page
    ingredientsResult = ingredientsResult[:len(ingredientsResult)-3]
    return ingredientsResult

def main(recipeUrl):
    # create soup object that represents the input recipe's web page
    recipeSoup = getRecipeSoup(recipeUrl)
    # access the recipe's title
    recipeTitle = recipeSoup.title.string.split('-')[0]
    # form list of text where ingredients are written from the web page
    ingredientsList = getIngredientsList(recipeSoup)
    # create ingredients objects for each ingredient
    # ingredients object has fields for name, quantity, measurement, preparation, description
    ingredients = getIngredientsObject(ingredientsList)

    print(f'\nRecipe Title: {recipeTitle}\n')

    for ingredient in ingredients:
        print(f'Ingredient Name: {ingredient["name"]}')
        print(f'Ingredient Quantity: {ingredient["quantity"]}')
        print(f'Ingredient Measurement: {ingredient["measurement"]}')
        print(f'Ingredient Preparation: {ingredient["preparation"]}')
        print(f'Ingredient Descriptors: {ingredient["descriptors"]}')
        print('\n')
        
if __name__ == '__main__':
    recipeUrl = input('Provide a url for your recipe: ')
    main(recipeUrl)