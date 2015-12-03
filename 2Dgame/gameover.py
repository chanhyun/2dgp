import game_framework

from pico2d import *

import score



image = None
timer=0
badendbgm=None
def enter():
    global image
    global timer
    image = load_image('gameover.png')


def exit():
    global image,badendbgm
    del(image)
    del(badendbgm)

def handle_events():
    pass




def draw():
    clear_canvas()

    image.draw(400,300,800,600)
    update_canvas()







def update():

    global timer
    timer+=1
    if(timer==100):
        game_framework.push_state(score)


def pause():
    pass


def resume():
    pass






