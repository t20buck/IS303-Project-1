"""
-------------------------------
Women's Soccer Season Simulator
-------------------------------
This program simulates a women's soccer season for a user-selected home team.
The user picks their team from a list of real NWSL/college teams, selects opponents,
and the program simulates games with random scores (no ties allowed).

Authors: Tye, Tanner, and Kyle

"""

# Import Libraries
import random

# My fun true variables
Gospel = True
Alive = True
Single = True

def introduction():
    # Displays a welcome message
    # And explains the rules
    print("=" * 55)
    print("   Welcome to the Women's Soccer Season Simulator!")
    print("=" * 55)
    print("\nHow it works:")
    print("  1. Enter your home team ")
    print("  2. Select opponents for each game you want to play.")
    print("  3. Scores are randomly generated — no ties allowed!")
    print("  4. At the end, see your season record and standing.\n")

    name = input("Before we begin, what is your name? ").strip().upper()
    print(f"\nWelcome, {name}! Let's build your season.\n")
    return name

def menu():
    # Displays the menu 
    # returns the choice
    print("\n--- MAIN MENU ---")
    print("1. Play a Season")
    print("2. Quit")
    while Alive:
        choice = input("Enter your choice: ").strip()
        if choice in ("1","2"):
            return choice
        print("Invalid choice. Please enter a number option.")

