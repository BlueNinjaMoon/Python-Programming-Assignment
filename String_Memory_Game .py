import time
import msvcrt
import os

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
        gameresult.append(True)
    else:
        print("Game over.")
        gameresult.append(False)
        gameresult.append(guess)    

def print_game(lvl:int, string:str):
    print(f"Level {lvl}, the string is {string}.")
    tim = str("ABCDE")
    for i in range(5):
        time.sleep(1)
        print("•",end=" ",flush=True)
    clear_keyboard_buffer()
    os.system("cls")

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

def play_again():
    user = input("Would you like to play again? (Y/y or N/n): ").strip().upper()
    while True:
        if user == "Y":
            return "Y"
        elif user == "N":
            return "N"
        else:
            while user != "Y" or "N":
                print("Incorrect input, must be Y/y or N/n.")
                user = input("Would you like to play again? (Y/y or N/n): ").strip().upper()
        
max = 4
lvl = 0
playagain = "Y"
while playagain == "Y":
    gameresult = []
    randstr = generate_random_str(max)
    print_game(lvl, randstr)
    game(lvl, randstr)
    if gameresult[0] == False:
        print(f"Correct string: {randstr}")
        print(f"Your answer: {gameresult[1]}")
        max += 1
        if lvl > 0 or lvl <= 2:
            print(f"Wow, did you understand the game?")
        else:
            if lvl >= 3 or lvl <= 6:
                print(f"Not bad, keep working at it")
            else:
                if lvl >= 7:
                    print("Nice Job! You're a memory master!")
        playagain = play_again()
    else:
        lvl += 1
        print(f"You made it to Round {lvl}.")
        lvl = 0
        playagain = play_again()