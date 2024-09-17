'''
def main():
    print_bricks(3)

def print_bricks(height):
    for i in range(height):
        print("#")

main()
'''

'''
def main():
    print_row(4)

def print_row(width):
    print("?" * width)

main()
'''

'''
def main():
    print_square(3)

def print_square(size):
    
    # For each row in square 
    for i in range(size):

        # For each column in row 
        for j in range(size):

            # Print bricks
            print("#", end="")

        print()

main()
'''

def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()
