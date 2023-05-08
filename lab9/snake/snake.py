# import :
import pygame as pg
import random, time
from random import randrange, randint

# initializating :
pg.init()

# creating a window, where the whole process will take place and to watch it :
w = h = 400
screen = pg.display.set_mode((w, h))
pg.display.set_caption("🐍")
screen.fill((205, 133, 63))

# other parammeters :
block_size = 20 
level = 0

# setting up prame per second (fps) :
fps = 5
clock = pg.time.Clock()

# fonts : 
font1 = pg.font.SysFont("Verdana", 20)
font2 = pg.font.SysFont("Verdana", 30)

# theme :
pg.mixer.init()
pg.mixer.music.load("./music/ssss.mp3")
pg.mixer.music.play(-1)

# ending :
game_over = font2.render("GAME OVER!", True, (76, 0, 153))

# to check the whole process :
crawling = True


class Food:
    def __init__(self):
        self.x = randrange(0, w, block_size)
        self.y = randrange(0, h, block_size)
   
    def draw(self):
        pg.draw.rect(screen, (255, 51, 51), (self.x, self.y, block_size, block_size)) 
    
    def redraw(self):
        self.x = randrange(0, w, block_size)
        self.y = randrange(0, h, block_size)


class Wall:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def draw(self):
        pg.draw.rect(screen, (204, 102, 0), (self.x, self.y, block_size, block_size))


class Snake:
    def __init__(self):
        self.speed = block_size
        self.score = 0
        self.body = [[40, 40],[500, 500],[520, 520]] # initial random head coordinates.
        self.dx = self.speed
        self.dy = 0
        self.destination = ""
        self.color = (102, 102, 255) # lavender blue

    def move(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT and self.destination != "right":
                    self.dx = -self.speed
                    self.dy = 0
                    self.destination = "left"
                if event.key == pg.K_RIGHT and self.destination != "left":
                    self.dx = self.speed
                    self.dy = 0
                    self.destination = "right"
                if event.key == pg.K_UP and self.destination != "down":
                    self.dx = 0
                    self.dy = -self.speed
                    self.destination = "up"
                if event.key == pg.K_DOWN and self.destination != "up":
                    self.dx = 0
                    self.dy = self.speed
                    self.destination = "down"

        # move the body parts of the snake in x and y to the previous coordinates :
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i][0] = self.body[i - 1][0]
            self.body[i][1] = self.body[i - 1][1]
        
        # move the head of the snake in x and y to the following coordinates :
        self.body[0][0] += self.dx
        self.body[0][1] += self.dy

        # collosion occurs between snake and borders :
        self.body[0][0] %= w
        self.body[0][1] %= h

    def draw(self):
        for block in self.body:
            pg.draw.circle(screen, self.color, (block[0] + 10, block[1] + 10), block_size / 2)

    # a function to check if snake and food cross :
    def food_collision(self, f:Food):
        if self.body[0][0] == f.x and self.body[0][1] == f.y:
            self.score += random.randint(1, 4)
            self.body.append([500, 500])

    # condition for the end of the game (if the snake's head collides with its body) :
    def self_collision(self):
        global crawling
        if self.body[0] in self.body[1:]:
            crawling = False

    # checking if food will appear in the snake's body :
    def check_food(self, f:Food):
        if [f.x, f.y] in self.body:
            f.redraw()


# setting up classes :
s = Snake()
f = Food()

# game loop :
while crawling:
    clock.tick(fps)
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False
            # pg.quit()

    screen.fill((128, 255, 0))

    # conditions to leveling up :
    if s.score >= 3:
        level = 1
        fps = 5
    if s.score >= 6:
        level = 2
        fps = 5
    if s.score >= 9:
        level = 3
        fps += 1
    if s.score >= 12:
        level = 4
        fps += 1
    if s.score >= 15:
        level = 5
        fps += 1

    # draw walls :
    wall_maria = open(f"level{level}.txt", "r").readlines() 
    
    wall_sina = []

    for i, line in enumerate(wall_maria):  # loop through index and row
        for j, each in enumerate(line):  # loop through each element in the string
            if each == "#":
                wall_sina.append(Wall(j * block_size, i * block_size))  # add each wall block to the list 

    for wall in wall_sina:
        wall.draw()

        # checking if food will appear in the walls :
        if f.x == wall.x and f.y == wall.y:
            f.redraw()

        # stop the game if the snake's head hits the wall :
        if s.body[0][0] == wall.x and s.body[0][1] == wall.y:
            crawling = False
            pg.mixer.music.stop()
            screen.fill((0, 0, 0))
            screen.blit(score, (100, 180))
            screen.blit(game_over, (100, 140))
            pg.display.update()
            time.sleep(4)

    # call all functions :
    f.draw()
    s.draw()
    s.move(events)
    s.food_collision(f)
    s.self_collision()
    s.check_food(f)

    # results :
    score = font2.render(f"Your Score : {s.score}", True, (76, 0, 153))
    s_cnt = font1.render(f"score : {s.score}", True, (76, 0, 153))
    screen.blit(s_cnt, (5, 0))
    l_cnt = font1.render(f"level : {level}", True, (76, 0, 153))
    screen.blit(l_cnt, (5, 30))

    pg.display.flip()

pg.quit()


