'''gametemplate.py'''

# from gameobject import GameObject
import pygame
from constants import *


class GameTemplate(object):
    '''pygame object'''

    def __init__(self):
        '''abc'''
        pygame.init()
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        BLUE = (0, 0, 255)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)
        PAD = (5, 5)
        ROWS = 10
        COLS = 10
        WIDTH = 50
        HEIGHT = 50
        SCREEN_WIDTH = COLS * (PAD[0] + WIDTH) + PAD[1]
        SCREEN_HEIGHT = ROWS * (PAD[0] + HEIGHT) + PAD[1]
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def startup(self):
        '''do startup routines'''


    def update(self):
        '''input and time'''
        return True

    def draw(self):
        '''base draw'''

    def shutdown(self):
        '''shutdown the game properly'''
