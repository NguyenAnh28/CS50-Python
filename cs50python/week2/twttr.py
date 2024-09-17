# Ask user for input
sentence = input("Input: ")

# Create a list of characters to be removed
vowels = {"a", "A", "e", "E", "u", "U", "i", "I", "o", "O"}
# Remove the characters from the string
for vowel in vowels:
    if vowel in sentence:
        sentence = sentence.replace(vowel,"")

# Print the final result
print(f"Output: {sentence}")