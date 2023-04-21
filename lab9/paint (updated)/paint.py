# imports :
import pygame as pg, math

# initialzing : 
pg.init()

# setting up fps :
fps = 60
clock = pg.time.Clock()

# creating a window, where the whole process will take place and to watch it :
w = h = 800 # width and height
canvas = pg.display.set_mode((w, h))
canvas.fill((255, 255, 255))
pg.display.set_caption("Van Gogh 👨🎨🌃🌌✨🌻")

# parameters :
color = (0, 0, 0)   # default color.
shape = 'line'  # initial/default mode.
width = 10  # width of shape.
size = 50   # width of eraser.

# start and end points :
prev, cur = 0, 0

drawing = True

# to save ur masterpiece :
def save_image():
    subsurface = canvas.subsurface((0, 100, w - 100, h - 100))
    pg.image.save(subsurface, "image.png")

while drawing:

    clock.tick(fps)

    for event in pg.event.get():
        pressed = pg.key.get_pressed()
        ctrl_pressed = pressed[pg.K_RCTRL] or pressed[pg.K_LCTRL] # ctrl is pressed
    
        if event.type == pg.QUIT:
            drawing = False

        # call the function to save the picture :
        if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    save_image()
                    drawing = False

        if event.type == pg.KEYDOWN:
            # change width of the shape :
            if pressed[pg.K_DOWN] and width > 1:
                width -= 1
            if pressed[pg.K_UP]:
                width += 1

            # color palette :
            if pressed[pg.K_b]:
                color = (135, 206, 235) # sky blue.
            if pressed[pg.K_v]:
                color = (204, 153, 255) # lavender.
            if pressed[pg.K_g]:
                color = (191, 255, 0) # lime.
            if pressed[pg.K_p]:
                color = (128, 128, 255) # periwinkle.
            if pressed[pg.K_d]:
                color = (255, 188, 217) # cotton candy.
            if pressed[pg.K_m]:
                color = (131,137,150) # roman silver.

            # shapes : 
            if ctrl_pressed and pressed[pg.K_l]:
                shape = "line"
            if ctrl_pressed and pressed[pg.K_e]:
                shape = "eraser"
            if ctrl_pressed and pressed[pg.K_c]:
                shape = "circle"
            if ctrl_pressed and pressed[pg.K_r]:
                shape = "rectangle"
            if ctrl_pressed and pressed[pg.K_s]:
                shape = "square"
            if ctrl_pressed and pressed[pg.K_t]:
                shape = "equilateral_triangle"
            if ctrl_pressed and pressed[pg.K_i]:
                shape = "right_triangle"
            if ctrl_pressed and pressed[pg.K_h]:
                shape = "rhombus"
        
        # line and eraser are similar in use.
        if shape == "line" or shape == "eraser":

            if event.type == pg.MOUSEBUTTONDOWN:
                prev = pg.mouse.get_pos()

            if event.type == pg.MOUSEMOTION:
                cur = pg.mouse.get_pos()

                if prev:
                    if shape == "line":
                        pg.draw.line(canvas, color, prev, cur, width)

                    if shape == "eraser":
                        pg.draw.line(canvas, (255, 255, 255), prev, cur, size) # just repaints white.
                    prev = cur

            if event.type == pg.MOUSEBUTTONUP:
                prev = None
        else:
            if event.type == pg.MOUSEBUTTONDOWN:
                prev = pg.mouse.get_pos()

            if event.type == pg.MOUSEBUTTONUP:
                cur = pg.mouse.get_pos()

                if shape == "square" or shape == "rectangle":
                    x = min(prev[0], cur[0])  # min cordinates.
                    y = min(prev[1], cur[1])
                    lx = abs(prev[0] - cur[0]) # length.
                    ly = abs(prev[1] - cur[1])

                    if shape == "square":
                        lx = (lx + ly) / 2  # length and width are same for square.
                        ly = lx
                    pg.draw.rect(canvas, color, (x, y, lx, ly), width)

                elif shape == "circle":
                    x = (prev[0] + cur[0]) / 2  # coordinates of center.
                    y = (prev[1] + cur[1]) / 2
                    rx = abs(prev[0] - cur[0]) / 2 # radius for x.
                    ry = abs(prev[1] - cur[1]) / 2  # radius for y.
                    r = (rx + ry) / 2 # central radius.
                    pg.draw.circle(canvas, color, (x, y), r, width)

                elif shape == "right_triangle" or shape == "equilateral_triangle":
                    x = min(prev[0], cur[0])  # min coordinate.
                    y = min(prev[1], cur[1])
                    lx = abs(prev[0] - cur[0])  # length of pseudo rectangle.
                    ly = abs(prev[1] - cur[1])

                    if shape == "right_triangle":
                        ly = math.sqrt(lx**2 - (lx / 2)**2)  # all sides are equal.
                    points = (x, y + ly), (x + lx / 2, y), (x + lx, y + ly)  # draw by three points.
                    pg.draw.polygon(canvas, color, points, width)

                elif shape == "rhombus":               
                    x = min(prev[0], cur[0])  # min coordinate.
                    y = min(prev[1], cur[1])
                    lx = abs(prev[0] - cur[0])  # abs value.
                    ly = abs(prev[1] - cur[1])
                    points = (x + lx / 2, y), (x + lx, y + ly / 2), (x + lx / 2, y + ly), (x, y + ly / 2)
                    pg.draw.polygon(canvas, color, points, width)  # draw by points.

    pg.display.update() # updates the canvas.

pg.quit()