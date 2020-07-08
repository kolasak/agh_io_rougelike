from configuration import load_configuration
from graphics.Screen import *

if __name__ == "__main__":
    game_map = load_configuration()
    first_stage = game_map[0]

    screen = Screen(first_stage)
    screen.animate()

    for row in game_map:
        print(row)
