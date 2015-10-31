

import os
os.chdir('c://2dgp//image')
import classonly
import game_framework
from pico2d import *




name = "StartState"
image = None
logo_time = 0.0
bgm=None

def enter():
    global image
    global bgm
    open_canvas()
    bgm=load_music('football.mp3')
    image= load_image('kpu_credit.png')


def exit():
    global image,bgm
    del(image)
    del(bgm)
    close_canvas()

def update():
    global logo_time
    global bgm
    bgm.set_volume(128)
    bgm.play(1)
    if (logo_time>1.0):
        logo_time=0
        #game_framework.quit()#넌뭐니
        game_framework.push_state(classonly)
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




