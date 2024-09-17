def main():
    # Ask user for input
    camelCase = input("camelCase: ")
    snake_case = change_case(camelCase)
    print(f"snake_case: {snake_case}")
    # Function for converting camelcase to snakecase
def change_case(word):
    snake_case = ""
    for char in word:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    return snake_case
main()
