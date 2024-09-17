def main():
    # Get the text input
    text = input("Text: ")

    # Convert the text to emojis
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")

    # Print the results
    print(text)



main()  