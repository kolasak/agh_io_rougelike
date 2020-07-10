import pygame
from character.CharacterInfo import CharacterInfo
from character.items.Backpack import Backpack
from character.items.Laptop import Laptop
from character.items.Sword import Sword
from configuration import load_configuration
from graphics.Screen import Screen
from graphics.views.CharacterInfoView import CharacterInfoView
from graphics.views.BattleView import BattleView
from tokens.BossToken import BossToken


def get_example_character_info():
    character_info = CharacterInfo(100, 0, 2)

    laptop = Laptop()
    backpack = Backpack()
    sword = Sword()

    character_info.add_item(backpack)
    character_info.add_item(laptop)
    character_info.add_item(sword)

    return character_info


if __name__ == "__main__":
    game_map = load_configuration()
    first_stage = game_map[0]

    screen = Screen(first_stage)

    screen.display_map()
    character_info = get_example_character_info()
    character_info_view = CharacterInfoView(character_info)
    screen.display_character_info(character_info_view)
    # screen.animate()  # todo: add threads??
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # battle_view = BattleView()
                    # battle_view.display()
                    BossToken().interact(character_info)
                    character_info_view = CharacterInfoView(character_info)
                    screen.display_map()
                    character_info_view.display()

    for row in game_map:
        print(row)
