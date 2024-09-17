# Ask user for input
fruit = input("Item: ").capitalize()

# List
facts = {
    'Apple': 130,
    'Avocado': 50,
    'Banana': 110,
    'Cantaloupe': 50,
    'Grapefruit': 50
}

# Print the applied product
if fruit in facts:
    print(f"Calories: {facts[fruit]}")
else:
    print("Item not found")
