import time

def generate_random_str(maxstring:int) -> str:
    """
    Generates a random string (length is determined by the int inputed.)
    """
    from random import choice
    randstring = ""
    while maxstring != 0:
        randstring = randstring + choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        maxstring -= 1
    return randstring

def game(lvl:int, rand:str):
    print("")

def print_game(lvl:int, string:str):
    print(f"Level {lvl}, the string is {string}.")
    

def check_win(guess:str, correct:str):
    if guess == correct:
        print("Correct!")
    else:
        print("Incorrect.")

def clear_keyboard_buffer():
    print("")

max = 4
lvl = 0
#while True:
randstr = generate_random_str(max)
print_game(lvl, randstr)
game(lvl, randstr)

#user = userguess("")