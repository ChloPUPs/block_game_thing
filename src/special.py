import pygame as pg

class Player:
    def __init__(self, x, y):
        self.start_x = x
        self.start_y = y

        self.x = x
        self.y = y

        self.rect = pg.Rect(0, 0, 24, 32)
        self.img = pg.image.load("../assets/player/player.png")

        self.velocity_y = 0
        self.velocity_x = 0

    def jump(self, level):
        for b in level["level_data"]["blocks"]:
            if self.x < b["pos"]["x"] + 1 and self.x + 24/32 > b["pos"]["x"] and self.y < b["pos"]["y"] + 1 / 100 and self.y + (1 + 1 / 100) > b["pos"]["y"]:
                self.velocity_y = -0.2

    def update(self, camera_x, camera_y, level, key_down_dict):
        self.velocity_y += 0.007

        if key_down_dict["d"] and key_down_dict["a"]:
            self.velocity_x = 0
        elif key_down_dict["d"]:
            self.velocity_x = 0.06
        elif key_down_dict["a"]:
            self.velocity_x = -0.06
        else:
            self.velocity_x = 0
        
        self.x += self.velocity_x
        self.y += self.velocity_y

        for b in level["level_data"]["blocks"]:
            while self.x < b["pos"]["x"] + 1*0.9 and self.x + 24/32*0.9 > b["pos"]["x"] and self.y < b["pos"]["y"] + 1 / 100 and self.y + 1 > b["pos"]["y"]:
                self.velocity_y = 0
                self.y -= 0.005
            while self.x < b["pos"]["x"] + 1*0.9 and self.x + 24/32*0.9 > b["pos"]["x"] and self.y < b["pos"]["y"] + 1 and self.y + 1 / 100 > b["pos"]["y"]:
                self.velocity_y = 0
                self.y += 0.005
            while self.x < b["pos"]["x"] + 1 and self.x + 24/32 / 100 > b["pos"]["x"] and self.y < b["pos"]["y"] + 1*0.95 and self.y + 1*0.95 > b["pos"]["y"]:
                self.velocity_x = 0
                self.x += 0.005
            while self.x < b["pos"]["x"] + 1 / 100 and self.x + 24/32 > b["pos"]["x"] and self.y < b["pos"]["y"] + 1*0.95 and self.y + 1*0.95 > b["pos"]["y"]:
                self.velocity_x = 0
                self.x -= 0.005

        if self.y > 20:
            self.x = self.start_x
            self.y = self.start_y
            self.velocity_x = 0
            self.velocity_y = 0

        self.rect.x = (self.x - camera_x) * 32
        self.rect.y = (self.y - camera_y) * 32