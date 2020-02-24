from bs4 import BeautifulSoup
import json
import requests
from nltk import pos_tag, word_tokenize
import sys
from lists import healthList


def makeHealthy(ingredients, recipeTitle):


    print('\nFinding healthy substitutions for your ingredients...')

    print(f'\nRecipe Title: Healthy {recipeTitle}\n')

    healthyIngredients = []

    for ingredient in ingredients:
        if ingredient["name"] in healthList:
            #for every substitution ingredient
            ingredientNumber = 1
            while ingredientNumber < len(healthList.get(ingredient["name"])):
            # adjust quantity
                if healthList.get(ingredient["name"])[ingredientNumber + 1] != 1:
                    quantity = convertFractoFloat(ingredient["quantity"])
                    new_quantity = quantity * float(healthList.get(ingredient["name"])[ingredientNumber + 1])
                    quant = str(new_quantity)

                #change name
                name = healthList.get(ingredient["name"])[ingredientNumber]
                msmt = ingredient["measurement"]
                prep = ingredient["preparation"]
                desc = ""

                ingredientObj = {
                    "name": f'{name}',
                    "quantity": f'{quant}',
                    "measurement": f'{msmt}',
                    "preparation": f'{prep}',
                    "descriptors": f'{desc}'
                }

                healthyIngredients.append(ingredientObj)
                ingredientNumber += 2

        else:
            healthyIngredients.append(ingredient)


    for ingredient in healthyIngredients:
        print(f'Ingredient Name: {ingredient["name"]}')
        print(f'Ingredient Quantity: {ingredient["quantity"]}')
        print(f'Ingredient Measurement: {ingredient["measurement"]}')
        print(f'Ingredient Preparation: {ingredient["preparation"]}')
        print(f'Ingredient Descriptors: {ingredient["descriptors"]}')
        print('\n')


def convertFractoFloat(number):
    total = 0
    num = number.split()
    for n in num:
        frac = n.split('/')
        if len(frac) == 1:
            value = float(frac[0])
        else:
            value = float(frac[0]) / float(frac[1])
        total += value
    return total
