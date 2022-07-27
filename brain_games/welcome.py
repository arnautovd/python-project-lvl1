import prompt


def welcome():
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    return user_name