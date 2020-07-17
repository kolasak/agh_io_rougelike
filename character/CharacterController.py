import pygame
from numpy.core.defchararray import isnumeric
from pygame.constants import K_m
from pygame.locals import K_w, K_a, K_s, K_d, K_e, K_r, K_h, K_q

from character.items.Key import Key
from enums.Direction import Direction
from fields import GateField, RoadField
from fixtures.constants import max_items_count
from graphics import Screen
# from controllers.ManualController import ManualController


class CharacterController:
    cannot_add_more_items_msg = f"You cannot add more items than {max_items_count}"

    def __init__(self):
        pass

    @staticmethod
    def execute_character_movement(event_key, character_info_view, fields):
        old_x = character_info_view.character_info.x
        old_y = character_info_view.character_info.y

        move_keys = {
            K_w: (0, -1, Direction.NORTH),
            K_a: (-1, 0, Direction.WEST),
            K_d: (1, 0, Direction.EAST),
            K_s: (0, 1, Direction.SOUTH)
        }

        if event_key in move_keys.keys():
            x = character_info_view.character_info.x + move_keys[event_key][0]
            y = character_info_view.character_info.y + move_keys[event_key][1]
            direction = move_keys[event_key][2]
            token = fields[x][y].get_token()
            if token is not None:
                result = token.interact(character_info_view.character_info)
                if result:
                    if hasattr(token, 'item'):
                        if token.item is not None:
                            fields[x][y].put_item(token.item)
                    fields[x][y].remove_token()

                Screen.Screen.display_map()
                character_info_view.display()
            elif CharacterController.check_if_passable(fields[x][y]):
                character_info_view.character_info.x = x
                character_info_view.character_info.y = y
                character_info_view.character_info.direction = direction
                Screen.Screen.render_character(old_x, old_y, x, y, character_info_view.character_img,
                                               direction)
                fields[x][y].interact(character_info_view.character_info)
                character_info_view.display()
            elif isinstance(fields[x][y], GateField):
                keys_ids = [x.id for x in character_info_view.character_info.items if isinstance(x, Key)]
                if fields[x][y].key_id in keys_ids:
                    fields[x][y] = RoadField()
                    Screen.Screen.display_map()
                    character_info_view.display()
        elif event_key == K_e:
            field = fields[character_info_view.character_info.x][character_info_view.character_info.y]
            if field.item is not None:
                item = field.get_item()
                if not character_info_view.character_info.add_item(item):
                    field.put_item(item)
                    Screen.Screen.render_text_values_for_n_seconds(character_info_view,
                                                                   'You can\'t have any more items.',
                                                                   700, 0, 800, 0)
                character_info_view.display()
        elif isnumeric(pygame.key.name(event_key)) \
                and int(pygame.key.name(event_key)) in range(1, len(character_info_view.character_info.items) + 1):
            item_number = int(pygame.key.name(event_key)) - 1
            item = character_info_view.character_info.items[item_number]
            if fields[character_info_view.character_info.x][character_info_view.character_info.y].item is None:
                character_info_view.character_info.remove_item(item)
                fields[character_info_view.character_info.x][character_info_view.character_info.y].put_item(item)
                Screen.Screen.repaint_screen()
                Screen.Screen.display_character_info(character_info_view)
            else:
                Screen.Screen.render_text_values_for_n_seconds(character_info_view,
                                                               'This field is already occupied by another item',
                                                               700, 0, 800, 0)
        elif event_key == K_r:
            fields[character_info_view.character_info.x][character_info_view.character_info.y].interact()
        elif event_key == K_m:
            healing_item = character_info_view.character_info.find_healing_item()
            if healing_item:
                if not character_info_view.character_info.heal_with_item(healing_item):
                    text = "Your health is excellent! There's no need to heal"
                else:
                    text = 'You have been healed!'
                Screen.Screen.render_text_values_for_n_seconds(character_info_view, text, 700, 0, 800, 0)
        elif event_key == K_h:
            from controllers.ManualController import ManualController
            controller = ManualController()
            controller.display_manual()
            Screen.Screen.display_map()
            Screen.Screen.display_character_info(character_info_view)

    @staticmethod
    def check_if_passable(field):
        return field.passable
