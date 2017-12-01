# Create a function that prints the ingredient list of dictionaries to the console in the following format:
#
# +--------------------+---------------+----------+
# | Ingredient         | Needs cooling | In stock |
# +--------------------+---------------+----------+
# | vodka              | Yes           | 1        |
# | coffee_liqueur     | Yes           | -        |
# | fresh_cream        | Yes           | 1        |
# | captain_morgan_rum | Yes           | 2        |
# | mint_leaves        | No            | -        |
# +--------------------+---------------+----------+
#
# OPTIONAL:
# The frist columns should be automatically as wide as the longest key

ingredients = [
	{ "name": "vodka", "in_stock": 1, "needs_cooling": True },
	{ "name": "coffee_liqueur", "in_stock": 0, "needs_cooling": True },
	{ "name": "fresh_cream", "in_stock": 1, "needs_cooling": True },
	{ "name": "captain_morgan_rum", "in_stock": 2, "needs_cooling": True },
	{ "name": "mint_leaves", "in_stock": 0, "needs_cooling": False },
	{ "name": "sugar", "in_stock": 0, "needs_cooling": False },
	{ "name": "lime juice", "in_stock": 0, "needs_cooling": True },
	{ "name": "soda", "in_stock": 0, "needs_cooling": True },
	{ "name": "water", "in_stock": 0, "needs_cooling": True },
	{ "name": "something with very long name", "in_stock": 1, "needs_cooling": False },
	{ "name": "cola", "in_stock": 0, "needs_cooling": True }
]
def box(ingredients):
    first_length = []
    second_length = len(" Needs cooling ")
    third_length = len(" In stock ")

    stock = []
    cool_list = []
    for i in range(len(ingredients)):
        if len(first_length)<len(ingredients[i]['name']):
            first_length = ingredients[i]['name']
        if ingredients[i]['needs_cooling'] == True:
            cool_list.append("Yes")
        else:
            cool_list.append("No")
        if ingredients[i]['in_stock'] == 0:
            stock.append("-")
        else:
            stock.append(str(ingredients[i]['in_stock']))


    print("+"+"-"*(len(first_length)+2)+"+"+"-"*second_length+"+"+"-"*third_length+"+")
    print("|"+" "+"Ingredient"+" "*(len(first_length)-len("Ingredient ") +2)+"|"+" Needs cooling "+"|"+" In stock "+"|")
    print("+"+"-"*(len(first_length)+2)+"+"+"-"*second_length+"+"+"-"*third_length+"+")

    for i in range(len(ingredients)):
        print("|"+" "+ingredients[i]['name']+" "*(len(first_length)-len(ingredients[i]['name']) +1)+"|"+" "+cool_list[i] +" "*(second_length-1-len(cool_list[i]))+"|"+" "+stock[i]+" "*(third_length-2)+"|")
    print("+"+"-"*(len(first_length)+2)+"+"+"-"*second_length+"+"+"-"*third_length+"+")


box(ingredients)
