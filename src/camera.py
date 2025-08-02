import pygame as pg

camera_x = 0
camera_y = 0

def draw_camera(level, player, window_width, window_height, surface):
    for b in level["level_data"]["blocks"]:
        if b["pos"]["x"] > camera_x - 1 and b["pos"]["x"] < window_width / 50 + camera_x + 1 and b["pos"]["y"] > camera_y - 1 and b["pos"]["y"] < window_height / 50 + camera_y + 1:
            pg.draw.rect(surface["surface"], [255, 255, 255], b["block_rect"])

    if player.x > camera_x - 4/5 and player.x < window_width / 50 + camera_x + 4/5 and player.y > camera_y - 4/5 and player.y < window_height / 50 + camera_y + 4/5:
        pg.draw.rect(surface["surface"], [255, 0, 0], player.rect)