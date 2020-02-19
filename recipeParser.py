from bs4 import BeautifulSoup
import json
import requests
from nltk import pos_tag, word_tokenize
import sys
from lists import kitchenTools

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
        # print(tokenized)
        
        for word in tokenized:
            if word[1] == 'CD':
                q.append(word[0])
                quant += word[0] + " "
            elif word[1] in ['JJ', 'MD', 'VBZ', 'RB']:
                if word[0] in ['black', 'olive', 'maple', 'green',  'red', 'white', 'beef', 'garlic', 'sour', 'lemon', 'heavy', 'all-purpose', 'large', 'yellow', 'chocolate', 'vegetable']:
                    name += word[0] + " "
                else:
                    if word[0] in ['pinch', 'cup', 'can', 'cans', 'packages', 'fluid', 'squares']:
                        msmt+= word[0] + " "
                    elif word[0] in ['frozen', '3-inch']:
                        prep += word[0] + " "
                    elif word[0] == 'desired':
                        pass
                    else:
                        desc += word[0] + " "
            elif word[1] in ['NN', 'NNS', 'NNP']:
                if word[0] not in ['package', 'cup', 'teaspoon', 'tablespoon', 'ounce', 'teaspoons', 'pound', 'pounds', 'tablespoons', 'pint', 'pinch', 'cups', 'ounces', 'slices', 'packages', 'cloves']:
                    if word[0] in ['ground', 'pieces', 'room', 'temperature']:
                        prep += word[0] + " "
                    else:
                        name += word[0] + " "
                else:
                    msmt += word[0] + " "
            elif word[1] in ['VBD', 'VBN', 'VB', 'VBG']:
                if word[0] == 'taste':
                    desc += 'to ' + word[0] + " "
                elif word[0] == 'cut':
                    prep += word[0] + ' into '
                elif word[0] in ['grapeseed', 'baking', 'cake', 'whipping']:
                    name += word[0] + " "
                elif word[0] in ['needed']:
                    pass
                else:
                    prep += word[0] + " "
        
        if len(q) > 1:
            if q[1] not in ['1/4', '1/2', '3/4', '1/3', '2/3']:
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
        
        # So that we don't add the recipe section names to the ingredients
        if quant != "": 
            ingredients.append(ingredientObj)
        
    return ingredients

def getTools(directionsList):
    tools = []
    for i in range(len(directionsList)):
        tokenized = pos_tag(word_tokenize(directionsList[i]))
        for word in tokenized:
            if (word[1] == 'NN' or word[1] == 'NNS') and word[0] in kitchenTools and word[0] not in tools:
                tools.append(word[0])
    return tools



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

def getDirections(recipeSoup):
    alldirections = []
    directions = recipeSoup.find_all("span", class_="recipe-directions__list--item")
    for direction in directions:
        text = direction.get_text()
        alldirections.append(text)
    return alldirections
    
def getMethods(directionsList):
    methods = []
    for i in range(len(directionsList)):
        # tokenized = pos_tag(word_tokenize(directionsList[i]))
        steps = directionsList[i].split('. ')
        for step in steps:
            tokenized = pos_tag(word_tokenize(step))
            for word in tokenized:
                if word[0] in ['boil', 'heat', 'Bake']:
                    if word[0] not in methods:
                        methods.append(word[0])
                else:
                    pass
    return methods
    
def getSteps(directionsList):
    steps = []
    for i in range(len(directionsList)):
        sentences = directionsList[i].split('. ')
        for sentence in sentences:
            steps.append(sentence)
    return steps
    
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
    # get list of words from recipe directions
    directionsList = getDirections(recipeSoup)
    # get tools from directionsList
    tools = getTools(directionsList)
    # get cooking methods from direcions list
    methods = getMethods(directionsList)
    # get steps from list of directions
    steps = getSteps(directionsList)

    print(f'\nRecipe Title: {recipeTitle}\n')

    for ingredient in ingredients:
        print(f'Ingredient Name: {ingredient["name"]}')
        print(f'Ingredient Quantity: {ingredient["quantity"]}')
        print(f'Ingredient Measurement: {ingredient["measurement"]}')
        print(f'Ingredient Preparation: {ingredient["preparation"]}')
        print(f'Ingredient Descriptors: {ingredient["descriptors"]}')
        print('\n')

    print('Tools: ')
    for tool in tools:
        print(f'{tool}')
    print('\n')
    
    print('Primary Methods: \n')
    for method in methods:
        print(f'Method: {method}')
    print('\n')
    
    print('Steps to Complete the Recipe: \n')
    indx = 1
    for i in range(len(steps) - 1):
        print(f'Step {indx}: {steps[i]}')
        indx += 1


if __name__ == '__main__':
    recipeUrl = input('Provide a url for your recipe: ')
    main(recipeUrl)
