import runWorld as rw
import drawWorld as dw
import pygame as pg
import pygame, sys
from pygame.locals import *
from random import randint
from numpy import absolute


################################################################


################################################################

# Initialize world
name = "Hoo will win? Press the mouse (but not too fast)!"
width = 1000
height = 1000

pygame.init()

pygame.display.set_caption('font example')
size = [640, 480]
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

basicfont = pygame.font.SysFont(None, 48)
#text
text = basicfont.render('Hello World!', True, (255, 0, 0), (255, 255, 255))
textrect = text.get_rect()
textrect.centerx = screen.get_rect().centerx
textrect.centery = screen.get_rect().centery
screen.fill((255, 255, 255))
screen.blit(text, textrect)

pygame.display.update()



rw.newDisplay(width, height, name)

################################################################

# Display the state by drawing a cat at that x coordinate
myimage = dw.loadImage("cavman.jpg")
myimage1 = dw.loadImage("hokie.gif")

# state -> image (IO)
# draw the cat halfway up the screen (height/2) and at the x
# coordinate given by the first component of the state tuple


def updateDisplay(state):
    dw.fill(dw.blue)
    dw.draw(myimage, (state[0], state[2]))
    dw.draw(myimage1, (state[4], state[6]))


################################################################

# state -> state


def updateState(state):
    return((state[0] + state[1], state[1], state[2] + state[3], state[3], state[4] + state[5], state[5], state[5] + state[6]))

################################################################


def updateBound(state):
    if (state[0] and state[4] >= 1000):
        return True
    else:
        return False

####################################################################
# Terminate the simulation when the 2 images touch


def endState(state):

    if(absolute(state[0] - state[4]) < 150 + 93 and
       absolute(state[2] - state[6]) < 150 + 115):
        return True
    else:
        return False



################################################################

#handle each event by printing it on the console and by then responding to the event
def handleEvent(state, event):
    if (event.type == pg.MOUSEBUTTONDOWN):
        return((state[0], randint(-5, 5), state[2], randint(-5, 5), state[4], randint(-5, 5), state[6], randint(-5, 5)))
    else:

        return(state)

################################################################


#############################################################################


# World state will be single x coordinate at left edge of world

# The cat starts at the left, moving right
initState =(randint(0, 499), randint(1, 5), 100, randint(1, 5), 500, randint (1, 5), height/2, randint(1, 5))



# Run the simulation no faster than 60 frames per second
frameRate = 10

# Run the simulation!
rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)
