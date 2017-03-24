'''gametemplate.py'''

# from gameobject import GameObject
import pygame
from constants import *


class GameTemplate(object):
    '''pygame object'''

    def __init__(self):
        '''abc'''
        pygame.init()
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
