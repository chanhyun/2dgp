

import os
os.chdir('./image')
#os.chdir('c://2dgame//music')
import game_main
import game_framework
from pico2d import *




name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image

    open_canvas()

    image= load_image('kpu_credit.png')


def exit():
    global image
    del(image)
    #del(bgm)
    close_canvas()

def update():
    global logo_time
    global bgm

    if (logo_time>1.0):
        logo_time=0
        #game_framework.quit()#넌뭐니
        game_framework.push_state(game_main)
    delay(0.01)
    logo_time +=0.01

def draw():
    global image
    clear_canvas()
    image.draw(400,300)
    update_canvas()





def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass




