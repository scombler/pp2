# imports :
import pygame as pg 
import time
from random import randint, randrange

# initializating :
pg.init()

# creating a window, where the whole process will take place and to watch it :
h = w = 800  # width & height
screen = pg.display.set_mode((h, w))
pg.display.set_caption("蛇")
surf = pg.Surface((390, 390), pg.SRCALPHA)

# setting up prame per second (fps) :
FPS = 5
clock = pg.time.Clock()

# background image :
bg = pg.image.load("./images/background.jpg")
bg = pg.transform.scale(bg, (w, h))

# ending :
game_over = pg.image.load("./images/game over.jpg")
game_over = pg.transform.scale(game_over, (390, 390))

# font :
font = pg.font.SysFont("Verdana", 20)

# theme :
pg.mixer.init()
pg.mixer.music.load("./music/ssss.mp3")
pg.mixer.music.play(-1)

# other parameters :
block_size = 40
level = 0  # max is 3

crawling = True
lose = False


class Food:
    def __init__(self):
        self.x = randrange(0, w, block_size)
        self.y = randrange(0, h, block_size)
        self.image = pg.transform.scale(pg.image.load("./images/yummy.png"), (50, 50))

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def redraw(self):
        self.x = randrange(0, w, block_size)
        self.y = randrange(0, h, block_size)


class Snake:
    def __init__(self):
        self.body = [[250, 250]]  # initial head coordinates
        self.speed = block_size
        self.dx = 0
        self.dy = 0
        self.score = 0
        self.color = (0, 255, 0) # lime 
    
    def move(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:  
                if event.key == pg.K_LEFT: 
                    self.dx = -self.speed
                    self.dy = 0
                if event.key == pg.K_RIGHT:
                    self.dx = self.speed
                    self.dy = 0
                if event.key == pg.K_UP:
                    self.dx = 0
                    self.dy = -self.speed
                if event.key == pg.K_DOWN:
                    self.dx = 0
                    self.dy = self.speed

        # move the body parts of the snake in x and y to the previous coordinates :
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i][0] = self.body[i - 1][0] 
            self.body[i][1] = self.body[i - 1][1]

        # move the head of the snake in x and y to the following coordinates :
        self.body[0][0] += self.dx 
        self.body[0][1] += self.dy 


    def check_for_bound(self): 
        #if hits the boundaies -> game_over 
        if self.body[0].x * block_size >= w or self.body[0].x < 0 or self.body[0].y * block_size >= h or self.body[0].y < 0: 
            return True

    def draw(self):
        for part in self.body:
            pg.draw.rect(screen, self.color, (part[0], part[1], block_size, block_size))
    

    def food_collide(self, f:Food):
        if self.body[0][0] == f.x:
            if self.body[0][1] == f.y: # if snake head coordinates match food coordinates
                self.score += 1
                self.body.append([1000, 1000]) 
    

    # condition for the end of the game (if the snake's head collides with its body)
    def self_collide(self):
        global crawling
        if self.body[0] in self.body[1:]:
            crawling = False
            pg.mixer.music.stop()
            pg.mixer.Sound('./music/gameover.wav').play()
            pg.mixer.music.stop()

    
    def check_food(self, f:Food): 
        if [f.x, f.y] in self.body:
            f.redraw() 


class Wall:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.image = pg.image.load("./images/wall.png")


    def draw(self):
        screen.blit(self.image, (self.x, self.y))


s = Snake()
f = Food()

# game loop :
while crawling:
    clock.tick(FPS)
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            crawling = False
        
    screen.blit(bg, (0, 0))

    # draw walls :
    wall_maria = open("level{}.txt".format(level), 'r').readlines() # 1st wall in aot
    wall_sina = []    # 3rd wall in aot
    for i, line in enumerate(wall_maria):    # loop through index and row
        for j, each in enumerate(line): # loop through each element in the string
            if each == "#":
                wall_sina.append(Wall(j * block_size, i * block_size))  # add each wall block to the list 

   
    f.draw()
    s.draw()
    s.move(events)
    s.food_collide(f)
    s.self_collide()
    s.check_food(f)



    score = font.render(f'score: {s.score}', True, (0, 0, 0))
    screen.blit(score, (50, 50))
    lv = font.render(f'level: {level}', True, 'black')
    screen.blit(lv, (50, 80))

    # condition for moving to the next level
    if s.score == 3:
        level += 1 # увеличиваем уровень
        level %= 3
        FPS += 2 # увеличиваем скорость
        s.score = 0


    for sina in wall_sina:
        sina.draw()
        if f.x == sina.x and f.y == sina.y: 
            f.redraw()

        # stop the game if the snake's head hits the wall :
        if s.body[0][0] == sina.x and s.body[0][1] == sina.y: #
            lose = True
            pg.mixer.music.stop()
            pg.mixer.Sound('./music/gameover.wav').play()
            pg.mixer.music.stop()
            pg.display.update()

    # game over loop :
    while lose:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                crawling = False
                lose = False  
                #time.sleep(0.5)

        surf.blit(game_over, (0, 0))
        screen.blit(surf, (200, 200))
        s_cnt = font.render(f'Your score is {s.score}', True, (0, 0, 0))
        screen.blit(s_cnt, (320, 405))
        l_cnt = font.render(f'Your level is {level}', True, (0, 0, 0))
        screen.blit(l_cnt, (322, 435))
        pg.display.flip()

    pg.display.flip()

pg.quit()