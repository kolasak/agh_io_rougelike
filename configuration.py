from fields import *
import numpy as np

import json

# Returns map as array of objects.
# For these who dont know np.array is just array in C or Java, so you can get or set element by index/es.
def load_configuration(json_path='config.json'):
    with open(json_path) as json_file:
        json_data = json.load(json_file)
        json_file.close()

    json_stages = json_data['stages']
    stages = []
    for json_stage in json_stages: # we allow user to define as many stages as he want, and we load each one
        game_map = parse_map(json_stage['map'])
        game_map = parse_monsters(game_map, json_stage['monsters'])
        game_map = parse_npcs(game_map, json_stage['npcs'])
        stages.append(game_map)
    return stages


def parse_map(json_map):
    width = json_map['width']
    height = json_map['height']
    game_map = np.empty((width, height), dtype=Field)

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
    # add monsters to map
    return map


def parse_npcs(map, json_npcs):
    # add npcs to map
    return map

