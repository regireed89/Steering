'''gametemplate.py'''

# from gameobject import GameObject
import pygame
import constants


class GameTemplate(object):
    '''pygame object'''

    def __init__(self):
        '''abc'''
        pygame.init()    

    def startup(self):
        '''do startup routines'''
        return True

    def update(self):
        '''input and time'''
        
        return True

    def draw(self):
        pygame.display.flip()
        '''base draw'''

    def shutdown(self):
        '''shutdown the game properly'''
