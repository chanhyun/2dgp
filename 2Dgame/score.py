
from pico2d import*
import os
import game_main

os.chdir('c://2dgame//image')
scoreimage=None
score=0
mapfont=None
def enter():
    global scoreimage
    global badendbgm,mapfont,score
    score=game_main.score
    mapfont=game_main.Map()
    mapfont.font=load_font('ENCOBK.TTF',50)
    scoreimage=load_image('scoreview.png')


def exit():
    
    del(mapfont.font.draw)
    del(badendbgm)

def handle_events():
    pass




def draw():
    global score
    global scoreimage
    clear_canvas()
    scoreimage.draw(400,300,800,600)
    mapfont.font.draw(400,300, '%d' %score,(255,255,0))

    update_canvas()







def update():
    pass


def pause():
    pass


def resume():
    pass






