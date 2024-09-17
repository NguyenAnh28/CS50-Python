def main(): 
    name = input("what is your name? ")

    match name:
        case "Harry" | "Ron" | "Hermione":
            print("Griffindor")
        case "Draco":
            print("Slytherin")
        case _:
            print("Who?")
main()