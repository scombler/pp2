import pygame as pg
from datetime import datetime

pg.init()

screen = pg.display.set_mode((800, 600))
screen.fill("white")
pg.display.set_caption("oh mickey, ur soo fine!")

clock = pg.time.Clock()

pg.mixer.music.load("C:\\Users\\admin\\OneDrive\\Документы\\pp2\\tsis5\\music\\ticking.mp3")
pg.mixer.music.play(-1)

body = pg.image.load("C:\\Users\\admin\\OneDrive\\Документы\\pp2\\tsis5\\images\\body.png")
body = pg.transform.scale(body, (800, 600))
# short hand is responsible for minutes :
short_hand = pg.image.load("C:\\Users\\admin\\OneDrive\\Документы\\pp2\\tsis5\\images\\minute.png").convert_alpha()  # to improve image quality
# long hand is responsible for seconds :
long_hand = pg.image.load("C:\\Users\\admin\\OneDrive\\Документы\\pp2\\tsis5\\images\\second.png").convert_alpha()  # to improve image quality

font = pg.font.SysFont('Arial', 30)

# a function that's responsible for the rotation of mickey's body
def blitRotateCenter(surf, image, topleft, angle):

    rotated_image = pg.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect)

x = 800 // 2
y = 600 // 2
radius = 10
color = (0, 0, 0)

moving = True

while moving:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            moving = False

    screen.blit(body, (0, 0)) 

    time = datetime.now()
    lg_angle = - 6 * time.second
    sh_angle = - 6 * time.minute

    text = font.render(f'{time : %H:%M:%S}', True, (0, 0, 0), (255, 255, 255))
    screen.blit(text,(10, 10))

    blitRotateCenter(screen, long_hand, (148, 50), lg_angle)
    blitRotateCenter(screen, short_hand, (148, 50), sh_angle) 

    pg.draw.circle(screen, color, (x, y), radius) 

    pg.display.flip()

pg.quit()