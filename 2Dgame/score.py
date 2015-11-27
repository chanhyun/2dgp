
from pico2d import*
import os
import game_main

os.chdir('c://2dgame//image')

score=0
mapfont=None
def enter():
    global image
    global badendbgm,mapfont,score
    score=game_main.score
    mapfont=game_main.Map()
    


def exit():
    
    del(mapfont.font.draw)
    del(badendbgm)

def handle_events():
    pass




def draw():
    global score
    clear_canvas()

    mapfont.font.draw(30,550, '%d' %score)
    update_canvas()







def update():
    pass


def pause():
    pass


def resume():
    pass






