import sys
import inflect

p = inflect.engine()

name_list = []

while True:
    try:    
        name = input("Name: ")
        name_list.append(name)
        print(name_list)
    except EOFError:
        print()
        break

'''
while len(name_list) > 0:
    try:       
        if len(name_list) == 1:
            print(f"Adieu, adieu, to {name_list[0]}")
        elif len(name_list) == 2:
            print(f"Adieu, adieu, to {name_list[0]} and {name_list[1]}")
        elif len(name_list) == 3:
            print(f"Adieu, adieu, to {name_list[0]}, {name_list[1]}, and {name_list[2]}")

    except ValueError:
        print("Your list is empty")
        sys.exit(1)
'''
result = p.join(name_list)

if len(name_list) < 1:
    print("Your list is empty")
    sys.exit(1)

print(f"Adieu, adieu, to {result}")