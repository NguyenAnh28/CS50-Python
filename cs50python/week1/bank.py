# Input the greetings
greeting = input("Greeting: ")

# If commands
if greeting == 'Hello':
    print("$100")
elif greeting[0] == 'H' or greeting[0] == 'h':
    print("$20")
else:
    print("$0")