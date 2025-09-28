# rpg_game.py

import time
import sys

def slow_print(text, delay=0.03):
    """Print text slowly for dramatic effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def intro():
    slow_print("\n🌲 You wake up in a dark, damp forest. You have no memory of how you got here.")
    slow_print("The wind howls. You hear faint whispers between the trees...")
    slow_print("You see two paths ahead of you.")
    choice = input("Do you take the (L)eft path or the (R)ight path? ").strip().lower()

    if choice == 'l':
        path_left()
    elif choice == 'r':
        path_right()
    else:
        slow_print("You hesitate for too long... a shadow emerges and ends your journey.")
        game_over("You were lost to the forest.")


def path_left():
    slow_print("\n🌿 You walk down the left path. It's quiet... too quiet.")
    slow_print("Suddenly, a wild wolf appears! 🐺")
    choice = input("Do you (F)ight or (R)un? ").strip().lower()

    if choice == 'f':
        fight_wolf()
    elif choice == 'r':
        slow_print("You run as fast as you can and barely escape. You stumble upon a cabin.")
        cabin_scene()
    else:
        game_over("You froze, and the wolf didn’t wait.")


def fight_wolf():
    slow_print("You grab a stick from the ground and prepare to fight...")
    slow_print("After a fierce battle, you're injured but victorious.")
    slow_print("You limp forward and find a hidden path leading to an old cabin.")
    cabin_scene()


def cabin_scene():
    slow_print("\n🏚️ The old cabin creaks as you approach.")
    choice = input("Do you go (I)nside or (L)eave it alone? ").strip().lower()

    if choice == 'i':
        slow_print("Inside, you find food, bandages, and a map. You're saved!")
        game_won("You survived and escaped the forest!")
    elif choice == 'l':
        slow_print("You ignore the cabin, but soon get lost in the woods again.")
        game_over("You wandered until exhaustion took you.")
    else:
        game_over("Indecision leads to your doom in the forest.")


def path_right():
    slow_print("\n🌌 You take the right path, which leads to a glowing lake.")
    slow_print("You see a boat and a figure standing next to it.")
    choice = input("Do you (T)alk to the figure or (S)neak past? ").strip().lower()

    if choice == 't':
        talk_to_figure()
    elif choice == 's':
        sneak_past()
    else:
        game_over("Confused, you trip and fall into the lake... forever lost.")


def talk_to_figure():
    slow_print("\n👤 The figure is an old man. He says he knows the way out.")
    choice = input("Do you (T)rust him or (R)efuse? ").strip().lower()

    if choice == 't':
        game_won("He leads you safely out of the forest. You are free!")
    elif choice == 'r':
        game_over("You walk away, and the forest consumes you.")
    else:
        game_over("Silence is not always golden. He disappears. You're alone again.")


def sneak_past():
    slow_print("You sneak around the lake...")
    slow_print("Suddenly, the ground crumbles and you fall into a pit.")
    game_over("No one hears your screams. The end.")


def game_over(reason):
    slow_print(f"\n💀 GAME OVER: {reason}")
    play_again()


def game_won(message):
    slow_print(f"\n🎉 YOU WIN: {message}")
    play_again()


def play_again():
    choice = input("\nWould you like to play again? (Y/N): ").strip().lower()
    if choice == 'y':
        intro()
    else:
        slow_print("Thanks for playing! 🌟")
        exit()


if __name__ == "__main__":
    intro()
