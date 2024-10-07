import random

def main():

    level = promptUser()
    N = random.randint(1, n)    
    guessGame(N)


def guessGame(N):
    guess = -1
    while guess != N:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                if guess > N:
                    print("Too large!")
                elif guess < N:
                    print("Too small!")
                else: 
                    print("Just right!")
        except ValueError:
            pass

# If user does not input positive int, prompt again
def promptUser():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
        except ValueError:
            pass

# This comment is to test GitHub

main()


