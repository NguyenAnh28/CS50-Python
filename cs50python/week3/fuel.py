def main():
    # Ask user for input
    while True:
        try:
            fuel = input("Fraction: ")
            x, y = fuel.split("/")

        except ValueError:
            print("")
        else:
            try:
                x = int(x)
                y = int(y)
                percent = int(x / y * 100)
            except ZeroDivisionError:
                print("Can't divide by zero")
            if percent > 100:
                ValueError
            else: 
                break
            
    
    if 1 < percent < 100:
        print(f"{percent}%")
    elif 0 <= percent <= 1:
        print("E")
    elif 99 <= percent <= 100:
        print("F")
   


main()