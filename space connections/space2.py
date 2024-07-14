import pgzrun

from random import randint

from time import time

TITLE = "Help me please :) (version 2.0)"

WIDTH = 800

HEIGHT = 750

satellites = []

lines = []

start_time = 0

end_time = 0

total_time = 0

num_sat = 8

next_satellite = 1

def create_satellites():

    global start_time

    start_time = time()

    for i in range (num_sat):
        s = Actor("image\strawber")
        s.pos = randint(50, WIDTH-50), randint(50, HEIGHT-50)
        satellites.append(s)

def draw():
    global total_time

    screen.blit("pink", (0,0))

    number = 1

    for satellite in satellites:
        screen.draw.text(str(number), (satellite.pos[0], satellite.pos[1]+10))

        satellite.draw()
        number += 1
    
    for l in lines:
        screen.draw.line(l[0], l[1], (255,255,255))
    
    if next_satellite<num_sat:
        total_time = time()-start_time
        screen.draw.text(str(round(total_time, 1)), (10,10), fontsize = 30)
    else:
        screen.draw.text(str(round(total_time, 1)), (10,10), fontsize = 30)

def update():
    pass



def on_mouse_down(pos):

    global next_satellite, end_time

    for i in num_sat:
        satellite = satellites[i]
        if satellite.collidepoint(pos) and 1 + 1 == next_satellite:
            if next_satellite > 1:
                lines.append((satellites[next_satellite - 2].pos, satellite.pos))
            next_satellite += 1
            if next_satellite > num_sat:
                end_time = time()
            break



    


pgzrun.go()