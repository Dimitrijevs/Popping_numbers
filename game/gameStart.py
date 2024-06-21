from game.terminal import clear_screen

def level_select():
    while True:
        try:
            level = int(input("Plese select a level to start. 1 to 4: "))
            if level not in range(1, 5):
                raise ValueError(
                    "Invalid number. Plese select a level to start. From 1. to 4: "
                )
            break
        except ValueError as e:
            print(e)

    return level


def enemy_select():
    clear_screen()

    print("Enemy is active, he will try to get more points than you!")
    print("Oh, and his name is Average Joe. Good luck!")
    print("Average Joe will make his move after your move. \n")


def game_start():
    print("Welcome to the Popping Numbers game!")
    print("Instructions:")
    print("1. You can choose a number and position where to place it.")
    print("2. After your turn, 3 random numbers will appear in random places.")
    print("3. Create a row of the same numbers to make them disappear and earn points.")
    print("4. The game ends when there are no more places to put numbers.")
    print("5. Good luck!")