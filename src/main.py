import pygame as pg, sys
import entities, camera, level

pg.init()

screen = {
    "proportions": {
        "width": 640,
        "height": 480
    }
}
screen["surface"] = pg.display.set_mode([screen["proportions"]["width"], screen["proportions"]["height"]])

clock = pg.time.Clock()
framerate = 60

level.add_level("./level_data/test_level.json")

player = entities.Player(level.levels[level.current_level_num]["level_data"]["player_start"]["x"], level.levels[level.current_level_num]["level_data"]["player_start"]["y"])

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
                player.jump(level.levels[level.current_level_num])
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
    
    if is_key_down["right"]:
        camera.camera_x += 0.1
    if is_key_down["left"]:
        camera.camera_x -= 0.1
    if is_key_down["down"]:
        camera.camera_y += 0.1
    if is_key_down["up"]:
        camera.camera_y -= 0.1
    
    level.update_block_rects(level.levels[level.current_level_num], camera.camera_x, camera.camera_y)
    player.update(camera.camera_x, camera.camera_y, level.levels[level.current_level_num], is_key_down)

    clock.tick(framerate)

def draw():
    screen["surface"].fill([0, 0, 0])
    camera.draw_camera(level.levels[level.current_level_num], player, screen["proportions"]["width"], screen["proportions"]["height"], screen)
    pg.display.update()

while True:
    update()
    draw()