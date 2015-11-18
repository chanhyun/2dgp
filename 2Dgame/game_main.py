from pico2d import*#*는 몽땅다
import game_framework
import gameover
import os
import random
import json
os.chdir('c://2dgame//image')

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
        self.boomframe=0
        self.dieframe=0

        self.aidieframe=0

        if(self.time==0):


            self.x, self.y=random.randrange(40,650,40),random.randrange(60,500,40)


        #self.boomframe=(self.boomframe+1)

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
        global itemstar
        global blockteam
        global block
        self.frame=(self.frame+1)%4
        self.time+=1
        self.boomceframe=(self.boomceframe+1)%3

        #self.boomframe=(self.boomframe+1)%8
        for block in blockteam:
            if(block.blx == self.x and block.bly==self.y):
                self.x, self.y=random.randrange(40,570,40),random.randrange(60,500,40)#폭탄과 벽의 중복사라지게하는곳


        if(self.dieframe<4 and self.count==3):
            self.dieframe=(self.dieframe+1)

        elif(self.dieframe==4):
            game_framework.push_state(gameover)
        if(self.aidieframe<4 and self.count==5):
            self.aidieframe=(self.aidieframe+1)
        elif(self.aidieframe==4):
            game_framework.push_state(gameover)




        if(self.time==11):
             self.x, self.y=random.randrange(40,610,40),random.randrange(60,500,40)
             self.time=0




    def draw(self,timer):# bomb draw part
        global cx,cy
        global ch
        global right,left,up,down
        self.image.clip_draw(self.frame*45,0,47,50,self.x,self.y)
        if(self.time==10):

            self.explode(timer)
        #if(self.count==3):
            #self.bye.clip_draw(self.boomframe*68,0,69,105,cx,cy)



    def explode(self,timer):
        global cx,cy
        global bombcount,autoai

        self.boomce.clip_draw(self.boomceframe*50,0,40,50,self.x,self.y)

        self.boomri.clip_draw(self.boomframe*40,0,40,50,self.x+40,self.y)

        self.boomle.clip_draw(self.boomframe*40,0,40,50,self.x-40,self.y)

        self.boomup.clip_draw(self.boomframe*40,0,40,50,self.x,self.y+40)

        self.boomdo.clip_draw(self.boomframe*40,0,40,50,self.x,self.y-40)

        if((self.x+40==cx and self.y==cy) or (self.x-40==cx and self.y==cy) or (self.x==cx and self.y+40==cy)or (self.x==cx and self.y-40==cy)):
            self.count=3#캐릭죽을때
            for block in blockteam:
                if((self.x+40==block.blx and self.y==block.bly) or (self.x-40==block.blx and self.y==block.bly) or (self.x==block.blx and self.y+40==block.bly)or (self.x==block.blx and self.y-40==block.bly)):
                    self.count=0
        if(timer>50):
            for i in range(0,keyinputcount):
            #autoai[i].draw()
                if((self.x+40==autoai[i].aix and self.y==autoai[i].aiy) or (self.x-40==autoai[i].aix and self.y==autoai[i].aiy) or (self.x==autoai[i].aix and self.y+40==autoai[i].aiy)or (self.x==autoai[i].aix and self.y-40==autoai[i].aiy)):
                    autoai[i].life-=1
                    if(autoai[i].life==0  ):
                        self.count=5#ai죽을때
                        #ai_diecount+=1
                                #if(diecount==KEyinputcount)
                                #self.count==5






class Map:
    image =None
    def __init__(self):
        if Map.image==None:
            self.map=load_image('background.png')
            self.font=load_font('ENCOBK.TTF')
    def draw(self):
        self.map.draw(400,300)
        self.font.draw(30,550, '%d' %score)








class Ch:
    PIXEL_PER_METER=(10.0/0.6896)
    RUN_SPEED_KMPH=10.0
    RUN_SPEED_MPM=(RUN_SPEED_KMPH*1000.0/60.0)
    RUN_SPEED_MPS=(RUN_SPEED_MPM/60.0)
    RUN_SPEED_PPS=(RUN_SPEED_MPS * PIXEL_PER_METER)


    TIME_PER_ACTION=0.5
    ACTION_PER_TIME=1.0/TIME_PER_ACTION
    FRAMES_PER_ACTION=8

    def __init__(self):

        global cx,cy
        global right,left,up,down
        self.total_frames=0
        self.chframe=0
        self.sttimer=0

        self.chdo=load_image('downp.png')
        self.chri=load_image('rightp.png')
        self.chle=load_image('leftp.png')
        self.chup=load_image('upp.png')
        ###아이템 사용후 슈퍼맨모습
        self.star=load_image('star.png')
        self.itemai=load_image('itemai.png')
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
        global itemaix,itemaiy
        #sx=40
        #sy=27
        global bomb
        for bomb in bombteam:
            if bomb.count==3:
                bomb.bye.clip_draw(bomb.dieframe*68,0,69,105,cx,cy)



                break;
        if(bomb.count !=3):
            self.star.clip_draw(9,10,sx,sy,262,15)
            self.itemai.clip_draw(2,5,itemaix,itemaiy,300,15)

            self.chdo.clip_draw(self.chframe*44,0,42,60,cx,cy)

            if(right==True):
                self.chri.clip_draw(self.chframe*44,0,42,60,cx,cy)
                self.chframe=(self.chframe+1)%8
            elif(left==True):
                self.chle.clip_draw(self.chframe*44,0,42,60,cx,cy)
                self.chframe=(self.chframe+1)%8
            elif(up==True):
                self.chup.clip_draw(self.chframe*44,0,42,60,cx,cy)
                self.chframe=(self.chframe+1)%8
            elif(down==True):
                self.chdo.clip_draw(self.chframe*44,0,42,60,cx,cy)
                self.chframe=(self.chframe+1)%8
            if (stcount==True):
                self.starchdo.clip_draw(self.chframe*44,0,42,60,cx,cy)
                self.chframe=(self.chframe+1)%8
            if (stcount==True and right):
                self.starchri.clip_draw(self.chframe*44,0,42,60,cx,cy)
                self.chframe=(self.chframe+1)%8
            elif (stcount==True and left):
                self.starchle.clip_draw(self.chframe*44,0,42,60,cx,cy)
                self.frame=(self.chframe+1)%8
            elif (stcount==True and up):
                self.starchup.clip_draw(self.chframe*44,0,42,60,cx,cy)
                self.frame=(self.chframe+1)%8
            elif (stcount==True and down):
                self.starchdo.clip_draw(self.chframe*44,0,42,60,cx,cy)
                self.chframe=(self.chframe+1)%8




    def update(self):
        self.total_frames +=Ch.FRAMES_PER_ACTION*Ch.ACTION_PER_TIME*frame_time
        global right,left,up,down#0 오른쪽 1 왼쪽 2 위 3아
        global stcount
        global cx,cy
        global sx,sy
        global itemstar
        global blockteam
        global bombteam
        self.frame=int(self.total_frames)%8

        if(right==True):
            cx=cx+int(Ch.RUN_SPEED_PPS)

            if(cx>600):
                cx-=int(Ch.RUN_SPEED_PPS)
            for block in blockteam:
                if(block.blockcheck==True and block.blx == cx and block.bly==cy):
                    cx=cx-int(Ch.RUN_SPEED_PPS)
                    break;

            for bomb in bombteam:
                if(bomb.x == cx and bomb.y==cy and itemstar==False):
                    cx=cx-int(Ch.RUN_SPEED_PPS)
                    break;

        elif(left==True):
            cx=cx-int(Ch.RUN_SPEED_PPS)

            if(cx<40):
                cx+=int(Ch.RUN_SPEED_PPS)
            for block in blockteam:
                if(block.blockcheck==True and block.blx == cx and block.bly==cy):
                    cx=cx+int(Ch.RUN_SPEED_PPS)
                    break;
            for bomb in bombteam:
                if(bomb.x == cx and bomb.y==cy and itemstar==False):
                    cx=cx+int(Ch.RUN_SPEED_PPS)
                    break;
        elif(up==True):
            cy=cy+int(Ch.RUN_SPEED_PPS)

            if(cy>552):
                cy-=int(Ch.RUN_SPEED_PPS)
            for block in blockteam:
                if(block.blockcheck==True and block.blx == cx and block.bly==cy):
                    cy=cy-int(Ch.RUN_SPEED_PPS)

                    break;
            for bomb in bombteam:
                if(bomb.x == cx and bomb.y==cy and itemstar==False):
                    cy=cy-int(Ch.RUN_SPEED_PPS)
                    break;
        elif(down==True):
            cy=cy-int(Ch.RUN_SPEED_PPS)

            if(cy<45):
                cy+=int(Ch.RUN_SPEED_PPS)
            for block in blockteam:
                if(block.blockcheck==True and block.blx == cx and block.bly==cy):
                    cy=cy+int(Ch.RUN_SPEED_PPS)
                    break;
            for bomb in bombteam:
                if(bomb.x == cx and bomb.y==cy and itemstar==False):
                    cy=cy+int(Ch.RUN_SPEED_PPS)
                    break;
        if(stcount==True):
            self.sttimer+=1

            if(self.sttimer==30):
                stcount=False
                self.sttimer=0
                itemstar=False


###AI를  JSON화 시킵니다
def create_ai():
    global keyinputcount

    ai_data_text = '{"0":{"StartState":"RIGHT","x":40,"y":100},"1":{"StartState":"LEFT","x":40,"y":500},"2":{"StartState":"UP","x":120,"y":220}}'

    ai_state_table={
        "RIGHT":AI.RIGHT,
        "LEFT":AI.LEFT,
        "UP":AI.UP,
        "DOWN":AI.DOWN


    }

    ai_select_table = {
        0 : "0",
        1 : "1",
        2 : "2"
    }

    ai_data = json.loads(ai_data_text)

    aiteam=[]
    for i in range(0,keyinputcount):
        ai=AI()
        ai.select = ai_data[ai_select_table[i]]
        ai.aix=ai.select['x']
        ai.aiy=ai.select['y']
        ai.state=ai_state_table[ai.select['StartState']]
        aiteam.append(ai)
    return aiteam


class AI:

    RIGHT,LEFT,UP,DOWN=0,1,2,3
    def RIGHT_RUN(self):
        self.aix+=int(Ch.RUN_SPEED_PPS)
        for block in blockteam:
            if(block.blockcheck==True and block.blx == self.aix and block.bly==self.aiy):
                self.aix=self.aix-int(Ch.RUN_SPEED_PPS)
                break;
        for bomb in bombteam:
            if(bomb.x == self.aix and bomb.y==self.aiy and itemstar==False):
                self.aix=self.aix-int(Ch.RUN_SPEED_PPS)
                break;

    def LEFT_RUN(self):
        self.aix-=int(Ch.RUN_SPEED_PPS)
        for block in blockteam:
                if(block.blockcheck==True and block.blx == self.aix and block.bly==self.aiy):
                    self.aix=self.aix+int(Ch.RUN_SPEED_PPS)
                    break;
        for bomb in bombteam:
                if(bomb.x == self.aix and bomb.y==self.aiy and itemstar==False):
                    self.aix=self.aix+int(Ch.RUN_SPEED_PPS)
                    break;

    def UP_RUN(self):
        self.aiy+=int(Ch.RUN_SPEED_PPS)
        for block in blockteam:
                if(block.blockcheck==True and block.blx == self.aix and block.bly==self.aiy):
                    self.aiy=self.aiy-int(Ch.RUN_SPEED_PPS)
                    break;
        for bomb in bombteam:
                if(bomb.x == self.aix and bomb.y==self.aiy and itemstar==False):
                    self.aiy=self.aiy-int(Ch.RUN_SPEED_PPS)
                    break;
    def DOWN_RUN(self):

        self.aiy-=int(Ch.RUN_SPEED_PPS)
        for block in blockteam:
                if(block.blockcheck==True and block.blx == self.aix and block.bly==self.aiy):
                    self.aiy=self.aiy+int(Ch.RUN_SPEED_PPS)
                    break;
        for bomb in bombteam:
            if(bomb.x == self.aix and bomb.y==self.aiy and itemstar==False):
                    self.aiy=self.aiy+int(Ch.RUN_SPEED_PPS)
                    break;
    ai_state_table={
        RIGHT:RIGHT_RUN,
        LEFT:LEFT_RUN,
        UP:UP_RUN,
        DOWN:DOWN_RUN
    }
    def __init__(self):
        self.ai=load_image('ai.bmp')

        self.aix, self.aiy=None,None
        self.aiframe=0
        self.state=self.RIGHT
        self.life=3
        self.timer=0
        self.select = "noname"

    def update(self,timer):
        global blockteam
        global bombteam
        self.aiframe=(self.aiframe+1)%4
        if timer%3==0:
            self.ai_state_table[self.state](self)


            if(self.aix<40):
                self.aix+=int(Ch.RUN_SPEED_PPS)
            if(self.aix>600):
                self.aix-=int(Ch.RUN_SPEED_PPS)
            if(self.aiy>552):
                self.aiy-=int(Ch.RUN_SPEED_PPS)
            if(self.aiy<55):
                self.aiy+=int(Ch.RUN_SPEED_PPS)
            self.state=random.randrange(0,4,1)


    def draw(self):
        global bombteam
        for bomb in bombteam:
            if bomb.count==5:
                self.ai.clip_draw(bomb.aidieframe*32,0,30,49,self.aix,self.aiy)

                #game_framework.push_state(gameover)


                break;
        if(bomb.count !=5):
            if(self.state==self.RIGHT):
                self.ai.clip_draw(self.aiframe*32,48,30,49,self.aix,self.aiy)#오른쪽
            elif(self.state==self.LEFT):
                self.ai.clip_draw(self.aiframe*32,93,30,49,self.aix,self.aiy)#왼쪽
            elif(self.state==self.UP):
                self.ai.clip_draw(self.aiframe*32,145,30,49,self.aix,self.aiy)#위
            elif(self.state==self.DOWN):
                self.ai.clip_draw(self.aiframe*32,190,30,49,self.aix,self.aiy)#아래

def handle_events():
    global cx,cy#캐릭좌표
    global sx,sy#아이템쓰고난후좌표
    global blx,bly#벽좌표
    global BSIZE#충돌체크용
    global inputcount
    global right,left,up,down# 오른쪽 왼쪽 위 아래 캐릭터방향
    global blockcheck
    global itemstar,itemaix,itemaiy
    global stcount
    global blockteam
    global block,bomb
    global blockcount,autoai
    global keyinputcount
    events=get_events()
    for event in events:
        if event.type==SDL_KEYDOWN:
            print("%d %d %d %d \n" %(right,left,up,down));

            if event.key==SDLK_RIGHT:

                right=True
                left=False
                up=False
                down=False

            elif event.key == SDLK_LEFT:
                left=True
                right=False
                up=False
                down=False
            elif event.key == SDLK_UP:
                up=True
                left=False
                right=False
                down=False
            elif event.key == SDLK_DOWN:
                down=True
                left=False
                up=False
                right=False
            elif event.key == SDLK_2:
                stcount=True
                itemstar=True
                sx=-40
                sy=-20
            elif event.key== SDLK_3:

                keyinputcount+=1

                autoai = create_ai()
            elif event.key ==SDLK_a:

                if(inputcount==0):

                    blockteam[blockcount].blockcheck=True
                    blockteam[blockcount].blx,blockteam[blockcount].bly=cx,cy
                    blockcount=(blockcount+1)%11

                    right=False
                    left=False
                    up=False
                    down=False
                    for block in blockteam:
                        for bomb in bombteam:
                            if(block.blx==bomb.x and block.bly==bomb.y):
                                inputcount=1

                    inputcount=0

        if event.type==SDL_KEYUP:
            if event.key==SDLK_RIGHT:
                right=False

            elif event.key==SDLK_LEFT:
                left=False
            elif event.key==SDLK_UP:
                up=False
            elif event.key==SDLK_DOWN:
                down=False
            #elif event.key==SDLK_a:
               #blockcheck=True
current_time=get_time()
frame_time=get_time()-current_time
keyinputcount=1
bombcount=0
time=0
itemstar=False
inputcount=0
blockcheck=False
blockcount=0
stcount=False#별 아이템 사용여부체크
sx=40#별크좌표
sy=27
itemaix=30
itemaiy=27
BSIZE=20
right=False#오른쪽
left=False#왼쪽
up=False#위
down=False#아래
cx=0#캐릭좌표
cy=0#캐릭좌표
block=None
ma=None
ch=None
bomb=None
bombteam=None
blockteam=None
score=0
autoai=None
aiteam=None





def enter():

    global ma,ch
    global blockteam
    global bombteam,autoai
    global aiteam
    global cx,cy
    global time

    cx=40
    cy=500
    bombteam=[Bomb() for i in range(11)]
    blockteam=[Block() for i in range(11)]
    ma=Map()
    ch=Ch()
    #autoai=AI()
    autoai=create_ai()

def exit():
    global ma,ch,blockteam,block,bombteam,bomb,autoai
    del(bombteam)
    del(bomb)
    del(block)
    del(blockteam)
    del(ma)
    del(ch)
    del(autoai)

def update():

    global itemstar
    global bomb
    global block
    global time
    global score
    global autoai
    global keyinputcount
    global itemaix,itemaiy
    time+=1

    for i in range(0,keyinputcount):
        autoai[i].update(time)
    ch.update()
    if(keyinputcount==3):
        itemaix=-30
        itemaiy=-27

    if(itemstar==False):
        for bomb in bombteam:
            bomb.update()
            bomb.boomframe=(bomb.boomframe+1)%8

    for block in blockteam:

        block.blockupdate()




    score+=1
    delay(0.1)


def draw():
    clear_canvas()
    global itemstar
    global bomb
    global block
    global autoai
    global time
    ma.draw()
    ch.draw()
    if time>50:
        for i in range(0,keyinputcount):
            autoai[i].draw()


    if(itemstar==False):
        for bomb in bombteam:
            bomb.draw(time)
    for block in blockteam:
        block.blockupdate()

    update_canvas()
def resume():
    pass
def pause():
    pass


