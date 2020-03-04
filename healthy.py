from bs4 import BeautifulSoup
import json
import requests
from nltk import pos_tag, word_tokenize
import sys
from lists import healthList, pasta, healthSubs
from nutritionInfo import tester


def makeHealthy(ingredients, steps, recipeTitle):

    #TEST
    print(ingredients[0])
    for i in ingredients:
        tester(i)


    print('\nFinding healthy substitutions for your ingredients...')

    print(f'\nRecipe Title: Healthy {recipeTitle}\n')

    old_ingredients = []
    healthy_ingredients = []
    # list of foods that got substituted
    substitutions = []
    # list of foods that got removed
    removed = []
    quant = ""

    #switch out pastas
    ingredients, steps, old_pasta = pastaSub(ingredients, steps)


    # switch out ingredients from healthList
    for ingredient in ingredients:
        ingredient["name"] = ingredient["name"].lower()
        if ingredient["name"] in healthList:
            substitutions.append(ingredient["name"])
            #for every substitution ingredient
            ingredientNumber = 1
            while ingredientNumber < len(healthList.get(ingredient["name"])):
            # adjust quantity
                if healthList.get(ingredient["name"])[ingredientNumber + 1] != 1:
                    quantity = convertFractoFloat(ingredient["quantity"])
                    new_quantity = quantity * float(healthList.get(ingredient["name"])[ingredientNumber + 1])
                    quant = str(new_quantity)
                else:
                    quant = ingredient["quantity"]

                #change name
                sub = ingredient["name"]
                name = healthList.get(ingredient["name"])[ingredientNumber]
                msmt = ingredient["measurement"]
                prep = ingredient["preparation"]
                desc = ""

                ingredientObj = {
                    "substitution": f'{sub}',
                    "name": f'{name}',
                    "quantity": f'{quant}',
                    "measurement": f'{msmt}',
                    "preparation": f'{prep}',
                    "descriptors": f'{desc}'
                }

                healthy_ingredients.append(ingredientObj)
                ingredientNumber += 2

        elif ingredient["name"] == 'salt':
            removed.append(ingredient["name"])
            continue
        else:
            old_ingredients.append(ingredient)

    if removed != []:
        print('Removed Ingredients: ' )
    for ingredient in removed:
        print(ingredient)
        print("\n")

    alreadySubbed = []
    for ingredient in healthy_ingredients:
        #print(f'Substitution for {ingredient["sub"]}')
        print(f'Ingredient Name: {ingredient["name"]} (substitution for {ingredient["substitution"]})')
        print(f'Ingredient Quantity: {ingredient["quantity"]}')
        print(f'Ingredient Measurement: {ingredient["measurement"]}')
        print(f'Ingredient Preparation: {ingredient["preparation"]}')
        print(f'Ingredient Descriptors: {ingredient["descriptors"]}')
        print('\n')
        # switch out old ingredients from directions
        if ingredient["substitution"] not in alreadySubbed:
            if ingredient["substitution"] in healthSubs:
                sub = healthSubs.get(ingredient["substitution"])
            else:
                sub = ingredient["name"]

            alreadySubbed.append(ingredient["substitution"])
            indx = 1
            for i in range(len(steps) - 1):
                if ingredient["substitution"] in steps[i]:
                    steps[i] = steps[i].replace(ingredient["substitution"], sub)

    for ingredient in old_ingredients:
        # if spaghetti squash
        if ingredient["name"] == "squash" and ingredient["descriptors"] == "as pasta replacement":
            print(f'Ingredient Name: {ingredient["name"]} (substitution for {old_pasta})')
        else:
            print(f'Ingredient Name: {ingredient["name"]}')
        print(f'Ingredient Quantity: {ingredient["quantity"]}')
        print(f'Ingredient Measurement: {ingredient["measurement"]}')
        print(f'Ingredient Preparation: {ingredient["preparation"]}')
        print(f'Ingredient Descriptors: {ingredient["descriptors"]}')
        print('\n')

    print('Steps to Complete the Recipe: \n')
    indx = 1
    for i in range(len(steps) - 1):
        print(f'Step {indx}: {steps[i]}')
        indx += 1


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


def pastaSub(ingredients, steps):
    old_pasta = ""
    for ingredient in ingredients:
        if ingredient["name"] in pasta:
            old_pasta = ingredient["name"]
            ingredient["name"] = "squash"
            #quant = ingredient["quantity"]
            #msmt = ingredient["measurement"]
            ingredient["preparation"] = ""
            ingredient["descriptors"] = "as pasta replacement"



            indx = 1
            for i in range(len(steps) - 1):
                if (old_pasta in steps[i] or "pasta" in steps[i]) and "boil" in steps[i]:
                    steps[i] = "Bring a large pot of lightly salted water to a boil. Boil squash for about 20 minutes. Once ready, use a fork to separate the flesh into spaghetti-like strings."
                if(old_pasta in steps[i]):
                    steps[i] = steps[i].replace(old_pasta, ingredient["name"])

            return ingredients, steps, old_pasta

    return ingredients, steps, old_pasta
