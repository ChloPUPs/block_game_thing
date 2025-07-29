import pygame as pg, sys
from typing import Any

pg.init()

screen = {
    "proportions": {
        "width": 640,
        "height": 480
    }
}
screen["surface"] = pg.display.set_mode([screen["proportions"]["width"], screen["proportions"]["height"]])

while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
            sys.exit(0)