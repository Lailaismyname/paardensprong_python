from tabulate import tabulate
from pyfiglet import Figlet
from colorama import Fore
from cowpy import cow
import random
import sys
import os

def main():
    while True:
        option = render_start_screen()
        run_option(option)


def render_start_screen():
    """"This is a function that renders the starting screen of the game"""
    #Setting color to Magenta
    print(Fore.MAGENTA,"",end="")
    #Printing the title of the game
    figlet = Figlet()
    figlet.setFont(font="epic")
    print(figlet.renderText("Horse"))
    print(figlet.renderText("Jump"))
    #Setting color back to white
    print(Fore.WHITE,"")
    #Printing the start screen options
    table = [["Start","S"],["Help","H"],["Quit","ctrl + d"]]
    header =["Option","Command"]
    print(tabulate(table, header, tablefmt="double_grid"))
    while True:
        try:
            option = input("")
        except EOFError:
            #clearing the screen
            os.system("clear")
            cow_cls = cow.get_cow('budfrogs')
            cheese = cow_cls()
            msg = cheese.milk("Thanks for playing, have a nice day!")
            sys.exit(msg)
        if option == "s" or option == "S":
            #clearing the screen
            os.system("clear")
            return "start"
        elif option == "h" or option == "H":
            #clearing the screen
            os.system("clear")
            return "help"

def run_option(option):
    """This is a function runs the option that the users has choses
        Args: Option chosen by user"""
    #clearing the screen
    os.system("clear")
    #running options
    if option == "start":
        #Play the game
        streak = 0
        try:
            while True:
                if play_game(streak):
                    streak += 1
                else:
                    break
        except EOFError:
            #clearing the screen
            os.system("clear")
            return
    elif option == "help":
        #Print help screen
        give_explanation()


def play_game(streak):
    """This is a function that renders the game
        Args: streak, the amount of times the user has guessed the word to keep track of the guessed words"""
    word = render_game(streak)
    #print(word)
    if check_guess(word):
        return True


def get_word():
    """This function gets the words from a text file, and returns a random 9 letter word"""
    wordlist = []
    with open('words.txt') as reader:
        for line in reader:
            wordlist.append(line.replace("\n",""))
    random.shuffle(wordlist)
    word = wordlist[0].lower()
    return word

def get_template(word):
    """This is a function that generates the templates for the letters to be filled in.
        Args: Word, the word to be used"""
    sequences = [
        [[word[0],word[5],word[2]],[word[3]," ",word[7]],[word[6],word[1],word[4]]],
        [[word[0],word[3],word[6]],[word[5]," ",word[1]],[word[2],word[7],word[4]]],
        [[word[3],word[0],word[5]],[word[6]," ",word[2]],[word[1],word[4],word[7]]],
        [[word[5],word[0],word[3]],[word[2]," ",word[6]],[word[7],word[4],word[1]]],
        [[word[6],word[3],word[0]],[word[1]," ",word[5]],[word[4],word[7],word[2]]],
        [[word[2],word[5],word[0]],[word[7]," ",word[3]],[word[4],word[1],word[6]]],
        [[word[3],word[6],word[1]],[word[0]," ",word[4]],[word[5],word[2],word[7]]],
        [[word[5],word[2],word[7]],[word[0]," ",word[4]],[word[3],word[6],word[1]]],
        [[word[7],word[2],word[5]],[word[4]," ",word[0]],[word[1],word[6],word[3]]],
        [[word[1],word[6],word[3]],[word[4]," ",word[0]],[word[7],word[2],word[5]]],
        [[word[2],word[7],word[4]],[word[5]," ",word[1]],[word[0],word[3],word[6]]],
        [[word[6],word[1],word[4]],[word[3]," ",word[7]],[word[0],word[5],word[2]]],
        [[word[1],word[4],word[7]],[word[6]," ",word[2]],[word[3],word[0],word[5]]],
        [[word[7],word[4],word[1]],[word[2]," ",word[6]],[word[5],word[0],word[3]]],
        [[word[4],word[7],word[2]],[word[1]," ",word[5]],[word[6],word[3],word[0]]],
        [[word[4],word[1],word[6]],[word[7]," ",word[3]],[word[2],word[5],word[0]]],
        ]
    random.shuffle(sequences)
    template = sequences[0]
    return template


def render_game(guessed):
    """This is a function that renders the gamescreen
        Args: guessed, nr of correctly guessed words so far."""
    # amount of lives
    horse = "🐴"
    streak = guessed * horse
    if guessed != 0:
        print(f"Streak: {streak}")
    else:
        print(f"Streak: 0")
    #get_word
    word = get_word()
    # get board template
    template = get_template(word)
    #print the board
    #Setting color to Magenta
    print(Fore.MAGENTA)
    print(tabulate(template, tablefmt="double_grid"))
    #Setting color to Magenta
    print(Fore.WHITE)
    return word


def check_guess(word):
    """This is a function that checks wether the word the user guessed is the right word
        Args: word, the current word that needs to be guessed"""
    while True:
        guess = input("")
        if guess == word:
            #clearing the screen
            os.system("clear")
            return True

def give_explanation():
    """This function provides an explanation to the user"""
    print("The boxes are filled following a pattern similar to the jump a horse would make on a chessboard. \nSo if the word is pythonic it would go as this: ")
    example1 = [["p","-","-"],["-"," ","-"],["-","-","-"]]
    print(tabulate(example1, tablefmt="double_grid"))
    example2 = [["p","-","-"],["-"," ","-"],["-","y","-"]]
    print(tabulate(example2, tablefmt="double_grid"))
    print("Et cetera, and the final result will be:")
    example = [["p","n","t"],["h"," ","c"],["i","y","o"]]
    print(tabulate(example, tablefmt="double_grid"))
    print("Your goal is to guess the word by reverse engineering this process. Or by any other way you see fit")
    while True:
        try:
            back = input("Press B to go back: ")
        except EOFError:
            os.system("clear")
            return True
        if back == "B" or back == "b":
            #clearing the screen
            os.system("clear")
            return True

if __name__ == "__main__":
    main()