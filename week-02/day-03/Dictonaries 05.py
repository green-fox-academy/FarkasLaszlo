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
    second_length = len(' Needs cooling ')
    third_length = len(' In stock ')
    plus = '+'
    minus = '-'
    space = ' '
    separator = '|'

    stock = []
    cool_list = []
    for i in range(len(ingredients)):
        if len(first_length) < len(ingredients[i]['name']):
            first_length = ingredients[i]['name']
        if ingredients[i]['needs_cooling'] == True:
            cool_list.append('Yes')
        else:
            cool_list.append('No')
        if ingredients[i]['in_stock'] == 0:
            stock.append('-')
        else:
            stock.append(str(ingredients[i]['in_stock']))


    print(plus + minus * (len(first_length) + 2) + plus + minus * second_length + plus + minus * third_length + plus)
    print(separator + space + 'Ingredient' + space * (len(first_length) - len('Ingredient ') + 2) +
    separator + ' Needs cooling ' + separator + ' In stock ' + separator)
    print(plus + minus * (len(first_length) + 2) + plus + minus * second_length + plus + minus * third_length + plus)

    for i in range(len(ingredients)):
        print(separator + space + ingredients[i]['name'] + space * (len(first_length) - len(ingredients[i]['name']) + 1) 
        + separator + space+cool_list[i] + space * (second_length - 1 - len(cool_list[i])) + separator + space + stock[i] +
        space * (third_length - 2) + separator)
    print(plus + minus * (len(first_length) + 2) + plus + minus * second_length + plus + minus * third_length + plus)


box(ingredients)
