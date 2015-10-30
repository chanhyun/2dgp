from pico2d import*#*는 몽땅다
import game_framework
import gameover
import os
import random

os.chdir('c://2dgp//image')

class Block:
    def __init__(self):
        global cx,cy
        global ch
        self.blockcheck=False
        self.blx,self.bly=cx,cy

        #self.count=0#벽이 설치됫다면 1로
        
        #self.block[2][100]
        self.block=load_image('wall.png')
        self.count=0

    def blockupdate(self):


        if(self.blockcheck==True):
            self.block.draw(self.blx,self.bly)
     
       
   
class Bomb:

    def __init__(self):#take the picture part
        self.count=0
        self.time=0
        self.boomceframe=0
        self.dieframe=0
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
        self.bye=load_image('bye.png')
    def update(self):#frame about bombanimation
        #global bomb
        global itemuse
        global blockteam
        global block
        self.frame=(self.frame+1)%4
        self.time+=1
        self.boomceframe=(self.boomceframe+1)%3

        self.boomframe=(self.boomframe+1)%8
        for block in blockteam:
            if(block.blx == self.x and block.bly==self.y):
                self.x, self.y=random.randrange(40,570,40),random.randrange(60,500,40)#폭탄과 벽의 중복사라지게하는곳


        if(self.dieframe<4 and self.count==3):
            self.dieframe=(self.dieframe+1)

        elif(self.dieframe==4):
            game_framework.push_state(gameover)




        if(self.time==11):
             self.x, self.y=random.randrange(40,610,40),random.randrange(60,500,40)
             self.time=0

            


    def draw(self):# bomb draw part
        global cx,cy
        global ch
        global run,run2,run3,run4
        self.image.clip_draw(self.frame*45,0,47,self.chx,self.x,self.y)
        if(self.time==10):

            self.explode()
        #if(self.count==3):
            #self.bye.clip_draw(self.boomframe*68,0,69,105,cx,cy)



    def explode(self):
        global cx,cy
        global bombcount

        self.boomce.clip_draw(self.boomceframe*50,0,40,50,self.x,self.y)

        self.boomri.clip_draw(self.boomframe*40,0,40,50,self.x+40,self.y)

        self.boomle.clip_draw(self.boomframe*40,0,40,50,self.x-40,self.y)

        self.boomup.clip_draw(self.boomframe*40,0,40,50,self.x,self.y+40)

        self.boomdo.clip_draw(self.boomframe*40,0,40,50,self.x,self.y-40)

        if((self.x+40==cx and self.y==cy) or (self.x-40==cx and self.y==cy) or (self.x==cx and self.y+40==cy)or (self.x==cx and self.y-40==cy)):
            self.count=3
            for block in blockteam:
                if((self.x+40==block.blx and self.y==block.bly) or (self.x-40==block.blx and self.y==block.bly) or (self.x==block.blx and self.y+40==block.bly)or (self.x==block.blx and self.y-40==block.bly)):
                    self.count=0














class Map:
    def __init__(self):
        self.map=load_image('background.png')
        self.font=load_font('ENCOBK.TTF')
    def draw(self):
        global x
        self.map.draw(400,300)
        self.font.draw(30,550, '%d'%score)





















class Ch:
    def __init__(self):

        global cx,cy
        global run,run2,run3,run4
        self.itemusetime=0
        self.chframe=0
        self.sttimer=0
        
        self.chdo=load_image('downp.png')
        self.chri=load_image('rightp.png')
        self.chle=load_image('leftp.png')
        self.chup=load_image('upp.png')
        ###아이템 사용후 슈퍼맨모습
        self.star=load_image('star.png')
        self.starchdo=load_image('itemdown.png')
        self.starchri=load_image('itemright.png')
        self.starchup=load_image('itemup.png')
        self.starchle=load_image('itemleft.png')
        self.chx,self.chy=20,500
        #cx=40
        #cy=500
    def draw(self):
        global bombteam
        global sx,sy
        #sx=40
        #sy=27
        global bomb
        for bomb in bombteam:
            if bomb.count==3:
                bomb.bye.clip_draw(bomb.dieframe*68,0,69,105,cx,cy)



                break;
        if(bomb.count !=3):
            self.star.clip_draw(9,10,sx,sy,262,15)
        
            self.chdo.clip_draw(self.chframe*44,0,42,60,cx,cy)
        
            if(run==True):
                self.chri.clip_draw(self.chframe*44,0,42,60,cx,cy)
                self.chframe=(self.chframe+1)%8
            elif(run2==True):
                self.chle.clip_draw(self.chframe*44,0,42,60,cx,cy)
                self.chframe=(self.chframe+1)%8
            elif(run3==True):
                self.chup.clip_draw(self.chframe*44,0,42,60,cx,cy)
                self.chframe=(self.chframe+1)%8
            elif(run4==True):
                self.chdo.clip_draw(self.chframe*44,0,42,60,cx,cy)
                self.chframe=(self.chframe+1)%8
            if (stcount==True):
                self.starchdo.clip_draw(self.chframe*44,0,42,60,cx,cy)
                self.chframe=(self.chframe+1)%8
            if (stcount==True and run):
                self.starchri.clip_draw(self.chframe*44,0,42,60,cx,cy)
                self.chframe=(self.chframe+1)%8
            elif (stcount==True and run2):
                self.starchle.clip_draw(self.chframe*44,0,42,60,cx,cy)
                self.frame=(self.chframe+1)%8
            elif (stcount==True and run3):
                self.starchup.clip_draw(self.chframe*44,0,42,60,cx,cy)
                self.frame=(self.chframe+1)%8
            elif (stcount==True and run4):
                self.starchdo.clip_draw(self.chframe*44,0,42,60,cx,cy)
                self.chframe=(self.chframe+1)%8




    def update(self):
        global run,run2,run3,run4#0 오른쪽 1 왼쪽 2 위 3아
        global stcount
        global cx,cy
        global sx,sy
        global itemuse
        global blockteam
        global bombteam
        self.frame=(self.chframe+1)%8

        if(run==True):
            cx=cx+40
            
            if(cx>600):
                cx-=40
            for block in blockteam:
                if(block.blockcheck==True and block.blx == cx and block.bly==cy):
                    cx=cx-40
                    break;

            for bomb in bombteam:
                if(bomb.x == cx and bomb.y==cy and itemuse==False):
                    cx=cx-40
                    break;

        elif(run2==True):
            cx=cx-40
         
            if(cx<40):
                cx+=40
            for block in blockteam:
                if(block.blockcheck==True and block.blx == cx and block.bly==cy):
                    cx=cx+40
                    break;
            for bomb in bombteam:
                if(bomb.x == cx and bomb.y==cy and itemuse==False):
                    cx=cx+40
                    break;
        elif(run3==True):
            cy=cy+40
         
            if(cy>552):
                cy-=40
            for block in blockteam:
                if(block.blockcheck==True and block.blx == cx and block.bly==cy):
                    cy=cy-40

                    break;
            for bomb in bombteam:
                if(bomb.x == cx and bomb.y==cy and itemuse==False):
                    cy=cy-40
                    break;
        elif(run4==True):
            cy=cy-40
          
            if(cy<45):
                cy+=40
            for block in blockteam:
                if(block.blockcheck==True and block.blx == cx and block.bly==cy):
                    cy=cy+40
                    break;
            for bomb in bombteam:
                if(bomb.x == cx and bomb.y==cy and itemuse==False):
                    cy=cy+40
                    break;
        if(stcount==True):
            self.sttimer+=1
            
            if(self.sttimer==30):
                stcount=False
                self.sttimer=0
                itemuse=False
      
        

class AI:
    def __init__(self):
        self.ai=load_image('ai.bmp')

        self.aix, self.aiy=100,40
        self.aiframe=0
        self.aiwaycount=0
        self.timer=0
    def update(self):
        self.aiwaycount=random.randrange(0,3,1)
        self.aiframe=(self.aiframe+1)%4
        if(self.aiwaycount==0):

           self.aix+=20

        elif(self.aiwaycount==1):

            self.aix-=20

        elif(self.aiwaycount==2):
            pass
        elif(self.aiwaycount==3):
            pass
        if(self.aix+20<20):
            self.aiy-=20
        if(self.aix+20>600):
            self.aix-=20

    def draw(self):
        if(self.aiwaycount==0):
           self.ai.clip_draw(self.aiframe*32,48,30,49,self.aix+20,self.aiy+500)
        elif(self.aiwaycount==1):
            self.ai.clip_draw(self.aiframe*32,93,30,49,self.aix+20,self.aiy+500)

def handle_events():
    global cx,cy#캐릭좌표
    global sx,sy#아이템쓰고난후좌표
    global blx,bly#벽좌표
    global BSIZE#충돌체크용
    global inputcount
    global run,run2,run3,run4# 오른쪽 왼쪽 위 아래 캐릭터방향
    global blockcheck
    global itemuse
    global stcount
    global blockteam
    global block,bomb
    global blockcount
    events=get_events()
    for event in events:
        if event.type==SDL_KEYDOWN:
            print("%d %d %d %d \n" %(run,run2,run3,run4));

            if event.key==SDLK_RIGHT:

                run=True
                run2=False
                run3=False
                run4=False

            elif event.key == SDLK_LEFT:
                run2=True
                run=False
                run3=False
                run4=False
            elif event.key == SDLK_UP:
                run3=True
                run2=False
                run=False
                run4=False
            elif event.key == SDLK_DOWN:
                run4=True
                run2=False
                run3=False
                run=False
            elif event.key == SDLK_2:
                stcount=True
                itemuse=True
                sx=-40
                sy=-20
            elif event.key ==SDLK_a:

                if(inputcount==0):

                    blockteam[blockcount].blockcheck=True
                    blockteam[blockcount].blx,blockteam[blockcount].bly=cx,cy
                    blockcount=(blockcount+1)%11

                    run=False
                    run2=False
                    run3=False
                    run4=False
                    for block in blockteam:
                        for bomb in bombteam:
                            if(block.blx==bomb.x and block.bly==bomb.y):
                                inputcount=1

                    inputcount=0

        if event.type==SDL_KEYUP:
            if event.key==SDLK_RIGHT:
                run=False

            elif event.key==SDLK_LEFT:
                run2=False
            elif event.key==SDLK_UP:
                run3=False
            elif event.key==SDLK_DOWN:
                run4=False
            #elif event.key==SDLK_a:
               #blockcheck=True
def mathsqrt(cx,cy,blx,b1y):
    return math.sqrt((cx-blx) *(cx-blx) + (cy-bly)*(cy-bly))
bombcount=0
time=0
itemuse=False
inputcount=0
blockcheck=False
blockcount=0
stcount=False#별 아이템 사용여부체크
sx=40#별크좌표
sy=27
BSIZE=20
run=False#오른쪽
run2=False#왼쪽
run3=False#위
run4=False#아래
cx=0#캐릭좌표
cy=0#캐릭좌표
block=None
ma=None
ch=None
bomb=None
bombteam=None
blockteam=None
score=0
auto=None






def enter():

    global ma,ch
    global blockteam
    global bombteam,auto
    global cx,cy
    cx=40
    cy=500
    bombteam=[Bomb() for i in range(11)]
    blockteam=[Block() for i in range(11)]
    ma=Map()
    ch=Ch()
    auto=AI()

def exit():
    global ma,ch,blockteam,block,bombteam,bomb,auto
    del(bombteam)
    del(bomb)
    del(block)
    del(blockteam)
    del(ma)
    del(ch)
    del(auto)

def update():

    global itemuse
    global bomb
    global block
    global time
    global score
    time+=1

    ch.update()
    auto.update()
    if(itemuse==False):
        for bomb in bombteam:
            bomb.update()

    for block in blockteam:

        block.blockupdate()
    #if(time==50):

    score+=1
    delay(0.1)


def draw():
    clear_canvas()
    global itemuse
    global bomb
    global block
    global auto
    ma.draw()
    ch.draw()
    auto.draw()
    if(itemuse==False):
        for bomb in bombteam:
            bomb.draw()
    for block in blockteam:
        block.blockupdate()

    update_canvas()
def resume():
    pass
def pause():
    pass


