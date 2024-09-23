def main():
    grocery_list = {}   

    # Loop 
    while True:
        try:
            item = input().strip().lower() # Ask user for input
            item = item.upper()
            
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1

        except EOFError:
            break

    for item in sorted(grocery_list):
        print(grocery_list[item], item)

main()