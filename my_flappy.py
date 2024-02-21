import pygame, random, time
from pygame.locals import *

#VARIABLES
SCREEN_WIDHT = 400
SCREEN_HEIGHT = 600
SPEED = 20
GRAVITY = 2.5
GAME_SPEED = 15

GROUND_WIDHT = 2 * SCREEN_WIDHT
GROUND_HEIGHT= 100

PIPE_WIDHT = 80
PIPE_HEIGHT = 500

PIPE_GAP = 150

wing = 'assets/audio/wing.wav'
hit = 'assets/audio/hit.wav'
pygame.mixer.init()

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images =  [pygame.image.load('assets/sprites/bluebird-upflap.png').convert_alpha(),
                        pygame.image.load('assets/sprites/bluebird-midflap.png').convert_alpha(),
                        pygame.image.load('assets/sprites/bluebird-downflap.png').convert_alpha()]
        
        self.speed = SPEED #speed_y car speed_x constant
        self.current_image = 0
        self.image = pygame.image.load('assets/sprites/bluebird-upflap.png').convert_alpha()

        self.rect = self.image.get_rect()
        #self.rect[0] = SCREEN_WIDHT / 6 # Pourquoi ?
        #self.rect[1] = SCREEN_HEIGHT / 2


    def update(self): #update for next image
        self.current_image = (self.current_image + 1) % 3 
        self.image = self.images[self.current_image]
        self.speed += GRAVITY
        #UPDATE HEIGHT
        self.rect[1] += self.speed

    def bump(self): #press K-SPACE
        self.speed = -SPEED
    
    def begin(self):       # Why not update() ?
        self.current_image = (self.current_image + 1) % 3 
        self.image = self.images[self.current_image]


class Pipe(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('assets/sprites/pipe-green.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(PIPE_WIDHT,PIPE_HEIGHT))









pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird')
bird = pygame.image.load('assets/sprites/bluebird-downflap.png')

BACKGROUND = pygame.image.load('assets/sprites/background-day.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDHT, SCREEN_HEIGHT))
BEGIN_IMAGE = pygame.image.load('assets/sprites/message.png').convert_alpha()

while 1 :
    screen.fill("black")
    screen.blit(BACKGROUND,(0,0))
    #screen.blit(BEGIN_IMAGE, (120, 150))
    pygame.display.flip()