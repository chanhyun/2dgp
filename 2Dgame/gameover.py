import game_framework
import game_main
import logo_state
from pico2d import *
import os
import score

os.chdir('c://2dgame//image')


image = None
timer=0

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
    if(timer==10):
        game_framework.push_state(score)


def pause():
    pass


def resume():
    pass






