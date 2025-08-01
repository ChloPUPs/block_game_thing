import pygame as pg

camera_x = 0
camera_y = 0

def set_camera_pos(x, y):
    ...

def draw_camera(level, window_width, window_height, surface):
    for o in level["level_data"]["blocks"]:
        if o["pos"]["x"] > camera_x - 1 and o["pos"]["x"] < window_width / 50 + camera_x + 1 and o["pos"]["y"] > camera_y - 1 and o["pos"]["y"] < window_height / 50 + camera_y + 1:
            pg.draw.rect(surface["surface"], [255, 255, 255], pg.Rect((o["pos"]["x"] - camera_x) * 50, (o["pos"]["y"] - camera_y) * 50, 50, 50))