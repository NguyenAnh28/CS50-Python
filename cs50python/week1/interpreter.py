# Output is a float, 1 decimal place

def main():
    # Ask for input
    expression = input("Expression: ")

    # Define x y z
    x, y, z = expression.split()
    x = float(x)
    z = float(z)
    
    if y == '+':
        print(x + z)
    elif y == '-':
        print(x - z)
    elif y == '*':
        print(x * z)
    elif y == '/':
        print(x / z)
        
main()