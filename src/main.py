import pygame as pg, sys, json
import entities, camera

pg.init()

screen = {
    "proportions": {
        "width": 640,
        "height": 480
    }
}
screen["surface"] = pg.display.set_mode([screen["proportions"]["width"], screen["proportions"]["height"]])

clock = pg.Clock()
framerate = 60

def add_level(level_file_path):
    with open(level_file_path, "r") as level_file:
        level_dict = json.load(level_file)

        for l in levels:
            if level_dict["level_num"] == l["level_num"]:
                raise RuntimeError()

        levels.append(level_dict)

levels = []
current_level_num = 0

add_level("./level_data/test_level.json")

is_key_down = {
    "right": False,
    "left": False,
    "down": False,
    "up": False,
    "w": False,
    "a": False,
    "s": False,
    "d": False
}

def update():
    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
            sys.exit(0)
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_RIGHT:
                is_key_down["right"] = True
            if e.key == pg.K_LEFT:
                is_key_down["left"] = True
            if e.key == pg.K_DOWN:
                is_key_down["down"] = True
            if e.key == pg.K_UP:
                is_key_down["up"] = True
            if e.key == pg.K_w:
                is_key_down["w"] = True
            if e.key == pg.K_a:
                is_key_down["a"] = True
            if e.key == pg.K_s:
                is_key_down["s"] = True
            if e.key == pg.K_d:
                is_key_down["d"] = True
        if e.type == pg.KEYUP:
            if e.key == pg.K_RIGHT:
                is_key_down["right"] = False
            if e.key == pg.K_LEFT:
                is_key_down["left"] = False
            if e.key == pg.K_DOWN:
                is_key_down["down"] = False
            if e.key == pg.K_UP:
                is_key_down["up"] = False
            if e.key == pg.K_w:
                is_key_down["w"] = False
            if e.key == pg.K_a:
                is_key_down["a"] = False
            if e.key == pg.K_s:
                is_key_down["s"] = False
            if e.key == pg.K_d:
                is_key_down["d"] = False
    
    if is_key_down["right"] or is_key_down["d"]:
        camera.camera_x += 0.1
    if is_key_down["left"] or is_key_down["a"]:
        camera.camera_x -= 0.1
    if is_key_down["down"] or is_key_down["s"]:
        camera.camera_y += 0.1
    if is_key_down["up"] or is_key_down["w"]:
        camera.camera_y -= 0.1

    clock.tick(framerate)

def draw():
    screen["surface"].fill([0, 0, 0])
    camera.draw_camera(levels[current_level_num], screen["proportions"]["width"], screen["proportions"]["height"], screen)
    pg.display.update()

while True:
    update()
    draw()