
from pico2d import*
import game_main
import game_framework
badendbgm=None
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
    global mapfont,badendbgm
    del(mapfont)
    del(badendbgm)

def handle_events():
    events=get_events()
    for event in events:
        if event.type==SDL_KEYDOWN:
            if event.key==SDLK_ESCAPE:


                close_canvas()



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






