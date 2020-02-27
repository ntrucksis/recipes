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
    "flour": [1, "whole wheat flour", .5], # half
    "beef": [1, "chicken", 1]
}
