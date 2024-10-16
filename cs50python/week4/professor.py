import random

def main():     
    level = get_level()
    questions_amount = 0
    correct_answer = 0
    while questions_amount <= 10:
        incorrect_answer = 0
        x, y, answer = generate_integer(level)
        user_answer = input(f"{x} + {y} = ")
        if user_answer == answer:
            correct_answer += 1
            questions_amount += 1
            if questions_amount == 10:
                break
        while user_answer != answer:
            print("EEE")
            incorrect_answer += 1
            if incorrect_answer == 3:
                print(f"{x} + {y} = {answer}")
                break
            user_answer = input(f"{x} + {y} = ")
            if user_answer == answer:
                break


    print(f"Score: {correct_answer}")

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n == 1 or n == 2 or n == 3:
                return n
        except ValueError:
            pass

def generate_integer(level):
    # X and Y has n digits 
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
        answer = x + y 
    elif level == 2:
        x = random.randint(0,99)
        y = random.randint(0,99)
        answer = x + y
    elif level == 3:
        x = random.randint(0,999)
        y = random.randint(0,999)
        answer = x + y
    answer = str(answer)
    return x, y, answer


if __name__ == "__main__":
    main()