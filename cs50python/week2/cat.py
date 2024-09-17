# Create a program that asks user for input then print meow the same number of times as the input
# Input has to be positive using loop

def main():
    meow(get_n())

def get_n():
    # Loop comes in here
    while True:
        n = int(input("What's n: "))

        if n > 0:
            break
            
    return n
    
def meow(n):
    # Use input n to print meow
    for _ in range(n):
        print("meow")
main()