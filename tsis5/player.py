import pygame as pg

pg.init()

screen = pg.display.set_mode((500, 500))
pg.display.set_caption("ฅ^•ﻌ•^ฅ")

clock = pg.time.Clock()

playlist = []
playlist.append("C:\\Users\\admin\\OneDrive\\Документы\\pp2\\tsis5\\music\\5 Seconds Of Summer - Kill My Time.mp3")
playlist.append("C:\\Users\\admin\\OneDrive\\Документы\\pp2\\tsis5\\music\\Blue Hair - TV Girl.mp3")
playlist.append("C:\\Users\\admin\\OneDrive\\Документы\\pp2\\tsis5\\music\\Ed Sheeran, Travis Scott - Antisocial.mp3")
playlist.append("C:\\Users\\admin\\OneDrive\\Документы\\pp2\\tsis5\\music\\Hiroyuki Sawano feat. Mika Kobayashi - EGO.mp3")
playlist.append("C:\\Users\\admin\\OneDrive\\Документы\\pp2\\tsis5\\music\\Juice WRLD - Feeling.mp3")
playlist.append("C:\\Users\\admin\\OneDrive\\Документы\\pp2\\tsis5\\music\\LMYK - Zero.mp3")
playlist.append("C:\\Users\\admin\\OneDrive\\Документы\\pp2\\tsis5\\music\\NCT DREAM, HRVY -  Don't Need Your Love.mp3")
playlist.append("C:\\Users\\admin\\OneDrive\\Документы\\pp2\\tsis5\\music\\NewJeans - OMG.mp3")
playlist.append("C:\\Users\\admin\OneDrive\\Документы\\pp2\\tsis5\\music\\SZA - Snooze.mp3")
playlist.append("C:\\Users\\admin\\OneDrive\\Документы\\pp2\\tsis5\\music\\Steve Lacy - Bad Habit.mp3")

pg.mixer.music.load("C:\\Users\\admin\\OneDrive\\Документы\\pp2\\tsis5\\music\\5 Seconds Of Summer - Kill My Time.mp3")
pg.mixer.music.play(-1)

playing = True
next = 0
previous = 0
on = True
off = False

while playing: 
    clock.tick(60)
    
    screen.fill((153, 153, 255))
    template = pg.image.load("C:\\Users\\admin\\OneDrive\\Документы\\pp2\\tsis5\\images\\template.png")
    screen.blit(template, (72, 80))
    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
        
        if event.type == pg.KEYDOWN:    
            if event.key == pg.K_SPACE and on == True:
                pg.mixer.music.pause()
                on = False
            elif event.key == pg.K_SPACE and off == False:
                pg.mixer.music.unpause()
                on = True
            if event.key == pg.K_RIGHT:
                next += 1
                if next == len(playlist):
                    next = 0
                pg.mixer.music.load(playlist[next])
                pg.mixer.music.play()
            if event.key == pg.K_LEFT:
                previous -= 1
                if previous == -1:
                    previous == len(playlist) - 1
                pg.mixer.music.load(playlist[previous])
                pg.mixer.music.play()

    pg.display.flip() 

pg.quit()