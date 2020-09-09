import pygame
import random
from pygame import *

pygame.init()
pygame.display.set_caption("Minesweeper")
list=[True,True,True,False,True,True,True,False,30 ,False]
#     run,bomb,close,plyer,gm,  mainloop, file, fps,hint
clock = pygame.time.Clock()
size=[]
clicks=[]
list1=[]
bomb=[]
#bomb=[[40,60],[40,80],[40,100],[40,120],[40,140],[40,160],[60,160],[80,160],[100,160],[120,160],[140,160],[160,160],[160,140],[160,120],[160,100],[160,80],[160,60],[60,60],[80,60],[100,60],[120,60],[140,60]]
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
        #print(bomb)
     
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
    win.blit(happy,(int((size[0]/2)-3),17))
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
#fclick=list(dict.fromkeys(fclick))     
def first1():
    pygame.display.update()
    clock.tick(list[8])
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
            list[0] =list[2]=list[4]=list[5]= False
            list[6]=True
      if event.type==pygame.MOUSEBUTTONDOWN:
            xx,y=pos(event.pos[0],event.pos[1])
            fclick.append([xx,y])
            nebor(xx,y)
            bomb_and_no()
            for a,b in fclick:
                clicks.append([a,b])
            uncover()
            screen(win)


            
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
                   for x,fy in clicks:
                      if x==xx and y==fy:
                          clicks.remove([xx,y])
                      if fy<60 :
                          clicks.remove([xx,fy])
                   clicks.append([xx,y])
                   check(xx,y)

                   if [xx,y] in flag:
                          
                              flag.remove([xx,y])
                              clicks.remove([xx,y])
                              l=False 
                   if l and [xx,y] in bomb:
                    
                      
                          print('game over')
                          list[0]=list[3]=list[6]=False
            if event.button==3:
                   if [xx,y] in flag:
                    
                      flag.remove([xx,y])
                      l=False
                   if l:
                      flag.append([xx,y])
            screen(win)     
      return down



def game(win):
 
 
 #for a,b in bomb:
 #       flag.append([a,b])
 screen(win)
 while len(clicks)==0:
    first1()
 
 while list[0]:
    
    pygame.display.update()
    clock.tick(list[8])
    
    down=False
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
            list[0] =list[2]=list[4]=list[5]= False
            list[6]=True
      #print(event)
      if event.type==pygame.KEYDOWN and list[9]==False:
        if event.key==104:
          #print("yes")
          list[9]=True
      if event.type == pygame.MOUSEBUTTONDOWN:
          down=True
          if event.pos[0]>int((size[0]/2)-3) and event.pos[1]>17 and event.pos[0]<int((size[0]/2)-3)+26 and event.pos[1]<17+26:
              list[2]=list[0]=list[4]=list[1]=down=False
              clicks.clear()
              bomb.clear()
              bomb_no1.clear()
              flag.clear()
              fclick1.clear()
          win.blit(hope,(int((size[0]/2)-3),17))
          
          pygame.display.update()
          while down :
              down=action(win,down)
      if len(clicks)+len(bomb)==size[3]:
                      list[0]=list[6] =False
                      list[3]=True
                      print('you won')
    
    
    
    if list[9]:
        xx,y=pos(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
        if [xx,y] not in clicks:
            
          if [xx,y] in bomb :
            flag.append([xx,y])
          elif [xx,y] not in clicks:
              clicks.append([xx,y])
        list[9]=False
        check(xx,y)
        #print(xx,y)
        screen(win)
def end():
 while list[2]:
    
    clock.tick(list[8])
    if list[3]==False:
        win.blit(dead,(int((size[0]/2)-3),17))
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
         if event.type == pygame.QUIT:
            list[5]=list[2]=False
         if event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>int((size[0]/2)-3) and event.pos[1]>17 and event.pos[0]<int((size[0]/2)-3)+26 and event.pos[1]<17+26:
          list[0]=list[6]=True
          list[2]=list[4]=list[1]=False
          
          clicks.clear()
          
          bomb.clear()
          bomb_no1.clear()
          flag.clear()
          fclick1.clear()
def start():
    n=int(input("Select Your Difficulty:\n1.Easy(9X9)\n2.Medium(16X16)\n3.Hard(30X16)\n4.Custom\n"))
    if n==1:
                  size.append(180)
                  size.append(240)
                  size.append(10)
                  size.append(81)
                  
    if n==2:
                  size.append(320)
                  size.append(380)
                  size.append(40)
                  size.append(256)
    if n==3:
                  size.append(600)
                  size.append(360)
                  size.append(99)
                  size.append(480)
    if n==4:
        while list[4]:
          a=int(input("Enter rows\n"))
          b=int(input("Enter coloums\n"))+3
          if a<6 and b<11:
            print("Game should be greater or equal to 6X8")
          else:
            size.append(a*20)
            size.append(b*20)
            list[4]=False
        while list[1]:
            size.append(int(input("Enter bomb\n")))
            print(size)
            if size[2]<a*b:
                list[1]=False
            else:
                size.pop(2)
        size.append(int(a*(b-3)))
        
    
start()
grid()
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
















