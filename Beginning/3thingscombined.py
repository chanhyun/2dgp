from pico2d import*#*는 몽땅다
from math import*
import random
import os

os.chdir('c://2dgp//image')
open_canvas()
wall=load_image('wall.png')#벽이미지
background=load_image('background.png')#배경
#bomb=load_image('bluebub2.jpg')
chdo=load_image('downp.png')#캐릭터아래
chri=load_image('rightp.png')#캐릭터오른쪽
chle=load_image('leftp.png')#캐릭터왼쪽
chup=load_image('upp.png')#캐릭터위
ch=load_image('downp.png')
star=load_image('star.png')#별이미지
starchdo=load_image('itemdown.png')#슈퍼맨아래
starchle=load_image('itemleft.png')#슈퍼맨왼쪽
starchri=load_image('itemright.png')#슈퍼맨오른쪽
starchup=load_image('itemup.png')#슈퍼맨위쪽
ai=load_image('ai.bmp')#ai
bye=load_image('bye.png')
waterjail=load_image('waterjail.png')
#starch
class Bomb:

    def __init__(self):#take the picture part
        self.count=0#폭탄물 맞을때 5
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
        self.byex=0
        self.byey=0
        self.frame=random.randint(0,4)
        self.bye=load_image('bye.png')
        self.waterjail=load_image('waterjail.png')
        self.image=load_image('bluebub2.jpg')
        self.boomce=load_image('boomcenter.bmp')
        self.boomri=load_image('boomright.png')
        self.boomle=load_image('boomleft.png')
        self.boomup=load_image('boomup.png')
        self.boomdo=load_image('boomdown.png')
        ####여기서부터 이제 중요한 폭탄 충돌 체크 입니다.
    def update(self):#frame about bombanimation
        global bombteam#재귀함수처럼 불러오시면됩니당!!!!!
        global BSIZE
        global cx,cy#두근두근 캐릭터 좌표..
        global mathdistance
        global run,run2,run3,run4
        global bmx,bmy
        global byecheck

        self.byex=cx
        self.byey=cy

        math.sqrt(((cx+65)-self.x) *((cx+65)-self.x) + ((cy+500)-self.y)*((cy+500)-self.y))#캐릭방향오른쪽으로못감 폭탄기준

        self.frame=(self.frame+1)%4
        self.time+=1
        self.boomceframe=(self.boomceframe+1)%3
        self.boom=(self.boomframe+1)%8

        if(math.sqrt(((cx+65)-self.x) *((cx+65)-self.x) + ((cy+500)-self.y)*((cy+500)-self.y))<BSIZE+10):#오른쪽
            run=False
        elif(math.sqrt(((cx-5)-self.x) *((cx-5)-self.x) + ((cy+500)-self.y)*((cy+500)-self.y))<BSIZE+10):
            run2=False
        elif(math.sqrt(((cx+40)-self.x) *((cx+40)-self.x) + ((cy+540)-self.y)*((cy+540)-self.y))<BSIZE+10):
            run3=False
        elif(math.sqrt(((cx+40)-self.x) *((cx+40)-self.x) + ((cy+460)-self.y)*((cy+460)-self.y))<BSIZE+10):
            run4=False
        if(self.count==5):

            if(math.sqrt(((cx+60)-bmx+20) *((cx+60)-bmx+20) + ((cy+500)-bmy)*((cy+500)-bmy))<BSIZE+10):

                self.count=6
                byecheck=1

            elif(math.sqrt(((cx-15)-bmx+20) *((cx-15)-bmx+20) + ((cy+500)-bmy)*((cy+500)-bmy))<BSIZE+10):
                byecheck=1
                self.count= 6

            elif(math.sqrt(((cx+40)-bmx) *((cx+40)-bmx) + ((cy+540)-bmy+10)*((cy+540)-bmy+10))<BSIZE+10):#아래
                byecheck=1
                self.count=6

            elif(math.sqrt(((cx+40)-bmx) *((cx+40)-bmx) + ((cy+460)-bmy-10)*((cy+460)-bmy-10))<BSIZE+10):
                byecheck=1
                self.count=6








        if(self.time==10):
            self.explode()
            self.x, self.y=random.randrange(40,610,40),random.randrange(60,500,40)



            self.time=0


    def draw(self):# bomb draw part
        self.image.clip_draw(self.frame*45,0,47,self.chx,self.x,self.y)
    def explode(self):
        global bmx,bmy
        bmx=self.x
        bmy=self.y
        self.boomce.clip_draw(self.boomceframe*50,0,40,50,bmx,bmy)
        self.boomri.clip_draw(self.boomframe*40,0,40,50,bmx+40,bmy)
        self.boomle.clip_draw(self.boomframe*40,0,40,50,bmx-40,bmy)
        self.boomup.clip_draw(self.boomframe*40,0,40,50,bmx,bmy+50)
        self.boomdo.clip_draw(self.boomframe*40,0,40,50,bmx,bmy-50)
        self.count=5



def handle_events():
    global running#캐릭움직이게 변수
    global cx,cy#캐릭터좌표
    global box,boy#포탄좌표
    global blx,bly#박스좌표
    global BSIZE
    global count,stcount,starnocount#방향전환 변수,아이템 별의 사라짐유무변수
    global sx,sy#star 좌표
    global run,run2,run3,run4#오른쪽,왼쪽,위,아래
    global mx,my
    global timer,aitimer
    global blockcheck#벽이 설치됬는지 안됬는지 체크 0은 벽을 그대로남긴다1은 됨
    global mathdistance


    global rmx,rmy#벽이남아있게하는 좌표
    events = get_events()
    for event in events:
        if event.type==SDL_KEYDOWN:
            if event.key==SDLK_RIGHT:
                count=1#오른쪽

                run=True
                run2=False
                run3=False
                run4=False
                #a= [[0]*3] *4
                #a[0][1]=3

            elif event.key == SDLK_LEFT:
                count=2#왼쪽

                run1=False
                run2=True
                run3=False
                run4=False


            elif event.key==SDLK_UP:
                count=3#위

                run1=False
                run2=False
                run3=True
                run4=False


            elif event.key == SDLK_DOWN:
                count=4#아래

                run1=False
                run2=False
                run3=False
                run4=True


            elif event.key == SDLK_a:
                blockcheck=True


                blx,bly=cx+40,cy+500
                wall.draw(blx,bly)
            elif event.key == SDLK_2:
                stcount=True
                starnocount=1
                sx=-40
                sy=-27

        if event.type==SDL_KEYUP:

            if event.key==SDLK_RIGHT:

                run=False

            elif event.key==SDLK_LEFT:

                run2=False

            elif event.key==SDLK_UP:

                run3=False

            elif event.key==SDLK_DOWN:

                run4=False





def mathsqrt(cx,cy,blx,b1y):
    return math.sqrt(((cx+40)-blx) *((cx+40)-blx) + ((cy+500)-bly)*((cy+500)-bly))


starnocount=None
byecheck=0
bmx=0
bmy=0
run=False#오른쪽
run2=False#왼쪽키
run3=False#위키
run4=False#아래키
running=True
count=0
frame=0#애니메이션프레임
aiframe=0
timer=0#시간
cx,cy=0,0#캐릭터좌표
mx,my=400,300#맵좌표
sx,sy=0,0
blockcheck=False
stcount=False
box=90
BSIZE=20
aix=0#ai x좌표
aiy=0#ai y좌표
aitimer=0#ai나오는시
aicount=0
frame1=0
blx,bly=cx+40,cy+500
byex=0
byey=0
mathdistanceri=None
checkcheck=False
mathdistancele=None
mathdistanceup=None
mathdistancedown=None
bomb=Bomb()
bombteam=[Bomb() for i in range(11)]
while(running):
    clear_canvas()

    aitimer+=1
    aiframe=(aiframe+1)%4
    background.draw(mx,my)
    #wall.draw(mx,my)
    if(checkcheck==False):
        for bomb in bombteam:
            bomb.update()
            bomb.draw()
    if(run==False and run2==False and run3==False and run4==False):
        chdo.clip_draw(0,0,42,60,cx+40,cy+500)

    star.clip_draw(9,10,sx+40,sy+27,262,15)
    ##폭탄부분
    #bomb.clip_draw(frame1*45,0,48,49,box,90)
    #frame1=(frame1+1)%4
    ##아이템사용부분
    if(stcount==True and run==False and run2==False and run3==False and run4==False):
        checkcheck=True#폭탄다없앰
        starchdo.clip_draw(frame*44,0,42,60,cx+40,cy+500)
        frame=(frame+1)%8
        timer+=1#아이템사용시간 증가
    if(timer==50 and starnocount==1):#별을쓰고난후의 아이템지속시간은 50초?
        stcount=False
        checkcheck=False
        timer=0

    #star.clip_draw(10,10,0,0,100,200)

    ##벽설치부분및 벽과의충돌체크
    if(blockcheck):
        wall.draw(blx,bly)



        if(mathsqrt(cx-25,cy,blx,bly)<BSIZE+10):#왼쪽방향

            run2=False


        elif(mathsqrt(cx+25,cy,blx,bly)<BSIZE+10):#오른쪽방향
            run=False
        elif(mathsqrt(cx,cy+25,blx,bly)<BSIZE+15):
            run3=False
        elif(mathsqrt(cx,cy-25,blx,bly)<BSIZE+15):
            run4=False




    ##여기는 캐릭터의 방향전환 부분
    if(count==1 and run):
        cx=cx+40

        chri.clip_draw(frame*44,0,42,60,cx+40,cy+500)
        frame=(frame+1)%8

    elif(count==2 and run2):
        cx=cx-40
        chle.clip_draw(frame*44,0,42,60,cx+40,cy+500)
        frame=(frame+1)%8
    elif(count==3 and run3):
        cy=cy+40
        chup.clip_draw(frame*44,0,42,60,cx+40,cy+500)
        frame=(frame+1)%8
    elif(count==4 and run4) :
        cy=cy-40
        chdo.clip_draw(frame*44,0,42,60,cx+40,cy+500)
        frame=(frame+1)%8
    ##캐릭터 아이템쓰고(무적)난 후의 방향전환코딩부분

    if (stcount==True and run and count==1):
        starchri.clip_draw(frame*44,0,42,60,cx+40,cy+500)
        frame=(frame+1)%8
    elif (stcount==True and run2 and count==2):
        starchle.clip_draw(frame*44,0,42,60,cx+40,cy+500)
        frame=(frame+1)%8
    elif (stcount==True and run3 and count==3):
        starchup.clip_draw(frame*44,0,42,60,cx+40,cy+500)
        frame=(frame+1)%8
    elif (stcount==True and run4 and count==4):
        starchdo.clip_draw(frame*44,0,42,60,cx+40,cy+500)
        frame=(frame+1)%8



    if(byecheck==1):#가실때
        bmx=cx+40
        bmy=cy+500
        bye.clip_draw(frame*68,0,69,105,bmx,bmy)
        chup.clip_draw(0,0,0,0,0,0)
        chdo.clip_draw(0,0,0,0,0,0)
        chle.clip_draw(0,0,0,0,0,0)
        chri.clip_draw(0,0,0,0,0,0)
        frame=(frame+1)%8
        run=False
        run2=False
        run3=False
        run4=False
        cx=-400
        cy=-400

        # self.bye.clip_draw(self.boomframe*68,0,69,105,self.byex+40,self.byey+500)
    ##캐릭터가 이동할수있는거리 제한 부분
    if(cx+20>600):

        cx-=40
    elif(cx+40<20):
        cx+=40
    elif(cy+500>552):
        cy-=40
    elif(cy+500<45):
        cy+=40

    #####ai 코딩부분
    """
    ai.clip_draw(frame1*32,190,30,49,aix+40,aiy+500)
    if(aicount==0):
        aiy-=20
        frame1=(frame1+1)%4
    elif(aicount==2):
        ai.clip_draw(frame1*32,145,30,49,aix+40,aiy+500)
        aiy+=20
        frame1=(frame1+1)%4

    if((aiy+500>552)or (aiy+500<65)):
        count=random.randrange(0,5)
        if(aiy+500<60):
            aiy=aiy+20
            frame1=(frame1+1)%4


    """
    delay(0.15)
    handle_events()
    update_canvas()
