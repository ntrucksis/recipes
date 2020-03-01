from bs4 import BeautifulSoup
import json
import requests
from nltk import pos_tag, word_tokenize
import sys
from lists import kitchenTools, kitchenTools_two
from healthy import makeHealthy

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
            elif word[1] in ['JJ', 'MD', 'VBZ', 'RB']:
                if word[0] in ['black', 'olive', 'maple', 'beef', 'garlic', 'sour', 'lemon', 'heavy', 'yellow', 'chocolate', 'vegetable', 'lime', 'angel', 'bread', 'cheese', 'chorizo', 'chipotle', 'jalapeno', 'sazon', 'spaghetti']:
                    name += word[0] + " "
                else:
                    if word[0] in ['pinch', 'cup', 'can', 'cans', 'packages', 'fluid', 'squares', 'teaspoon', 'jars']:
                        msmt+= word[0] + " "
                    elif word[0] in ['frozen', '3-inch', 'finely', 'coarsely']:
                        prep += word[0] + " "
                    elif word[0] in ['nonstick']:
                        desc += word[0] + " "
                    elif word[0] in ['desired', 'such', 'only']:
                        pass
                    else:
                        desc += word[0] + " "
            elif word[1] in ['NN', 'NNS', 'NNP']:
                if word[0] not in ['package', 'cup', 'teaspoon', 'tablespoon', 'ounce', 'teaspoons', 'pound', 'pounds', 'tablespoons', 'pint', 'pinch', 'cups', 'ounces', 'slices', 'packages', 'cloves', 'frying', 'drop', 'packet', 'fluid', 'head', 'inch', 'container', 'cubes', 'cube', 'quart', 'quarts']:
                    if word[0] in ['ground', 'pieces', 'room', 'temperature', 'chunks', 'florets']:
                        prep += word[0] + " "
                    # elif word[0] in ['Pillsbury®', 'Recipe', 'Creations®', 'Campbell\'s®']:
                    elif "®" in word[0]:
                        pass
                    elif word[0] in ['semisweet', 'medium']:
                        desc += word[0] + " "
                    else:
                        name += word[0] + " "
                else:
                    if word[0] in ['frying']:
                        desc += 'for ' + word[0] + ' '
                    else:
                        msmt += word[0] + " "
            elif word[1] in ['VBD', 'VBN', 'VB', 'VBG', 'VBP']:
                if word[0] == 'taste' or 'to':
                    pass
                elif word[0] == 'cut':
                    prep += word[0] + ' into '
                elif word[0] in ['grapeseed', 'baking', 'cake', 'whipping', 'taco', 'seasoning', 'bacon', 'tomato', 'sauce']:
                    name += word[0] + " "
                elif word[0] in ['needed', 'desired']:
                    pass
                else:
                    prep += word[0] + " "
            elif word[1] == 'IN':
                pass

        if len(q) > 1:
            tmp = q[1:]
            print(tmp)
            for element in tmp:
                if element not in ['1/4', '1/2', '3/4', '1/3', '2/3']:
                    msmtPart = element + " "
                    quant = quant[:2]
                    msmt = msmtPart + msmt
                else:
                    pass

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

        if 'cooking spray' in name:
            ingredients.append(ingredientObj)
        # So that we don't add the recipe section names to the ingredients
        if quant != "":
            ingredients.append(ingredientObj)

    return ingredients

def getTools(directionsList):
    toolsBuilder = ""
    for i in range(len(directionsList)):
        tokenized = pos_tag(word_tokenize(directionsList[i]))
        for t in range(len(tokenized)):
            if (tokenized[t][1] == 'NN' or tokenized[t][1] == 'NNS') and tokenized[t][0] not in toolsBuilder:
                #if single word
                if tokenized[t][0] in kitchenTools:
                    toolsBuilder += tokenized[t][0] + ', '
                #if two words
                if t < len(tokenized) - 1:
                    if tokenized[t][0] in kitchenTools_two and tokenized[t+1][0] in kitchenTools_two[tokenized[t][0]]:
                        toolsBuilder += tokenized[t][0] + ' ' + tokenized[t+1][0] + ', '
    toolsBuilder = toolsBuilder[:-2]
    toolsObj = {
        "tools": f'{toolsBuilder}'
    }
    return toolsObj

def getRecipeSoup(recipeUrl):
    # make web request to recipe web page
    response = requests.get(recipeUrl)
    # initialize beautiful soup object from web response
    soup = BeautifulSoup(response.text, features="html.parser") # changed to html.parser so we dont have to install a new one
    return soup

def getIngredientsList(recipeSoup):
    # access & format the ingredients list
    flag = 0
    ingredients = recipeSoup.find_all("li", class_="checkList__line")
    if not ingredients:
        flag = 1
        ingredients = recipeSoup.find_all("span", class_="ingredients-item-name")
    ingredientsResult = []
    if not flag:
        for ingredient in ingredients:
            ingredientsResult.append(ingredient.label.text)
    else:
        for ingredient in ingredients:
            ingredientsResult.append(ingredient.get_text())
    # cut off the "add more ingredients" text from the page
    ingredientsResult = ingredientsResult[:len(ingredientsResult)-3]
    return ingredientsResult

def getDirections(recipeSoup):
    alldirections = []
    directions = recipeSoup.find_all("span", class_="recipe-directions__list--item")
    if not directions:
        directions = recipeSoup.find_all("div", class_="section-body")
    for direction in directions:
        text = direction.get_text()
        alldirections.append(text)
    return alldirections

def getPrimaryMethods(directionsList):
    primaryMethodsBuilder = ""
    for i in range(len(directionsList)):
        directionLower = directionsList[i].lower()
        tokenized = pos_tag(word_tokenize(directionLower))
        for word in tokenized:
            if word[0] in ['bake', 'heat', 'cook', 'boil']:
                if word[0] not in primaryMethodsBuilder:
                    primaryMethodsBuilder += word[0] + ", "
    primaryMethodsBuilder = primaryMethodsBuilder[:-2]
    primaryMethodsObj = {
        "primaryMethods": f'{primaryMethodsBuilder}'
    }
    return primaryMethodsObj

def getSecondaryMethods(directionsList):
    secMethodsBuilder = ""
    for i in range(len(directionsList)):
        directionLower = directionsList[i].lower()
        tokenized = pos_tag(word_tokenize(directionLower))
        for word in tokenized:
            if word[0] in ['mix', 'stir', 'shake', 'pour', 'ladle', 'toss', 'drain', 'top', 'crumble', 'spray', 'combine', 'season']:
                if word[0] not in secMethodsBuilder:
                    secMethodsBuilder += word[0] + ", "
    secMethodsBuilder = secMethodsBuilder[:-2]
    secondaryMethodsObj = {
        "secondaryMethods": f'{secMethodsBuilder}'
    }
    return secondaryMethodsObj

def getSteps(directionsList):
    steps = []
    for i in range(len(directionsList)):
        steps.append(directionsList[i])
    return steps

def buildRepresentation(recipeObj, steps):
    pass

def main(recipeUrl):
    # create soup object that represents the input recipe's web page
    recipeSoup = getRecipeSoup(recipeUrl)
    # access the recipe's title
    recipeTitle = recipeSoup.title.string.split('- ')[0]
    # form list of text where ingredients are written from the web page
    ingredientsList = getIngredientsList(recipeSoup)
    # create ingredients objects for each ingredient
    # ingredients object has fields for name, quantity, measurement, preparation, description
    ingredients = getIngredientsObject(ingredientsList)
    # get list of words from recipe directions
    directionsList = getDirections(recipeSoup)
    # get tools from directionsList
    tools = getTools(directionsList)
    # get primary cooking methods from direcions list
    primaryMethods = getPrimaryMethods(directionsList)
    # get secondary cooking methods from directions list
    secondaryMethods = getSecondaryMethods(directionsList)
    # get steps from list of directions
    steps = getSteps(directionsList)
    # initialize dicitonary that will hold all individual ingredient dictionaries
    ingredDict = {}
    # assign number to each ingredient dictionary and add them to wrapper dictionary
    for i in range(len(ingredients)):
        ingredDict[f'{i}'] = ingredients[i]
    # create large dictionary that holds all ingredients, tools, primary and secondary cooking methdos
    recipeObj = {**ingredDict , **tools , **primaryMethods , **secondaryMethods}

    # build our representation of the steps using the parsed info
    # stepsRep = buildRepresentation(recipeObj, steps)

    # print(recipeObj)
    # print(recipeObj["primaryMethods"])
    # print(recipeObj["0"]["name"])

    print(f'\nRecipe Title: {recipeTitle}\n')

    for ingredient in ingredients:
        print(f'Ingredient Name: {ingredient["name"]}')
        print(f'Ingredient Quantity: {ingredient["quantity"]}')
        print(f'Ingredient Measurement: {ingredient["measurement"]}')
        print(f'Ingredient Preparation: {ingredient["preparation"]}')
        print(f'Ingredient Descriptors: {ingredient["descriptors"]}')
        print('\n')

    print(f'Tools for Recipe: {tools["tools"]}\n')

    print(f'Primary Cooking Methods: {primaryMethods["primaryMethods"]}\n')

    print(f'Secondary Cooking Methods: {secondaryMethods["secondaryMethods"]}\n')

    print('Steps to Complete the Recipe: \n')
    indx = 1
    for i in range(len(steps) - 1):
        print(f'Step {indx}: {steps[i]}')
        indx += 1

    choice = input('Make healthy? (y/n): ')
    if choice == 'y':
        makeHealthy(ingredients, steps, recipeTitle)
        print('\n')

if __name__ == '__main__':
    recipeUrl = input('Provide a url for your recipe: ')
    main(recipeUrl)
