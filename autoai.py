from pico2d import*#*는 몽땅다
from math import*
import random 
import os
os.chdir('c://2dgp//image')
open_canvas()
ai=load_image('ai.bmp')
wall=load_image('wall.png')
aix=0
aiy=0
frame=0
ran=0
count=3
i=0
timer=0
wx=500
wy=500

BSIZE=20
def mathsqrt(cx,cy,wx,wy):
    return math.sqrt(((cx+20)-wx) *((cx+20)-wx) + ((cy+500)-wy)*((cy+500)-wy))
while 1:
    clear_canvas()
    #timer+=1
    frame=(frame+1)%4
    ai.clip_draw(frame*32,190,30,49,aix+20,aiy+500)
    frame=(frame+1)%4
    wall.draw(wx,wy)
    if(count==3):#오른쪽
        ai.clip_draw(frame*32,48,30,49,aix+20,aiy+500)
        aix+=20
    elif(count==4):#왼쪽
        ai.clip_draw(frame*32,93,30,49,aix+20,aiy+500)
        aix-=20
    if(aiy+500>552):
        count=random.randrange(0,5)
    if(mathsqrt(aix+25,aiy,wx,wy)<BSIZE+15):
         count=4
    elif(mathsqrt(aix-25,aiy,wx,wy)<BSIZE+15):
         count=3
    
    delay(0.2)
    update_canvas()
    get_events()
    #for i in range(0,5):
    
"""
    if(count==0):#아래
        aiy-=20
        frame=(frame+1)%4
    elif(count==2):#위간
        ai.clip_draw(frame*32,145,30,49,aix+20,aiy+500)
        frame=(frame+1)%4
        aiy+=20
"""
   
"""   
    if(mathsqrt(aix,aiy-25,wx,wy)<BSIZE+15):
        count=2
    elif(mathsqrt(aix,aiy+25,wx,wy)<BSIZE+15):
        count=0
"""
     
        
            
        
    
   
   
        
        #aix=random.randrange(0,10,2)
        #aiy=random.randrange(0,20,2)
        
    
    
        
        
    


