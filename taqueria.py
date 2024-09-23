def main():  
    # Dictionary

    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total = 0
    while True:
        try:
            while total >= 0:
                order = input("Item: ").title() # Getting input from user
                
                total = total + menu[order] # Calculate total
                print("Total: $" + str(total))
        except KeyError:
            print(end="")     
        except EOFError:
            break

main()
        
