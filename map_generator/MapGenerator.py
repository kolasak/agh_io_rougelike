import numpy as np
import json
from fields.Field import Field

import random


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


def create_multi_room_map(creator_config):
    map_height, map_width = creator_config["rooms"]
    room_height, room_width = creator_config["room_size"]
    rooms = np.empty((map_height, map_width), dtype=object)
    for x in range(map_height):
        for y in range(map_width):
            rooms[x][y] = create_room(room_height, room_width)
            rooms[x][y]["position"] = (x, y)
    add_locations(rooms, creator_config["locations"])
    set_passages(rooms, map_height, map_width)
    return rooms


def create_room(height, width):
    maze = np.empty((height, width), dtype=Field)
    for i in range(0, width):
        maze[0][i] = "V"
        maze[height-1][i] = "V"
    for i in range(0, height):
        maze[i][0] = "V"
        maze[i][width-1] = "V"

    x = random.randint(1, height-2)
    y = random.randint(1, width-2)
    none_counter = (width-2) * (height-2)

    maze[x][y] = None
    stack = [(x, y)]
    none_counter -= 1

    while stack:
        x, y = stack.pop()
        if is_addable(maze, width, height, x, y):
            field_list = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            random.shuffle(field_list)
            for field in field_list:
                stack.append(field)

    for x in range(height):
        for y in range(width):
            if not maze[x][y]:
                maze[x][y] = "V"

    stage = {
        "map": {
            "width": width,
            "height": height,
            "map": maze
        },
        "monsters": {
            "basic": [],
            "bosses": []
        },
        "npcs": [],
        "items": {
            "keys": [],
            "boost": []
        }
    }
    return stage


def add_locations(rooms, locations):
    for location in locations:
        x, y = location["room"]
        room_map = rooms[x][y]["map"]["map"]
        height = rooms[x][y]["map"]["height"]
        width = rooms[x][y]["map"]["width"]
        type = location["type"]

        neighbor_list = [location["center"]]
        for size_counter in range (location["size"]):
            x, y = neighbor_list.pop()
            room_map[x][y] = type
            for field in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                f_x, f_y = field
                if 0 < f_x < width - 1 and 0 < f_y < height - 1 and room_map[f_x, f_y] != type:
                    neighbor_list.append(field)
            random.shuffle(neighbor_list)
        if type in ["W", "V"]:
            for field in neighbor_list:
                f_x, f_y = field
                room_map[f_x][f_y] = "M"


def set_passages(rooms, map_height, map_width):
    for row in rooms:
        for room in row:
            l_x, l_y = room["position"]
            room_height = room["map"]["height"]
            room_width = room["map"]["width"]
            room_map = room["map"]["map"]

            if l_x != 0:
                pos = random.randint(1, room_width-1)
                while True:
                    if room_map[1][pos] != "V":
                        room_map[0][pos] = "P"
                        break
                    pos = (pos+1) % room_width

            if l_x != map_height-1:
                pos = random.randint(1, room_width-1)
                while True:
                    if room_map[room_height-2][pos] != "V":
                        room_map[room_height-1][pos] = "P"
                        break
                    pos = (pos+1) % room_width

            if l_y != 0:
                pos = random.randint(1, room_height - 1)
                while True:
                    if room_map[pos][1] != "V":
                        room_map[pos][0] = "P"
                        break
                    pos = (pos + 1) % room_width

            if l_y != map_width - 1:
                pos = random.randint(1, room_height - 1)
                while True:
                    if room_map[pos][room_width - 2] != "V":
                        room_map[pos][room_width - 1] = "P"
                        break
                    pos = (pos + 1) % room_width


def is_addable(array, width, height, x, y):
    if 0 < x < width - 1 and 0 < y < height - 1:
        if array[x][y]:
            return False
        neighbor_counter = 0
        if array[x+1][y] == "M": neighbor_counter += 1
        if array[x-1][y] == "M": neighbor_counter += 1
        if array[x][y+1] == "M": neighbor_counter += 1
        if array[x][y-1] == "M": neighbor_counter += 1
        if neighbor_counter > 1:
            array[x][y] = "V"
            return False
        array[x][y] = "M"
        return True


if __name__ == "__main__":
    creator_config = {
        "rooms": (2, 3),
        "room_size": (25, 25),
        "locations": [
            {
                "room": (0, 0),
                "type": "F",
                "size": 30,
                "center": (10, 15)
            },
            {
                "room": (0, 2),
                "type": "W",
                "size": 20,
                "center": (20, 5)
            },
            {
                "room": (1, 1),
                "type": "T",
                "size": 6,
                "center": (13, 13)
            },
            {
                "room": (1, 2),
                "type": "F",
                "size": 30,
                "center": (18, 20)
            }

        ]
    }
    generated_map = create_multi_room_map(creator_config)
    import json

    with open('generated_map.json', 'w') as f:
        json.dump(generated_map, f, cls=NumpyEncoder)
