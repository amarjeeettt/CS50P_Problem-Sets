# Define a dictionary 'fruit' where fruit names are keys and calorie values are values
fruit = {
    'apple': 130,
    'avocado': 50,
    'banana': 110,
    'cantaloupe': 50,
    'grapefruit': 60,
    'grapes': 90,
    'honeydew melon': 50,
    'kiwifruit': 90,
    'lemon': 15,
    'lime': 20,
    'nectarine': 60,
    'orange': 80,
    'peach': 60,
    'pear': 100,
    'pineapple': 50,
    'plums': 70,
    'strawberries': 50,
    'sweet cherries': 100,
    'tangerine': 50,
    'watermelon': 80
}

# Prompt the user to input an item (fruit) and store it in the 's' variable
s: str = input('Item: ').lower()

# Check if the input 's' exists as a key in the 'fruit' dictionary
if s in fruit:
    # If the input is found, print the corresponding calorie value
    print(f'Calories: {fruit[s]}')
