import pygame as pg
from pygame.color import THECOLORS

pg.init()

screen = pg.display.set_mode((500, 500))
pg.display.set_caption("球")

clock = pg.time.Clock()

x = 500 // 2
y = 500 // 2
r = 25

moving = True

while moving:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            moving = False

    pressed = pg.key.get_pressed()
    if pressed[pg.K_UP] and y - r > 15:
        y -= 20
    if pressed[pg.K_DOWN] and y + r + 15 < 500:  # height
        y += 20
    if pressed[pg.K_LEFT] and x - r > 15:
        x -= 20
    if pressed[pg.K_RIGHT] and x + r + 15 < 500: # width
        x += 20

    screen.fill(THECOLORS["white"])
    # pygame.draw.circle(Surface, color, pos, radius, width = 0)
    pg.draw.circle(screen, (255, 38, 38), (x, y), r)

    pg.display.flip()

pg.quit()