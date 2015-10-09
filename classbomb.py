from pico2d import *
import os
os.chdir('c://2DGP//Image')
import random

open_canvas()

class Map:
    def __init__(self):
        self.image=load_image('background.png')

    def draw(self):
        self.image.draw(400,300)

class Bomb:

    def __init__(self):#take the picture part
        self.count=0
        self.time=0
        self.boomceframe=0
        self.chx=None
        #self.x=0
        #self.y=0
        if(self.time==0):
            self.chx=50#터질때 화면에서 없어짐 0으로됨

            self.x, self.y=random.randrange(40,650,40),random.randrange(60,500,40)

            #self.count=1
        self.boomframe=random.randint(0,7)

        self.frame=random.randint(0,4)
        
        self.image=load_image('bluebub2.jpg')
        self.boomce=load_image('boomcenter.bmp')
        self.boomri=load_image('boomright.png')
        self.boomle=load_image('boomleft.png')
        self.boomup=load_image('boomup.png')
        self.boomdo=load_image('boomdown.png')
    def update(self):#frame about bombanimation
        #global bomb
        self.frame=(self.frame+1)%4
        self.time+=1
        self.boomceframe=(self.boomceframe+1)%3

        self.boom=(self.boomframe+1)%8
        if(self.time==10):
            self.explode()
            self.x, self.y=random.randrange(40,610,40),random.randrange(60,500,40)
            #self.count=0

            #self.chx=0
            self.time=0


    def draw(self):# bomb draw part
        self.image.clip_draw(self.frame*45,0,47,self.chx,self.x,self.y)
    def explode(self):

        self.boomce.clip_draw(self.boomceframe*50,0,40,50,self.x,self.y)
        self.boomri.clip_draw(self.boomframe*40,0,40,50,self.x+40,self.y)
        self.boomle.clip_draw(self.boomframe*40,0,40,50,self.x-40,self.y)
        self.boomup.clip_draw(self.boomframe*40,0,40,50,self.x,self.y+50)
        self.boomdo.clip_draw(self.boomframe*40,0,40,50,self.x,self.y-50)
            
            #self.x, self.y=random.randrange(40,650,40),random.randrange(60,500,40)



def mathsqrt(bx,by,bx2,by2):
    return math.sqrt((bx2-bx) *(bx2-bx) + (by2-by)*(by2-by))

running=True
bomb=Bomb()
bomb2=Bomb()
ma=Map()
timer=0
count=0
bombteam=[Bomb() for i in range(11)]
while running:
    clear_canvas()
    count=0
    timer+=1
    ma.draw()

    
    
    for bomb in bombteam:
        bomb.update()
        bomb.draw()


        
        
    update_canvas()
    get_events()
    delay(0.2)

    
    
