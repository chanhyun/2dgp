from pico2d import*#*는 몽땅다
from math import*
import os
os.chdir('c://2dgp//image')
open_canvas()
wall=load_image('wall.png')
background=load_image('background.png')
bomb=load_image('bluebub2.jpg')
chdo=load_image('downp.png')
chri=load_image('rightp.png')
chle=load_image('leftp.png')
chup=load_image('upp.png')
ch=load_image('downp.png')
star=load_image('star.png')
starchdo=load_image('itemdown.png')
starchle=load_image('itemleft.png')
starchri=load_image('itemright.png')
starchup=load_image('itemup.png')
#starch
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
    global timer
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
               
                count=5
                blx,bly=cx+20,cy+500
                wall.draw(blx,bly)
            elif event.key == SDLK_2:
                stcount=True
                starnocount=1
                sx=-40
                sy=-27
                
        if event.type==SDL_KEYUP:
            if event.key==SDLK_RIGHT:
                #blockcheck=False
                run=False
            elif event.key==SDLK_LEFT:
                run2=False
            elif event.key==SDLK_UP:
                run3=False
            elif event.key==SDLK_DOWN:
                run4=False
            
               
                
                

          
run=False
run2=False
run3=False
run4=False
running=True
count=0
frame=0#애니메이션프레임
frame1=0
timer=0#시간
cx,cy=0,0#캐릭터좌표
mx,my=400,300#맵좌표
sx,sy=0,0
blockcheck=False
stcount=False
box=90
BSIZE=20

blx,bly=cx+20,cy+500

while(running):
    clear_canvas()
    mathdistance=math.sqrt(((cx+20)-blx) *((cx+20)-blx) + ((cy+500)-bly)*((cy+500)-bly))
    
    
    background.draw(mx,my)
    wall.draw(mx,my)
    
    chdo.clip_draw(0,0,42,60,cx+20,cy+500)
       
    star.clip_draw(9,10,sx+40,sy+27,262,15)
    ##폭탄부분
    bomb.clip_draw(frame1*45,0,48,49,box,90)
    frame1=(frame1+1)%4
    ##아이템사용부분
    if(stcount==True):
        starchdo.clip_draw(frame*44,0,42,60,cx+20,cy+500)
        frame=(frame+1)%8
        timer+=1#아이템사용시간 증가
    if(timer==50 and starnocount==1):#별을쓰고난후의 아이템지속시간은 50초?
        stcount=False
        
        timer=0
        
    #star.clip_draw(10,10,0,0,100,200)
    
    ##벽설치부분및 벽과의충돌체크
    if(blockcheck):
        wall.draw(blx,bly)
        
        if(mathdistance<BSIZE):
            cx-=20
            cy-=20
           
        
    
    ##여기는 캐릭터의 방향전환 부분
    if(count==1 and run):
        cx=cx+20
        
        chri.clip_draw(frame*44,0,42,60,cx+20,cy+500)
        frame=(frame+1)%8
        
    elif(count==2 and run2):
        cx=cx-20
        chle.clip_draw(frame*44,0,42,60,cx+20,cy+500)
        frame=(frame+1)%8
    elif(count==3 and run3):
        cy=cy+20
        chup.clip_draw(frame*44,0,42,60,cx+20,cy+500)
        frame=(frame+1)%8
    elif(count==4 and run4) :
        cy=cy-20
        chdo.clip_draw(frame*44,0,42,60,cx+20,cy+500)
        frame=(frame+1)%8
    ##캐릭터 아이템쓰고(무적)난 후의 방향전환코딩부분
    
    if (stcount==True and run and count==1):
        starchri.clip_draw(frame*44,0,42,60,cx+20,cy+500)
        frame=(frame+1)%8
    elif (stcount==True and run2 and count==2):
        starchle.clip_draw(frame*44,0,42,60,cx+20,cy+500)
        frame=(frame+1)%8
    elif (stcount==True and run3 and count==3):
        starchup.clip_draw(frame*44,0,42,60,cx+20,cy+500)
        frame=(frame+1)%8
    elif (stcount==True and run4 and count==4):
        starchdo.clip_draw(frame*44,0,42,60,cx+20,cy+500)
        frame=(frame+1)%8
        
        
    
    
        
    ##캐릭터가 이동할수있는거리 제한 부분
    if(cx+20>600):
    
        cx-=20
    elif(cx+40<60):
        cx+=20
    elif(cy+500>552):
        cy-=20
    elif(cy+500<65):
        cy+=20        
    delay(0.1)
    
   
    handle_events()
    update_canvas()
    
    #bx+=0
    
   
    #for x in range(1,6):
        #for y in range(1,5):
            #wall.draw(x*75,y*75)
           
         
    
             
            
       
    

       
    
    #close_canvas()
