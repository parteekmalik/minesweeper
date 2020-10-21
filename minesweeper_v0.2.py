import pygame
import random
from pygame import *

pygame.init()
pygame.display.set_caption("Minesweeper")
list=[True,True,True,False,True,True,True,False,120 ,False,False,True,2,True]
#     run,bomb, end ,plyer,gm,  mainloop, file, fps,hint ,first
clock = pygame.time.Clock()
size=[]
clicks=[]
list1=[]
bomb=[]
bomb_no1=[]
flag=[]

none=pygame.image.load('mine\\none.jpg')
zero=pygame.image.load('mine\\zero.png')
one=pygame.image.load('mine\\one.png')
two=pygame.image.load('mine\\two.png')
three=pygame.image.load('mine\\three.png')
four=pygame.image.load('mine\\four.png')
five=pygame.image.load('mine\\five.png')
six=pygame.image.load('mine\six.png')
seven=pygame.image.load('mine\seven.png')
eight=pygame.image.load('mine\eight.png')
minered=pygame.image.load('mine\\minered.png')
mine=pygame.image.load('mine\\mine.png')
flag1=pygame.image.load('mine\\flag.png')
dead=pygame.image.load('mine\\dead.png')
happy=pygame.image.load('mine\\happy.PNG')
hope=pygame.image.load('mine\\click.PNG')
pygame.display.set_icon(flag1)
time0=pygame.image.load('time\\0.PNG')
time1=pygame.image.load('time\\1.PNG')
time2=pygame.image.load('time\\2.PNG')
time3=pygame.image.load('time\\3.PNG')
time4=pygame.image.load('time\\4.PNG')
time5=pygame.image.load('time\\5.PNG')
time6=pygame.image.load('time\\6.PNG')
time7=pygame.image.load('time\\7.PNG')
time8=pygame.image.load('time\\8.PNG')
time9=pygame.image.load('time\\9.PNG')



    
def grid():
    for y in range(60,size[1]):
     if y%20==0:
        for x in range(0,size[0]):
            if x%20==0:
                list1.append([x,y])
    #print(list1)
def bomb_and_no():
    i=1
    while size[2]>=i:
        bx=random.randrange(0,size[0],20)
        by=random.randrange(60,size[1],20)
        if [bx,by] in bomb:
                bomb.remove([bx,by])
                i-=1
        bomb.append([bx,by])
        if [bx,by] in fclick:
            bomb.remove([bx,by])
            i-=1
        i+=1
    for x,y in list1:
        i=0
        for a,b in bomb:
            if x==a and y==b:
                i=9
                break
            if x+20==a and y==b:
                i+=1
            if x+20==a and y+20==b:
                i+=1
            if x==a and y+20==b:
                i+=1
            if x+20==a and y-20==b:
                i+=1
            if x==a and y-20==b:
                i+=1
            if x-20==a and y-20==b:
                i+=1
            if x-20==a and y==b:
                i+=1
            if x-20==a and y+20==b:
                i+=1
        bomb_no1.append(i)
def pos(a,b):
            if a%20!=0:
                xx=int(a/20)
                xx=xx*20
            else :
                xx=a
            if b%20!=0: 
                y=int(b/20)
                y=y*20
            else:
                y=b
            return xx,y
def screen(win):
    pygame.draw.rect(win,(192,192,192),(0,0,size[0],60))
    win.blit(happy,(int((size[0]/2)-13),17))
    i=0
    for x,y in list1:
      if y>40 :
          win.blit(none,(x,y))
      for a,b in flag:
          if x==a and b==y:
              win.blit(flag1,(x,y))
      for a,b in clicks:
       if x==a and b==y:
        if bomb_no1[i]==0 and y>40 :
            win.blit(zero,(x,y))
        if bomb_no1[i]==1 and y>40:
            win.blit(one,(x,y))
        if bomb_no1[i]==2 and y>40:
            win.blit(two,(x,y))
        if bomb_no1[i]==3 and y>40:
            win.blit(three,(x,y))
        if bomb_no1[i]==4:
            win.blit(four,(x,y))
        if bomb_no1[i]==5:
            win.blit(five,(x,y))
        if bomb_no1[i]==6:
            win.blit(six,(x,y))
        if bomb_no1[i]==7:
            win.blit(seven,(x,y))
        if bomb_no1[i]==8:
            win.blit(eight,(x,y))
        if bomb_no1[i]==9:
            win.blit(minered,(x,y)) 
      i+=1

###########################################################
def time(b):
    if b<10 and b>=0:
        dis0(0,0,b,7)
    if b>=10 and b<=99:
        c=int(b/10)
        d=b%10
        dis0(0,c,d,7)
    if b>99 and b<1000:
        c=int(b/100)
        if b>109:
            d=int((b%100)/10)
            e=(b%100)%10
        else:
            d=0
            e=b%100
        dis0(c,d,e,7)
    if size[2]-len(flag)>9 :
        dis0(0,int((size[2]-len(flag))/10),(size[2]-len(flag))%10,size[0]-85)
    else:
        dis0(0,0,size[2]-len(flag),size[0]-85)
def dis0(a,b,c,d):
    if a==0:
        win.blit(time0,(d,7))
        dis1(b,c,d)
    elif a==1:
        win.blit(time1,(d,7))
        dis1(b,c,d)
    elif a==2:
        win.blit(time2,(d,7))
        dis1(b,c,d)
    elif a==3:
        win.blit(time3,(d,7))
        dis1(b,c,d)
    elif a==4:
        win.blit(time4,(d,7))
        dis1(b,c,d)
    elif a==5:
        win.blit(time5,(d,7))
        dis1(b,c,d)
    elif a==6:
        win.blit(time6,(d,7))
        dis1(b,c,d)
    elif a==7:
        win.blit(time7,(d,7))
        dis1(b,c,d)
    elif a==8:
        win.blit(time8,(d,7))
        dis1(b,c,d)
    elif a==9:
        win.blit(time9,(d,7))
        dis1(b,c,d)
def dis1(a,c,b):
    if a==0:
        win.blit(time0,(b+26,7))
        di2(c,b)
    elif a==1:
        win.blit(time1,(b+26,7))
        di2(c,b)
    elif a==2:
        win.blit(time2,(b+26,7))
        di2(c,b)
    elif a==3:
        win.blit(time3,(b+26,7))
        di2(c,b)
    elif a==4:
        win.blit(time4,(b+26,7))
        di2(c,b)
    elif a==5:
        win.blit(time5,(b+26,7))
        di2(c,b)
    elif a==6:
        win.blit(time6,(b+26,7))
        di2(c,b)
    elif a==7:
        win.blit(time7,(b+26,7))
        di2(c,b)
    elif a==8:
        win.blit(time8,(b+26,7))
        di2(c,b)
    elif a==9:
        win.blit(time9,(b+26,7))
        di2(c,b)
def di2(a,b):
    if a==0:
        win.blit(time0,(b+52,7))
    elif a==1:
        win.blit(time1,(b+52,7))
    elif a==2:
        win.blit(time2,(b+52,7))
    elif a==3:
        win.blit(time3,(b+52,7))
    elif a==4:
        win.blit(time4,(b+52,7))
    elif a==5:
        win.blit(time5,(b+52,7))
    elif a==6:
        win.blit(time6,(b+52,7))
    elif a==7:
        win.blit(time7,(b+52,7))
    elif a==8:
        win.blit(time8,(b+52,7))
    elif a==9:
        win.blit(time9,(b+52,7))
###############################################################################################################################################    
#fclick=list(dict.fromkeys(fclick))     
def first1():
    pygame.display.update()
    clock.tick(list[8])
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
            list[0] =list[2]=list[4]=list[5]=list[11]= False
            list[6]=True
            clicks.append('fuck off')
      if event.type==pygame.MOUSEBUTTONDOWN:
            xx,y=pos(event.pos[0],event.pos[1])
            if y>40:
                fclick.append([xx,y])
                nebor(xx,y)
                bomb_and_no()
                for a,b in fclick:
                    clicks.append([a,b])
                uncover()
                screen(win)
                list[11]=False
            if event.button==3 and event.pos[0]>int((size[0]/2)-13) and event.pos[1]>17 and event.pos[0]<int((size[0]/2)-13)+26 and event.pos[1]<17+26:
                change()
                list[11]=False


            
fclick=[]
def nebor(xx,y):
            fclick.append([xx+20,y])
            fclick.append([xx,y+20])
            fclick.append([xx+20,y+20])
            fclick.append([xx-20,y])
            fclick.append([xx,y-20])
            fclick.append([xx-20,y-20])
            fclick.append([xx+20,y-20])
            fclick.append([xx-20,y+20])
            fclick1.append([xx,y])
fclick1=[]
def nebors(xx,y):
  if xx+20<size[0] and y+20<size[1] and xx-20>-20 and y-20>40:
    if bomb_no1[list1.index([xx,y])]==0 and [xx,y] not in fclick1:
            nebor(xx,y)
    if bomb_no1[list1.index([xx+20,y])]==0 and [xx+20,y] not in fclick1:
            nebor(xx+20,y)
    if bomb_no1[list1.index([xx,y+20])]==0 and [xx,y+20] not in fclick1:
            nebor(xx,y+20)
    if bomb_no1[list1.index([xx+20,y+20])]==0 and [xx+20,y+20] not in fclick1:
            nebor(xx+20,y+20)
    if bomb_no1[list1.index([xx-20,y])]==0 and [xx-20,y] not in fclick1:
            nebor(xx-20,y)
    if bomb_no1[list1.index([xx,y-20])]==0 and [xx,y-20] not in fclick1:
            nebor(xx,y-20)
    if bomb_no1[list1.index([xx-20,y-20])]==0 and [xx-20,y-20] not in fclick1:
            nebor(xx-20,y-20)
    if bomb_no1[list1.index([xx+20,y-20])]==0 and [xx+20,y-20] not in fclick1:
            nebor(xx+20,y-20)
    if bomb_no1[list1.index([xx-20,y+20])]==0 and [xx-20,y+20] not in fclick1:
            nebor(xx-20,y+20)
  else:
      if y==60 or xx==0 or xx==size[0]-20 or y==size[1]-20:
          if bomb_no1[list1.index([xx,y])]==0 and [xx,y] not in fclick1:
            nebor(xx,y)
def uncover():
    for xx,y in fclick:
      if xx<size[0] and y<size[1] and xx>-20 and y>40:
        if bomb_no1[list1.index([xx,y])]==0:
            nebors(xx,y)
    for a,b in fclick:
                if [a,b] in clicks:
                    clicks.remove([a,b])
                clicks.append([a,b])
                if b<60 or b>size[1]-20 or a<0 or a>size[0]-20:
                    clicks.remove([a,b])
    fclick.clear()
def check(xx,y):
    if y>40:
        if bomb_no1[list1.index([xx,y])] == 0:
            nebor(xx,y)
            uncover()
def change():
                       bomb.clear()
                       flag.clear()
                       clicks.clear()
                       fclick.clear()
                       fclick1.clear()
                       list1.clear()
                       bomb_no1.clear()
                       size.clear()
                       list[11]=True
                       list[0]=list[10]=False
                       list[12]+=1
                       if list[12]>2:
                           list[12]=0
                       if list[12]==0:
                           size.append(220)
                           size.append(240)
                           size.append(15)
                           size.append(99)
                       if list[12]==1:
                           size.append(320)
                           size.append(380)
                           size.append(40)
                           size.append(256)
                       if list[12]==2:
                           size.append(600)
                           size.append(380)
                           size.append(99)
                           size.append(480)
##########################################################
def action(win,down):
      clock.tick(list[8])
      for event in pygame.event.get():
           if event.type == pygame.QUIT:
                  list[0]=list[2]=list[4]=list[5]= False    
           if event.type == pygame.MOUSEBUTTONUP:
            down=False
            l=True
            xx,y=pos(event.pos[0],event.pos[1])
            if  event.button==1:
                   if event.pos[0]>int((size[0]/2)-13) and event.pos[1]>17 and event.pos[0]<int((size[0]/2)-13)+26 and event.pos[1]<17+26:
                      list[2]=list[0]=list[4]=list[1]=list[10]=down=False
                      clicks.clear()
                      bomb.clear()
                      bomb_no1.clear()
                      flag.clear()
                      fclick1.clear()
                      list[11]=True
                   for x,fy in clicks:
                      if x==xx and y==fy:
                          clicks.remove([xx,y])
                      elif fy<60 :
                          clicks.remove([x,fy])
                   clicks.append([xx,y])
                   check(xx,y)
                   if [xx,y] in flag:
                              flag.remove([xx,y])
                              clicks.remove([xx,y])
                              l=False 
                   if l and [xx,y] in bomb:
                          t.append(int(pygame.time.get_ticks()/1000))
                          print('game over')
                          list[0]=list[3]=list[6]=False
            if event.button==3:
                   if event.pos[0]>int((size[0]/2)-13) and event.pos[1]>17 and event.pos[0]<int((size[0]/2)-13)+26 and event.pos[1]<17+26:
                      change()
                   if [xx,y] in flag:
                      flag.remove([xx,y])
                      l=False
                   if l and len(flag)<size[2] and [xx,y] not in clicks:
                      flag.append([xx,y]) 
      win.blit(hope,(int((size[0]/2)-13),17))
      time(int(pygame.time.get_ticks()/1000)-t[0])
      pygame.display.update()
      return down

########################################################################################################################################
t=[]
lt=[]
def t1():
 if len(t)==1:
    t.clear()
 
 t.append(int(pygame.time.get_ticks()/1000))
 if len(t)==3:
     t.pop()
     t.pop()
 
def game(win):
 if list[13]:  
     list[10]=False
     list[11]=True
 if list[10] is False:
    grid()
    list[10]=True
 screen(win)
 while list[11]:
    first1()
    time(0)
 t1()
 while list[0]:
    pygame.display.update()
    clock.tick(list[8])
    down=False
    if list[9]:
        xx,y=pos(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
        if [xx,y] not in clicks and [xx,y] not in flag:
          if [xx,y] in bomb :
            flag.append([xx,y])
          elif [xx,y] not in clicks:
              clicks.append([xx,y])
        list[9]=False
        check(xx,y)
        screen(win)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
            list[0] =list[2]=list[4]=list[5]= False
            list[6]=True
      if event.type==pygame.KEYDOWN and list[9]==False:
        if event.key==104:
          list[9]=True
      if event.type == pygame.MOUSEBUTTONDOWN:
          down=True
          
          while down :
              down=action(win,down)
          screen(win)
      if len(clicks)+len(bomb)==size[3]:
                      list[0]=list[6] =False
                      list[3]=True
                      print('you won')
    
    time(int(pygame.time.get_ticks()/1000)-t[0])
    
####################################################################################################################################################
    
def end():
 while list[2]:
    clock.tick(list[8])
    if list[3]==False:
        win.blit(dead,(int((size[0]/2)-13),17))
    i=0
    for x,y in list1:
     if y>40:
            win.blit(none,(x,y))
     if bomb_no1[i]==9 and list[3]==False:
         win.blit(mine,(x,y))
     for a,b in flag:
          if x==a and b==y:
              win.blit(flag1,(x,y))
     for c,d in clicks:
       if x==c and y==d:
        if bomb_no1[i]==0 and y>40 :
            win.blit(zero,(x,y))
        if bomb_no1[i]==1 and y>40:
            win.blit(one,(x,y))
        if bomb_no1[i]==2 and y>40:
            win.blit(two,(x,y))
        if bomb_no1[i]==3 and y>40:
            win.blit(three,(x,y))
        if bomb_no1[i]==4:
            win.blit(four,(x,y))
        if bomb_no1[i]==5:
            win.blit(five,(x,y))
        if bomb_no1[i]==6:
            win.blit(six,(x,y))
        if bomb_no1[i]==7:
            win.blit(seven,(x,y))
        if bomb_no1[i]==8 :
            win.blit(eight,(x,y))
        if bomb_no1[i]==9:
            win.blit(minered,(x,y))
     i+=1
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN and list[9]==False:
             if event.key==122:
                 del clicks[len(clicks)-1]
                 list[2]=list[13]=False
                 list[0]=list[3]=list[6]=True
                 i=t[0]
                 
                 t.pop(0)
                 
                 t.insert(0,int(pygame.time.get_ticks()/1000)-t[0]+i)
                 
        if event.type == pygame.QUIT:
            list[5]=list[2]=False
        if event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>int((size[0]/2)-13) and event.pos[1]>17 and event.pos[0]<int((size[0]/2)-13)+26 and event.pos[1]<17+26:
         if event.button==1:
          list[0]=list[6]=True
          list[2]=list[4]=list[1]=False
          clicks.clear()
          bomb.clear()
          bomb_no1.clear()
          flag.clear()
          fclick1.clear()
         if event.button==3:
             change()
             list[2]=False
             list[6]=True
#####################################################
size=[600,380,99,480]  
while list[5]:
    if  list[0]==False and list[6]==True:
        list[0]=True
    elif list[0]:
        win = pygame.display.set_mode((size[0],size[1]))
        game(win)
        if list[6]==False:
            list[2]=True
            end()
pygame.quit()
















