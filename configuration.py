import json

import numpy as np

from character.items.BoostItem import BoostItem
from character.items.Key import Key
from fields import *


# Returns map as array of objects.
# For these who dont know np.array is just array in C or Java, so you can get or set element by index/es.
from gameplay.Question import Question
from gameplay.QuestionContainer import QuestionContainer
from tokens.BossToken import BossToken
from tokens.MonsterToken import MonsterToken
from tokens.NpcToken import NpcToken


MAX_QUESTION_ANSWERS = 5


def load_multi_room_map(json_path='config.json'):
    with open(json_path) as json_file:
        json_data = json.load(json_file)
        json_file.close()

    map_height = len(json_data)
    map_width = len(json_data[0])
    game_map = np.empty((map_height, map_width), dtype=object)
    passages_map = np.empty((map_height, map_width), dtype=object)

    for row_of_rooms in json_data:
        for room in row_of_rooms:
            room_map, passages = parse_map(room['map'])
            room_map = parse_monsters(room_map, room['monsters'])
            room_map = parse_npcs(room_map, room['npcs'])
            room_map = parse_items(room_map, room['items'])
            x, y = room["position"]
            print(x, y)
            passages_map[x][y] = passages
            game_map[x][y] = room_map
    bind_passages(game_map, passages_map, map_height, map_width,
                  json_data[0][0]['map']['height'], json_data[0][0]['map']['width'])
    return game_map


def bind_passages(game_map, passages_map, map_height, map_width, room_height, room_width):
    reverse_passage_type = {
        "N": "S",
        "S": "N",
        "W": "E",
        "E": "W"
    }
    passage_vector = {
        "N": (1, 0),
        "S": (-1, 0),
        "W": (0, -1),
        "E": (0, 1)
    }
    for x in range(map_height):
        for y in range(map_width):
            passages = passages_map[x][y]
            for passage in passages:
                passage_type = get_passage_type(passage, room_height, room_width)
                n_x, n_y = passage_vector[passage_type]
                n_x += x
                n_y += y
                for n_passage in passages_map[n_x][n_y]:
                    if get_passage_type(n_passage, room_height, room_width) == reverse_passage_type[passage_type]:
                        p_x, p_y = passage
                        game_map[x][y][p_x][p_y].bind(game_map[n_x][n_y], n_passage)


def get_passage_type(passage, room_height, room_width):
    x, y = passage
    if x == 0: return "S"
    if y == 0: return "W"
    if x == room_height - 1: return "N"
    if y == room_width - 1: return "E"
    return None


def load_map(json_path='config.json'):
    with open(json_path) as json_file:
        json_data = json.load(json_file)
        json_file.close()

    json_stages = json_data['stages']
    stages = []
    for json_stage in json_stages:  # we allow user to define as many stages as he want, and we load each one
        game_map, _ = parse_map(json_stage['map'])
        game_map = parse_monsters(game_map, json_stage['monsters'])
        game_map = parse_npcs(game_map, json_stage['npcs'])
        game_map = parse_items(game_map, json_stage['items'])
        stages.append(game_map)
    return stages


def parse_questions(riddles):
    for riddle in riddles:
        question = Question(riddle['question'])
        for answer in riddle['answers']:
            Question.add_answer(question,answer)
            if answer == riddle['correct']:
                Question.add_correct(question, answer)
        QuestionContainer.getInstance().add_question(question)


def load_questions(json_path='riddles.json'):
    question_container = QuestionContainer.getInstance()
    with open(json_path) as json_file:
        json_data = json.load(json_file)
        json_file.close()
    parse_questions(json_data['riddles'])
    return question_container


def parse_map(json_map):
    width = json_map['width']
    height = json_map['height']
    game_map = np.empty((height, width), dtype=Field)

    row_counter = 0
    passages = []
    for json_row in json_map['map']:
        field_counter = 0
        for character in json_row:
            field_class = CHARACTER_TO_FIELD[character]
            game_map[row_counter][field_counter] = field_class()
            if character == 'P':
                passages.append((row_counter, field_counter))
            field_counter += 1
        row_counter += 1
    return game_map, passages


def parse_monsters(map, json_monsters):
    for monster in json_monsters['basic']:
        new_monster = MonsterToken(monster['hp'], monster['strength'], monster['image'], monster['xp'])
        new_monster.item = _get_item(map, monster['item'])
        map[monster['y']][monster['x']].put_token(new_monster)
    for boss in json_monsters['bosses']:
        new_boss = BossToken(boss['hp'], boss['strength'], boss['image'], boss['xp'])
        new_boss.item = _get_item(map, boss['item'])
        map[boss['y']][boss['x']].put_token(new_boss)
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
    for npc in json_npcs:
        new_npc = NpcToken(npc['name'], npc['image'], npc['attributes'], npc['dialog'])
        map[npc['y']][npc['x']].put_token(new_npc)
    return map

def _get_item(map, item):
    item_obj = None
    if item is not None:
        if item['type'] == 'boost':
            item_obj = BoostItem(item['name'], item['strength'], item['image'])
        elif item['type'] == 'key':
            item_obj = Key()
            gate = map[item['gate_y']][item['gate_x']]
    return item_obj