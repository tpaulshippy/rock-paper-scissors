"""
Rock, Paper, Scissors game
"""
import time
from getkey import getkey, keys

def play(first, second) -> str:
    """
    Play Rock, Paper, Scissors and determine winner
    """
    if (first == "r" or second == "r") and (first == "s" or second == "s"):
        return "r"

    if (first == "s" or second == "s") and (first == "p" or second == "p"):
        return "s"

    if (first == "p" or second == "p") and (first == "r" or second == "r"):
        return "p"

class Program:
    def start(self):
        print("Ready to play? Type 'r' for rock, 'p' for paper, or 's' for scissors.")
        key = getkey()
        key2 = getkey()

        time.sleep(5)

        winner = play(key, key2)

        if winner == "r":
            print("Rock wins!")
        elif winner == "s":
            print("Scissors wins!")
        elif winner == "p":
            print("Paper wins!")
        else:
            print("Nobody wins!")

if __name__ == '__main__':
    program = Program()
    program.start()
