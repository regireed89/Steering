'''game'''
import pygame
from gametemplate import GameTemplate


class AstarGame(GameTemplate):
    '''a*'''

    def __init__(self):
        '''init'''
        super(AstarGame, self).__init__()
        gameobjects = []
