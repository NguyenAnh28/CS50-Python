def main():
    
    name = input("File name: ")

    if name.endswith('.gif' or '.jpg' or '.jpeg'):
        print(f"image/{name[-3:]}")
    elif name.endswith('.pdf' or '.txt' or '.zip'):
        print(f"application/{name[-3:]}")

main()
