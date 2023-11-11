import pygame
import random
pygame.init()
size=width,height=(1000,800)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("RAINY DAY")
rain=[]
particle=[]
count=0
wall=pygame.Rect(0,700,width,height)
die=False
px,py,pw,ph=random.randint(0,int(width-200)),600,70,100
wallr=pygame.Rect(300,200,300,50)
clock=pygame.time.Clock()
x,y=0,-100
xm,ym,w=0,0,0
while not die:
    clock.tick(60)
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            die=True
    key=pygame.key.get_pressed()
    if key[pygame.K_LEFT] and px>=0:
        px-=5
    if key[pygame.K_RIGHT] and px+70<=width:
        px+=5

    
    count+=1
    if count>=3:
        x=random.randint(0,int(width))
        y=random.randint(-500,-100)
        w,h=random.randint(3,7),random.randint(20,30)
        rain.append([x,y,w,h])
        count=0
    pygame.draw.rect(screen,((255,0,0)),(px,py,pw,ph))
    pygame.draw.rect(screen,((0,255,0)),wallr)
    pygame.draw.rect(screen,(0,0,0),wall)
    for i in rain:
        i[1]+=10
        if i[1]>=height:
            rain.pop(rain.index(i))
        pygame.draw.rect(screen,((0,255,255)),i)
    for i in rain:
        #################### RAIN COLLISION ###############
        rainr=pygame.Rect(i[0],i[1],i[2],i[3])
        prect=pygame.Rect(px,py,pw,ph)
        if rainr.colliderect(wall):
            x,y=i[0],i[1]
            xm,ym,w=random.randint(-2,2),random.randint(-3,0),random.randint(3,7)
            for ten in range(100):
                if i in rain:
                    rain.pop(rain.index(i))
        if rainr.colliderect(prect):
            x,y=i[0],i[1]
            xm,ym,w=random.randint(-2,2),random.randint(-3,0),random.randint(3,7)
            for ten in range(100):
                if i in rain:
                    rain.pop(rain.index(i))
        if rainr.colliderect(wallr):
            x,y=i[0],i[1]
            xm,ym,w=random.randint(-2,2),random.randint(-3,0),random.randint(3,7)
            for ten in range(100):
                if i in rain:
                    rain.pop(rain.index(i))
    particle.append([x,y,xm,ym,w])
    for i in particle:
        pygame.draw.circle(screen,((0,255,255)),(i[0],i[1]),i[4])
        i[4]-=0.1
        i[0]+=i[2]*2
        i[1]+=i[3]
        i[3]+=0.1
        if i[1]>=700:
            i[1]=700
        if i[4]<=0:
            particle.pop(particle.index(i))
    pygame.display.update()
pygame.quit()






















