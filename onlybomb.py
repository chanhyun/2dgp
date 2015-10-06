from pico2d import*#*는 몽땅다
import os
import random

os.chdir('c://2dgp//image')
open_canvas()
wall=load_image('wall.png')
background=load_image('background.png')
bomb=load_image('bluebub2.jpg')
boom=load_image('boomcenter.bmp')
boomri=load_image('boomright.bmp')
boomle=load_image('boomleft.bmp')
boomdo=load_image('boomdown.bmp')
boomup=load_image('boomup.bmp')
def mathsqrt(bx,by,bx2,by2):
    return math.sqrt((bx2-bx) *(bx2-bx) + (by2-by)*(by2-by))
x=0
y=0
bx=0
by=0
bx2=0
by2=0

count=0
frame1=0
boomcenterframe=0
boomframe=0#폭탄터질때 프레
timer=0
BSIZE=20
boomcount=1#0되면 폭탄터진 프레임도 사라짐
bombcount=1#1은 폭탄이 생기게 하는 변수
bcy=0
while 1:
  
  
  clear_canvas()
  timer+=1
  bx=200
  by=100
  bx2=250
  by2=100
  boomframe=(boomframe+1)%8
  boomcenterframe=(boomcenterframe+1)%3
  bomb.clip_draw(frame1*45,0,47,bcy,bx2,by2)
  if(bombcount==1 and timer==1):
    bcy=50#폭탄 화면에서 없애기 메모리는계속있음..
  #bx=random.randrange(1,10,2)
  #by=random.randrange(0,8,2)
 
  
  
  bomb.clip_draw(frame1*45,0,47,bcy,bx,by)
  frame1=(frame1+1)%4
  
  if(timer==10 and boomcount==1 ):
    bcy=0
    
    timer=0
    boom.clip_draw(boomcenterframe*50,0,40,50,bx,by)#center는 프레임 세개임
    boomup.clip_draw(boomframe*40,0,40,50,bx,by+50)#나머지 상하좌우는 8개임 count=1
    boomdo.clip_draw(boomframe*40,0,40,50,bx,by-50)#count=2
    boomle.clip_draw(boomframe*40,0,40,50,bx-40,by)#count=3
    boomri.clip_draw(boomframe*40,0,40,50,bx+40,by)#count=4
    bombcount=1
    boomcenterframe=(boomcenterframe+1)%3
    boomframe=(boomframe+1)%8
    timer=0

    if(mathsqrt(bx+40,by,bx2-10,by2)<BSIZE):
      boom.clip_draw(boomcenterframe*50,0,40,50,bx2,by2)
      
  update_canvas()
  
  get_events()
  delay(0.1)  
  

  

update_canvas()
   
close_canvas()
