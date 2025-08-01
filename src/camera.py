import pygame as pg

camera_x = 0
camera_y = 0

def draw_camera(level, window_width, window_height, surface):
    for b in level["level_data"]["blocks"]:
        if b["pos"]["x"] > camera_x - 1 and b["pos"]["x"] < window_width / 50 + camera_x + 1 and b["pos"]["y"] > camera_y - 1 and b["pos"]["y"] < window_height / 50 + camera_y + 1:
            pg.draw.rect(surface["surface"], [255, 255, 255], b["block_rect"])