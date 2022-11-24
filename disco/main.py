# disco board
# credits: jonathan dias aka. jonathan.dev
# description: something random i made, im still learning how to use pygame so i can actually make games with

import pygame, sys, random
import instructions
from instructions import *

pygame.init()

SCREENSIZE = (800, 600)
SCREENSIZE169 = (1920, 1080)
SCREEN = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption('disco mode')
CLOCK = pygame.time.Clock()
FPS = 60

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)

BASICCOLOURLIST = [RED, GREEN, BLUE, YELLOW, PURPLE, CYAN]

def drawBoard(TILEWIDTH, TILEHEIGHT, BOARDWIDTH, BOARDHEIGHT, INTERVAL, SPACING, COLOURMODE):
    pygame.time.delay(INTERVAL)
    
    x = 0
    y = 0
    
    for bx in range(BOARDWIDTH):
        if SPACING == True:
            x += TILEWIDTH + round(TILEWIDTH/4)
        else:
            x += TILEWIDTH

        for by in range(BOARDHEIGHT):
            if COLOURMODE == 'basic':
                randcolour = random.randint(0, 5)
                pygame.draw.rect(SCREEN, BASICCOLOURLIST[randcolour], (x, y, TILEWIDTH, TILEHEIGHT))

            if COLOURMODE == 'random':
                pygame.draw.rect(SCREEN, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (x, y, TILEWIDTH, TILEHEIGHT))

            if SPACING == True:
                y += TILEHEIGHT + round(TILEHEIGHT/4)
            else:
                y += TILEHEIGHT
        y = 0
            

tw = 75
th = 75
bw = 5
bh = 5
spacing = True
dl = 500
colourmode = 'basic'
clselect = 1

showinstructions = True


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                if spacing == True:
                    spacing = False
                else:
                    spacing = True

            if event.key == pygame.K_i:
                bw += 1

            if event.key == pygame.K_k:
                bw -= 1

            if event.key == pygame.K_u:
                bh += 1

            if event.key == pygame.K_j:
                bh -= 1

            if event.key == pygame.K_t:
                tw += 5

            if event.key == pygame.K_g:
                if tw >= 25:
                    tw -= 5
                else:
                    continue

            if event.key == pygame.K_y:
                th += 5

            if event.key == pygame.K_h:
                if th >= 25:
                    th -= 5
                else:
                    continue

            if event.key == pygame.K_UP:
                dl += 50
                
            if event.key == pygame.K_DOWN:
                if dl >= 50:
                    dl -= 50
                else:
                    continue
            if event.key == pygame.K_o:
                if showinstructions == False:
                    showinstructions = True
                else:
                    showinstructions = False

            if event.key == pygame.K_v:
                if SCREENSIZE == (800, 600):
                    SCREENSIZE = (1920, 1080)
                    SCREEN = pygame.display.set_mode(SCREENSIZE, pygame.FULLSCREEN)
                else:
                    SCREENSIZE = (800, 600)
                    SCREEN = pygame.display.set_mode(SCREENSIZE)

            if event.key == pygame.K_c:
                if clselect == 1:
                    if colourmode == 'basic':
                        colourmode = 'random'

                else:
                    if colourmode == 'random':
                        colourmode = 'basic'
                        #i plan to add more modes later on so this is an extendable version of a toggle
                    clselect = 0

                clselect += 1

                

    pygame.display.update()
    SCREEN.fill(BLACK)
    drawBoard(tw, th, bw, bh, dl, spacing, colourmode)
    surface11 = FONT.render('Colour mode: ' + colourmode, True, fontcolour)

    if showinstructions == True:
            SCREEN.blit(instructions.surface1, (0, 450))
            SCREEN.blit(instructions.surface2, (0, 470))
            SCREEN.blit(instructions.surface3, (0, 490))
            SCREEN.blit(instructions.surface4, (0, 510))
            SCREEN.blit(instructions.surface5, (0, 530))
            SCREEN.blit(instructions.surface6, (0, 550))
            SCREEN.blit(instructions.surface7, (300, 450))
            SCREEN.blit(instructions.surface8, (300, 470))
            SCREEN.blit(instructions.surface9, (300, 490))
            SCREEN.blit(instructions.surface10, (300, 510))
            SCREEN.blit(surface11, (300, 530))
    CLOCK.tick(FPS)
        