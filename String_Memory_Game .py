import time
import msvcrt

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
    guess = input("Enter the string you just saw (Case Insensitive): ").strip().upper()
    if check_win(guess, rand) == True:
        print("Next round!")
    else:
        print("Game over.")
    

def print_game(lvl:int, string:str):
    print(f"Level {lvl}, the string is {string}.")
    tim = str("ABCDE")
    for i in tim:
        time.sleep(1)
        print("•",end=" ")
    clear_keyboard_buffer()

def check_win(guess:str, correct:str):
    if guess == correct:
        print("Correct!")
        guess = True
    else:
        print("Incorrect.")
        guess = False
    return guess

def clear_keyboard_buffer():
    """Remove any pending keystrokes from the keyboard buffer."""
    while msvcrt.kbhit():
        msvcrt.getwch()

max = 4
lvl = 0
#while True:
randstr = generate_random_str(max)
print_game(lvl, randstr)
game(lvl, randstr)

#user = userguess("")