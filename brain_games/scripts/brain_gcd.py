import prompt
import random
import math


def main():  # noqa: C901
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")
    print("Find the greatest common divisor of given numbers.")
    correct_answers = 0
    while correct_answers < 3:

        num1 = int(random.random() * 100)
        num2 = int(random.random() * 100)
        gcd = math.gcd(num1, num2)
        print(f"Question: {num1} {num2}")
        user_answer = prompt.integer("Your answer: ")
        template_for_answer = f"{user_answer} is wrong answer ;(. Correct answer was"

        if user_answer == gcd:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"{template_for_answer} {gcd}.")
            print(f"Let's try again, {user_name}!")
            break
       
    if correct_answers != 3:
        pass
    else:
        print(f"Congratulations, {user_name}!")


if __name__ == '__main__':
    main()
