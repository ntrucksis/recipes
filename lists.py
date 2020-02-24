# kitchen tools list

kitchenTools = ['barbecue', 'colander', 'grill','baster', 'beanpot',
'brush','blender','basket', 'bowl','knife','pan', 'baking', 'sheet', 'colander', 'timer', 'poacher', 'grater', 'griddle', 'mixer', 'juicer', 'microwave', 'oven', 'peeler',
'pot', 'strainer', 'steamer', 'skillet', 'scissors', 'sieve', 'skewer', 'tongs', 'whisk',
'wok', 'zester']

# kitchen tools with two words
kitchenTools_two = {
    "food": ["processor"],
    "cookie": ["cutter", "sheet", "sheets"],
    "bread": ["knife"],
    "cheese": ["grater, cutter, knife"]
}

# healthy food substitutions
# key is the unhealthy item
# value: number of substitutions, sub name, quantity amount
# ex: "butter": [2, "almond butter", .5, "coconut oil", .5] --> 1/2 cup almond butter & 1/2 cup coco oil per cup butter
healthList = {
    "bread crumbs": [1, "rolled oats", 1],
    "butter": [2, "almond butter", .5, "coconut oil", .5], # add measurements and oil, also cooking spray
    "cream": [1, "evaporated skim milk", 1],
    "cream cheese": [1, "low-fat cottage cheese", 1], # pureed
    "eggs": [1, "egg whites", 2], # 2 egg whites
    "flour": [1, "whole wheat flour", .5] # half
}

# top ingedients for each cuisine so we know how to transform and classify recipes
cuisines = {
    "brazilian": ["onions", "olive oil", "lime", "coconut milk", "totatoes", "condensed milk"],
    "british": ["flour", "butter", "milk" "eggs", "heavy cream", "baking powder", "unsalted butter"],
    "cajun": ["garlic", "green bell pepper", "butter", "andouille sausage", "creole seasoning", "cajun seasoning", "celery ribs", "celery"],
    "chinese": ["soy sauce", "sesame oil", "corn starch", "sugar", "five-spice powder","hoisin sauce", "oyster sauce", " peanut oil"],
    "filipino": ["garlic", "onions", "soy sauce", "cooking oil", "bay leaf", "bay leaves", "fish sauce"],
    "french": ["sugar", "flour", "unsalted butter", "olive oil", "shallots"],
    "greek": ["olive oil", "dried oregano", "garlic cloves", "garlic", "oregano", "feta cheese", "feta", "cucumber", "lemon juice"],
    "indian": ["onions", "garam masala", "ground turmeric", "turmeric", "masala", "tikki masala", "garam masala", "cumin seed", "green chilies"],
    "irish": ["flour", "butter", "onions", "potatoes", "buttermilk", "baking powder", "milk"],
    "italian": ["olive oil", "garlic cloves", "garlic", "grated parmesan", "parmesan", "basil", "e.v. olive oil", "black pepper"],
    "jamaican": ["onions", "garlic", "ground allspice", "allspice", "thyme"],
    "japanese": ["soy sauce", "mirin", "sugar", "shichimi", "sake", "rice vinegar", "scallions"],
    "korean": ["soy sauce", "sesame oil", "garlic", "green onions", "sugar", "gochujang", "kimchi", "toasted sesame seeds", "sesame seeds", "sesame oil"],
    "mexican": ["onions", "ground cumin", "cumin", "garlic", "olive oil", "adobo", "corn tortillas", "salsa", "flour tortilla", "tortilla", "black beans", "avocado"],
    "moroccan": ["olive oil", "ground cumin", "cumin", "onions", "garlic cloves", "garlic", "couscous", "chickpeas", "ground ginger", "cinnamon", "ginger", "coriander"],
    "russian": ["sugar", "onions", "flour", "sour cream", "beets", "dill", "potatos"],
    "southern": ["butter", "flour", "sugar", "eggs", "buttermilk", "baking soda", "baking powder", "vanilla extract", "milk"],
    "spanish": ["olive oil", "garlic cloves", "garlic", "e.v. olive oil", "e.v. olive oil", "white wine", "red bell pepper", "parsley", "tomatoes"],
    "thai": ["fish sauce", "garlic", "coconut milk", "vegetable oil", "lemongrass", "peanuts", "lime juice"],
    "vietnamese": ["fish sauce", "sugar", "garlic", "beansprouts", "cucumber", "rice vinegar", "lemongrass"],
}


# master list of types of ingredients so we know how to replace them
meat = ["lamb", "chicken", "steak", "fish", "tuna", "salmon", "ribeye", 
"rib-eye", "flank", "bacon", "pork", "beef", "duck", "turkey", "ham", 
"mutton", "sausage", "poultry", "venison", "red meat", "veal", "white meat", 
"goat", "anchovy", "hot dog", "salami", "meatball", "quail", "breast", "chicken breast", 
"chicken thigh", "chicken wing", "liver", "andouille sausage"]

seafood = ["oyster", "clam", "mussel", "fish", "eel", "salmon", "trout", "shrimp",
 "swordfish", "tuna", "tilapai", "carp", "cod", "octopus", "herring", "squid", "catfish",
  "lobster", "anchovy", "scallop", "mahi-mahi", "crayfish", "oyster", "roe", "caviar",
   "monkfish", "abalone", "skate", "mackerel"]

pasta = ["spaghetti", "fettuccine", "lunguine", "penne", "rigatoni", "orecchiette",
 "farfalle", "pappardelle", "fusilli", "rigatoni", "orzo", "tortellini", "ziti", 
 "ravioli", "macaroni", "cappelletti", "lasagne", "gnocci", "rotini"]

grains = ["rice", "barley", "quinoa", "oat", "millet", "maize", 
"rye", "whole grain", "wild rice", "brown rice", "white rice"]

sauce = ["alfredo", "marinara", "soy sauce", "mushroom sauce", "steak sauce",
 "barbecue", "bbq", "sauce", "salsa", "hollandaise", "mayonnaise", "cocktail sauce",
  "hot sauce", "peanut sauce", "bechamel sauce", "bechamel", "sweet and sour", "oyster sauce",
  "tomato sauce", "hoisin", "hoisin sauce", "pesto", "pesto sauce", "tartar", "chimichurri", 
  "creole sauce", "worcestershire", "mirin", "katchup", "relish", "hoisin sauce", "fish sauce"]

seasoning = ["pepper", "salt", "cinnamon", "chili powder", "ground cinnamon", 
"chili flakes", "cumin", "ginger", "ground ginger", "nutmeg", "paprika", 
"oregano", "dried oregano", "bay leaf", "bay leaves", "cayenne", 
"cayenne pepper", "paprika", "tarragon", "creole seasoning", "cajun seasoning"]

spices = ["adobo", "chili powder", "masala", "five-spice powder", "curry powder",
 "allspice", "lemon pepper", "taco", "shichimi", "old bay", "tikki masala", "tandoori masala", "garlic salt",
 "nutmeg", "ginger", "saffron", "turmeric", "cumin", "cardamom", "mace", "fenugreek", "vanilla", "paprika",
 "fennel", "clove", "garlic", "black pepper", "coriander", "star anise", "anise", "mustard seed", "garam masala",
  "chili powder", "onion powder"]

herbs = ["basil", "parsley", "rosemary", "thyme", "oregano", "sage", "chives", "mint", "dill", "lavender", "tarragon", "majoram", "coriander", 
"fennel", "chervil", "lemongrass", "cilantro", "pepperming", "chamomile", "anise", "arugula"]

fats = ["olive oil", "almond butter", "butter", "unsalted butter", "e.v. olive oil", "avocado oil",
 "sesame oil", "almond oil", "sunflower oil", "peanut oil", "canola oil", "grapeseed oil", "soybean oil",
 "whipped butter", "european style butter", "peanut butter", "sesame oil"]

dairy = ["milk", "goat milk", "yogurt", "ice cream", "cottage cheese", "buttermilk",
"sour cream", "cream cheese", "oat milk", "almond milk", "soy milk", "heavy cream", "coconut milk"]

cheese = ["cheese", "parmesan", "parmesan cheese", "feta", "goat cheese", "feta cheese",
 "blue cheese", "cheddar cheese", "gouda cheese", "camembert", "queso", "asiago cheese",
  "mascarpone", "monterey jack cheese", "provolone", "gorgonzola", "cream cheese"]

vegetables = ["asparagus", "lettuce", "celery", "brussels sprout", "broccoli", "cabbage", "spinach", "potato", "carrot", "kale", "curly kale",
"okra", "artichoke", "radish", "rhubarb", "pumpkin", "watercress", "cauliflower", "onion", "eggplant", "beetroot", "tomato", "parsnip", "arugula",
"cucumber", "pea", "turnip", "collard", "sweet potato", "ginger", "chives", "bean", "black beans", "pinto beans", "corn", "sweet corn",
"chesnut", "bok choy", "dill", "wasabi", "zucchini", "leek", "shallot", "beets", "beansprouts"]

fruits = ["berry", "apple", "papaya", "blueberry", "raspberry", "pear", "pineapple", "mango",
 "apricot", "avocado", "banana", "cherry", "lemon", "grapefruit", "orange", "grape", "pomegranate", 
 "tangerine", "plum", "tomato", "watermelon", "clementine", "strawberry", "kiwi", "elderberry", "cranberry",
  "blackberry", "lime"]

toppings = ["sesame seeds", "toasted sesame seeds"]