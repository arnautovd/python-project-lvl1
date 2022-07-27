import prompt
import random
from brain_games.welcome import welcome

def main():  # noqa: C901
    user_name = welcome()
    correct_answers = 0
    while correct_answers < 3:

        user_number = int(random.random() * 100)
        print(f"Question: {user_number}")
        user_answer = prompt.string("Your answer: ")

        if user_number % 2 == 0 and user_answer == 'yes':
            print('Correct!')
            correct_answers += 1
        elif user_number % 2 != 0 and user_answer == 'no':
            print('Correct!')
            correct_answers += 1
        else:
            if user_answer == "yes":
                print(f"{user_answer} is wrong answer ;(. Correct answer was 'no'.")
                print(f"Let's try again, {user_name}!")
            elif user_answer == "no":
                print(f"{user_answer} is wrong answer ;(. Correct answer was 'yes'.")
                print(f"Let's try again, {user_name}!")
            elif user_answer != "yes" and user_answer != "no":
                print(f"{user_answer} is wrong answer")
                print(f"Let's try again, {user_name}!")
            break
    if correct_answers != 3:
        pass
    else:
        print(f"Congratulations, {user_name}!")


if __name__ == '__main__':
    main()
