import game_framework
import game_main
import logo_state
from pico2d import *
import os
os.chdir('c://2dgame//image')


image = None
badendbgm=None

def enter():
    global image
    image = load_image('gameover.png')

def exit():
    global image
    del(image)


def handle_events():
    pass




def draw():
    clear_canvas()

    image.draw(400,300,800,600)
    update_canvas()







def update():
    pass


def pause():
    pass


def resume():
    pass






