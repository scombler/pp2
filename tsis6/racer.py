# imports
import pygame as pg
from pygame.locals import *
import random, time

# initialzing 
pg.init()

# creating a window, where the whole process will take place and to watch it :
w = 600     # window width.
h = 800     # window height.
screen = pg.display.set_mode((w, h))
pg.display.set_caption("🏎️") # name the window

# setting up frame per sec (fps)
FPS = 60
clock = pg.time.Clock()

# background music :
pg.mixer.music.load("C:\\Users\\admin\\OneDrive\\Документы\\pp2\\tsis6\\music\\background.wav")
pg.mixer.music.play(-1)

# background aka street :
road = pg.image.load("C:\\Users\\admin\\OneDrive\\Документы\\pp2\\tsis6\\images\\road.png")
road = pg.transform.scale(road, (w, h))

# fonts :
font = pg.font.SysFont("Verdana", 20)
point = pg.font.SysFont("Verdana", 20)

# ending :
game_over = pg.image.load("C:\\Users\\admin\\OneDrive\\Документы\\pp2\\tsis6\\images\\gameover.jpg")
game_over = pg.transform.scale(game_over, (w, h))

# other parameters for use in the process :
speed = 5
score = coin = 0

# create a class, responsible for the enemy and his actions :
class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pg.image.load("C:\\Users\\admin\\OneDrive\\Документы\\pp2\\tsis6\\images\\enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, w - 40), 0) 

    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if (self.rect.top > h):
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, w - 40), 0)


# create a class, responsible for the player and his actions :
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pg.image.load("C:\\Users\\admin\\OneDrive\\Документы\\pp2\\tsis6\\images\\player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (300, 700)
        
    def move(self):
        pressed_keys = pg.key.get_pressed()
        if self.rect.left > 0:
              if pressed_keys[pg.K_LEFT]:
                  self.rect.move_ip(-speed, 0)

        if self.rect.right < w:        
              if pressed_keys[pg.K_RIGHT]:
                  self.rect.move_ip(speed, 0)

        if self.rect.top > 0:
            if pressed_keys[pg.K_UP]:
                self.rect.move_ip(0, -speed)
        
        if self.rect.bottom < h:
            if pressed_keys[pg.K_DOWN]:
                self.rect.move_ip(0, speed)


# create a class, responsible for the coin :
class Coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("C:\\Users\\admin\\OneDrive\\Документы\\pp2\\tsis6\\images\\coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, w - 40), 0)

    def move(self):
        global coin
        self.rect.move_ip(0, speed)
        if (self.rect.top > h):
            self.rect.top = 0
            self.rect.center = (random.randint(40, w - 40), 0) 

    def chow_time(self):
        self.rect.top = 0
        self.rect.center = (random.randint(40, w - 40), 0) 

# setting up Sprites
p = Player()
e = Enemy()
c = Coin()

# creating sprites Ggroups
player = pg.sprite.Group()
player.add(p)

enemies = pg.sprite.Group()
enemies.add(e)

coins = pg.sprite.Group()
coins.add(c)

all_sprites = pg.sprite.Group()
all_sprites.add(p)
all_sprites.add(e)
all_sprites.add(c)

moving = True

# adding a new user event :
forrest_gump = pg.USEREVENT + 1
pg.time.set_timer(forrest_gump, 1000)

# game loop :
while moving:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == forrest_gump:
            speed += 1.5
        if event.type == pg.QUIT:
            moving = False
            pg.quit()

    screen.blit(road, (0, 0))

    # display game results :
    s1 = font.render("scores:", True, (0, 0, 0))
    c1 = font.render("coins:", True, (0, 0, 0))
    s_cnt = point.render(str(score), True, (0, 0, 0))
    c_cnt = point.render(str(coin), True, (0, 0, 0))
    screen.blit(s_cnt, (85, 6))
    screen.blit(s1, (10, 5))
    screen.blit(c_cnt, (70, 23))
    screen.blit(c1, (10, 22))
    
    # moves and re-draws all sprites :
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    # condition for collecting coins :
    if pg.sprite.collide_rect(p, c):
        coin += 1
        pg.mixer.music.load("C:\\Users\\admin\\OneDrive\\Документы\\pp2\\tsis6\\music\\yummy.ogg")
        pg.mixer.music.play(start = 0.5)
        c.chow_time()

    p.update()
    e.update()
    c.update()
    
    # a condition for a collision between player and enemy, also for game over :
    if pg.sprite.spritecollideany(p, enemies):
        pg.mixer.Sound("C:\\Users\\admin\\OneDrive\\Документы\\pp2\\tsis6\\music\\crash.wav").play()
        time.sleep(0.5)

        screen.blit(game_over, (0, 0)) # display that the game is OVER !
    
        pg.display.update()

        for entity in all_sprites:
            entity.kill() 
        time.sleep(4)  # put the system to sleep for a specified time 
        pg.quit()
    
    pg.display.update()
    #pg.display.flip()
    clock.tick(FPS)
