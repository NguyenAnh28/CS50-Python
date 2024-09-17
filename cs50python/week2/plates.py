def main():
    #Ask user for input
    plate = input("Plate: ")

    #Evaluate if plate is valid
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    #Returns the value True or False
    if 2 <= len(s) <= 6:
        if s[0].isdigit() or s[1].isdigit(): # Check if first two char is digit
            return False

        if not s.isalnum():
            return False

        for x in range(len(s) - 1):
            if s[x].isalpha(): # Check every character in s
                if s[x+1] == '0':
                    return False

            if s[x].isdigit():
                if s[x+1].isalpha():
                    return False
        return True
    else:
        return False


main()