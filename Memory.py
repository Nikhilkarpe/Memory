import pygame
import sys
from pygame.locals import *
import random

#start pygame
pygame.init()

RED=(255,0,0)
BLUE=(0,50,35)
GREEN=(0,255,0)
WHITE=(128,0,0)
BLACK=(255,255,0)
DARKGREEN=(0,45,0)
MAROON=(212,175,55)
PURPLE=(191,45,255)
YELLOW=(255,255,0)
CYAN=(255,255,255)

WINDOWWIDTH = 1280
WINDOWHEIGHT = 250
BOXHEIGHT = WINDOWHEIGHT-50
BOXWIDTH = WINDOWWIDTH/16
UPPERGAPSIZE = 5

dispwindow = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
pygame.display.set_caption('MEMORY GAME')
dispwindow.fill(MAROON)
#GAME LOGIC
from random import shuffle
deck = range(0,8) + range(0,8)
exposed = [0]*16
cards = [0,0]
score = 0
turns = 0
state = 0
matchCards = []

def newGame():
    #EVETHING RESTARTS FROM ZERO
    global exposed, deck, cards, score, turns, state,matchCards
    shuffle(deck)
    print deck
    score = 0
    turns = 0
    state = 0
    exposed = [0]*16
    cards = [0,0]
    matchCards = []
def makeText(text,center,colour,bgcolour=PURPLE ):
    fontObj= pygame.font.Font('freesansbold.ttf',32)
    textSurfaceObj = fontObj.render(text,True,colour,bgcolour)
    textRectObj=textSurfaceObj.get_rect()
    textRectObj.center=center
    return (textSurfaceObj,textRectObj)


def draw():
    global exposed, deck

    for i in range(0,len(exposed)):
        rect=pygame.Rect(i* BOXWIDTH + 5, UPPERGAPSIZE, BOXWIDTH- 2* UPPERGAPSIZE, BOXHEIGHT-2*UPPERGAPSIZE)
        if exposed[i]==0:#draw card
            pygame.draw.rect(dispwindow,BLACK,rect)
        else:#write text
            pygame.draw.rect(dispwindow,WHITE,rect)
            Temptext= makeText(str(deck[i]),rect.center,CYAN,bgcolour=WHITE)
            dispwindow.blit(Temptext[0],Temptext[1])

def mouseclick (x,y):
    global exposed, deck, cards, score, turns, state, matchCards
    pos = x//80     #ans wiil be in int
    if 5<int(y)< 200 and (pos*80+5< int (x)<(pos+1)*80-5):
        if state == 0:
            state =1
            exposed[pos] = 1
            cards[0] =pos

        elif state == 1:
            cards[1] =pos
            if cards[1]!=cards[0]:
                state = 2
                exposed[pos]  = 1
                if deck[cards[0]]==deck[cards[1]]:
                    if deck[cards[0]] not in matchCards:
                        matchCards = matchCards + [deck[cards[0]]]
                        score = score + 1
                        turns = turns + 1
                if deck[cards[0]] not in matchCards:
                    turns = turns +1

        elif state == 2:
            if cards[1]!=cards[0] :
                state = 1
                if deck[cards[0]]!=deck[cards[1]]:
                    exposed[cards[0]]=0
                    exposed[cards[1]] =0
                exposed[pos]  = 1
                cards[0] =pos

def scoreandturns():
    global score,turns
    a= 'SCORE=%d  TURNS=%d'%(score, turns)
    b= (640,225)
    Temptext=makeText(a,b,WHITE,bgcolour=MAROON)
    dispwindow.blit(Temptext[0],Temptext[1])

def YouWin():
    if exposed == [1]*16:
        a="YOU WIN!!! PRESS R TO RESTART OR ESC TO QUIT"
        b= (640,125)
        Temptext=makeText(a,b,WHITE,bgcolour=MAROON)
        dispwindow.fill(MAROON)
        dispwindow.blit(Temptext[0],Temptext[1])
#
# def z():
#     if

scoreandturns()
newGame()

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.key == pygame.K_r:
                dispwindow.fill(MAROON)
                newGame()

        elif event.type == MOUSEBUTTONUP:
            mousex,mousey= event.pos
            mouseclick(mousex,mousey)
    draw()
    scoreandturns()
    YouWin()
    pygame.display.update()
