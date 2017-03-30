'''gametemplate.py'''

# from gameobject import GameObject
import pygame
import constants


class GameTemplate(object):
    '''pygame object'''

    def __init__(self):
        '''abc'''
        pygame.init()
        self.surface = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    def startup(self):
        '''do startup routines'''
        return True

    def update(self):
        '''input and time'''
        #pygame.time.Clock.tick(0)

        return True

    def draw(self):
        '''base draw'''
        pygame.display.flip()

    def shutdown(self):
        '''shutdown the game properly'''
