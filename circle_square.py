from pico2d import *
import math

open_canvas()

sq = True

grass = load_image('grass.png')
character = load_image('character.png')


x = 400
y = 90
angle = 450

while(True):
    character.draw_now(x,y)
    grass.draw_now(400, 30)
    if sq:
        if(x <= 790 and y == 90):
            x = x + 2
            if(x == 400 and y == 90):
                sq = False
            delay(0.01)
        if(x == 790 and y <= 560 ):
            y = y + 2
            delay(0.01)
        if(x >= 20 and y == 560):
            x = x - 2
            delay(0.01)
        if(x == 20 and y >= 90):
            y = y - 2
            delay(0.01)
    else:
        if(angle <= 90):
            sq = True
            x,y = 400,90
            angle = 450
        else:
            cx = 405
            cy = 325
            r = 235
            radian = math.radians(angle)
            x = cx + r * math.cos(radian)
            y = cy + r * math.sin(radian)
            angle = angle - 5
            delay(0.05)
    clear_canvas_now()