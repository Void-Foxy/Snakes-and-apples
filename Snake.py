#########################################
# File Name: Snake.py
# Description: play a game of snake
# Author: ICS2O
# Date: 02/11/2018
#########################################
from random import randint
import pygame
pygame.init()
WIDTH = 800
HEIGHT= 600
gameWindow=pygame.display.set_mode((WIDTH,HEIGHT))

TOP = 0
BOTTOM = HEIGHT-100
MIDDLE = int(WIDTH/2.0)
WHITE = (255,255,255)
BLACK = (  0,  0,  0)
GREY = (200,200,200)
RED = (255, 0, 0)
GREEN = ( 0, 0,255,)
outline=0

font = pygame.font.Font("Kiona-Regular.ttf",20)


#---------------------------------------#
# functions                             #
#---------------------------------------#
def redrawGameWindow():
    gameWindow.fill(BLACK)
    pygame.draw.rect(gameWindow, WHITE, (SEGMENT_R,SEGMENT_R,WIDTH - 2*SEGMENT_R,HEIGHT - 2*SEGMENT_R),0)
    pygame.draw.rect(gameWindow, BLACK, (SEGMENT_R*2,SEGMENT_R*2,WIDTH - 4*SEGMENT_R,HEIGHT - 4*SEGMENT_R),0)
    pygame.draw.rect(gameWindow, WHITE, (segX[0],segY[0],SEGMENT_R*2,SEGMENT_R*2),outline)
    for i in range(1,len(segX)): 
        pygame.draw.rect(gameWindow, GREY, (segX[i],segY[i],SEGMENT_R*2,SEGMENT_R*2),outline)
    pygame.draw.rect(gameWindow, RED, (appleX,appleY,SEGMENT_R*2,SEGMENT_R*2),outline)
    gameWindow.blit(inGameScore,(3*SEGMENT_R,3*SEGMENT_R))
    pygame.display.update() 

#---------------------------------------#
# main program                          #
#---------------------------------------#
print "Use the arrows and the space bar."
print "Hit ESC to end the program."

# snake's properties
SEGMENT_R = 10
HSTEP = 20
VSTEP = 20
stepX = 0
stepY = -VSTEP                          # initially the snake moves upwards
segX = []
segY = []
segmentCLR=[]
for i in range(4):                      # add coordinates for the head and 3 segments
    if i == 0:
        segmentCLR.append(WHITE)
    else:
        segmentCLR.append(GREY)
    segX.append(MIDDLE)
    segY.append(BOTTOM + i*VSTEP)
temp=randint(1,WIDTH/(2*SEGMENT_R)-2)
appleX=2*SEGMENT_R*temp
temp=randint(1,HEIGHT/(2*SEGMENT_R)-2)
appleY=2*SEGMENT_R*temp

appleEat= False

score=0

velocity=60

notRight = True
notLeft = True
notUp = False
notDown = True
#---------------------------------------#
inPlay = True
while inPlay:
    snakeKill=False
    inGameScore=font.render("Score " + str(score),1,WHITE)
    redrawGameWindow()
    pygame.time.delay(velocity)

    pygame.event.clear()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        inPlay = False
    if keys[pygame.K_LEFT] and notRight:
        stepX = -HSTEP
        stepY = 0
        notRight = True
        notLeft = False
        notUp = True
        notDown = True
    elif keys[pygame.K_RIGHT] and notLeft:
        stepX = HSTEP
        stepY = 0
        notRight = False
        notLeft = True
        notUp = True
        notDown = True
    elif keys[pygame.K_UP] and notDown:
        stepX = 0
        stepY = -VSTEP
        notRight = True
        notLeft = True
        notUp = False
        notDown = True
    elif keys[pygame.K_DOWN] and notUp:
        stepX = 0
        stepY = VSTEP
        notRight = True
        notLeft = True
        notUp = True
        notDown = False

#if the apples is consumed

    if segX[0]==appleX and segY[0]==appleY:
        appleEat=True
    if appleEat:            # if space bar is pressed, add a segment:
        segX.append(segX[-1])           # assign it the same x and y coordinates
        segY.append(segY[-1])           # as those of the last segment
        segmentCLR.append(GREY)
        appleEat=False
        temp=randint(1,WIDTH/(2*SEGMENT_R)-2)
        appleX=2*SEGMENT_R*temp
        temp=randint(1,HEIGHT/(2*SEGMENT_R)-2)
        appleY=2*SEGMENT_R*temp
        score=score+1
        if velocity>=1:
            velocity=velocity-1
# move the segments
    lastIndex = len(segX)-1
    for i in range(lastIndex,0,-1):     # starting from the tail, and going backwards:
        segX[i]=segX[i-1]               # every segment takes the coordinates
        segY[i]=segY[i-1]               # of the previous one
# move the head
    segX[0] = segX[0] + stepX
    segY[0] = segY[0] + stepY
#Testing for death
    for x in range(len(segX)):
        if segX[x] <= 0 or segX[x] >= 800- 2*SEGMENT_R:
            inPlay = False
    for y in range(len(segY)):
        if segY[y] <= 0 or segY[y] >= 600- 2*SEGMENT_R:
            inPlay = False
    for x in range(1,len(segX)):
        if segX[0] == segX[x] and segY[0] == segY[x]:
            snakeKill = True
    if snakeKill:
        inPlay = False
#---------------------------------------#    
pygame.quit()
print "your score is:",score
