import pygame as pg

class Player:
    def __init__(self, x, y):
        self.start_x = x
        self.start_y = y

        self.x = x
        self.y = y

        self.rect = pg.Rect(0, 0, 40, 40)

        self.velocity_y = 0
        self.velocity_x = 0

        self.max_velocity_y = 40
        self.max_velocity_x = 10

    def jump(self, level):
        for b in level["level_data"]["blocks"]:
            if self.x < b["pos"]["x"] + 1 and self.x + 4/5 > b["pos"]["x"] and self.y < b["pos"]["y"] + 1 / 100 and self.y + 9/10 > b["pos"]["y"]:
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

        if self.velocity_x > self.max_velocity_x:
            self.max_velocity_x = self.max_velocity_x
        
        if self.velocity_x < -self.max_velocity_x:
            self.max_velocity_x = self.max_velocity_x
        
        self.x += self.velocity_x
        self.y += self.velocity_y

        self.rect.colliderect

        for b in level["level_data"]["blocks"]:
            while self.x < b["pos"]["x"] + 1*0.9 and self.x + 4/5*0.9 > b["pos"]["x"] and self.y < b["pos"]["y"] + 1 / 100 and self.y + 4/5 > b["pos"]["y"]:
                self.y -= 0.01
                self.velocity_y = 0
            while self.x < b["pos"]["x"] + 1*0.9 and self.x + 4/5*0.9 > b["pos"]["x"] and self.y < b["pos"]["y"] + 1 and self.y + 4/5 / 100 > b["pos"]["y"]:
                self.y += 0.01
                self.velocity_y = 0
            while self.x < b["pos"]["x"] + 1 and self.x + 4/5 / 100 > b["pos"]["x"] and self.y < b["pos"]["y"] + 1 and self.y + 4/5 > b["pos"]["y"]:
                self.velocity_x = 0
                self.x += 0.01
            while self.x < b["pos"]["x"] + 1 / 100 and self.x + 4/5 > b["pos"]["x"] and self.y < b["pos"]["y"] + 1 and self.y + 4/5 > b["pos"]["y"]:
                self.velocity_x = 0
                self.x -= 0.01
        
        if self.y > 20:
            self.x = self.start_x
            self.y = self.start_y
            self.velocity_x = 0
            self.velocity_y = 0

        self.rect.x = (self.x - camera_x) * 50
        self.rect.y = (self.y - camera_y) * 50