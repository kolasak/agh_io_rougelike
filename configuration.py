import json

import numpy as np

from character.items.BoostItem import BoostItem
from character.items.Key import Key
from fields import *


# Returns map as array of objects.
# For these who dont know np.array is just array in C or Java, so you can get or set element by index/es.
from tokens.MonsterToken import MonsterToken


def load_configuration(json_path='config.json'):
    with open(json_path) as json_file:
        json_data = json.load(json_file)
        json_file.close()

    json_stages = json_data['stages']
    stages = []
    for json_stage in json_stages:  # we allow user to define as many stages as he want, and we load each one
        game_map = parse_map(json_stage['map'])
        game_map = parse_monsters(game_map, json_stage['monsters'])
        game_map = parse_npcs(game_map, json_stage['npcs'])
        game_map = parse_items(game_map, json_stage['items'])
        stages.append(game_map)
    return stages


def parse_map(json_map):
    width = json_map['width']
    height = json_map['height']
    game_map = np.empty((height, width), dtype=Field)

    row_counter = 0
    for json_row in json_map['map']:
        field_counter = 0
        for character in json_row:
            field_class = CHARACTER_TO_FIELD[character]
            game_map[row_counter][field_counter] = field_class()
            field_counter += 1
        row_counter += 1
    return game_map


def parse_monsters(map, json_monsters):
    for monster in json_monsters['data']:
        new_monster = MonsterToken(monster['strength'], monster['hp'], monster['image'])
        map[monster['y']][monster['x']].put_token(new_monster)
    return map


def parse_items(map, json_items):
    for key in json_items['keys']:
        key_obj = Key()
        map[key['y']][key['x']].put_item(key_obj)
        gate = map[key['gate_y']][key['gate_x']]
        if isinstance(gate, GateField):
            gate.set_key_id(key_obj.id)

    for item in json_items['boost']:
        item_obj = BoostItem(item['name'], item['strength'], item['image'])
        map[item['y']][item['x']].put_item(item_obj)

    return map


def parse_npcs(map, json_npcs):
    # add npcs to map
    return map
