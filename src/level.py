import json, pygame as pg

def add_level(level_file_path):
    with open(level_file_path, "r") as level_file:
        level_dict = json.load(level_file)

        for l in levels:
            if level_dict["level_num"] == l["level_num"]:
                raise RuntimeError()

        for b in level_dict["level_data"]["blocks"]:
            b["block_rect"] = pg.Rect(0, 0, 33, 33)

        levels.append(level_dict)

def update_block_rects(level, camera_x, camera_y):
    for b in level["level_data"]["blocks"]:
        b["block_rect"].x = (b["pos"]["x"] - camera_x) * 32 - 0.5
        b["block_rect"].y = (b["pos"]["y"] - camera_y) * 32 - 0.5

levels = []
current_level_num = 1