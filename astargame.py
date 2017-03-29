'''game'''
import pygame
from gametemplate import GameTemplate
import agent


class AstarGame(GameTemplate):
    '''a*'''

    def __init__(self):
        '''init'''
        super(AstarGame, self).__init__()
        self.gameobjects = []
        self.target = agent.Agent()

    def addtobatch(self, obj):
        '''add'''
        self.gameobjects.append(obj)

    def update(self):
        '''update this games logic'''
        if not super(AstarGame, self).update():
            return False
        return True

    def draw(self):
        '''draw all gameobjects added to this game'''
        super(AstarGame, self).draw()
        for i in self.gameobjects:
            pygame.draw.circle(game.SCREEN, game.BLUE, (game.SCREEN_HEIGHT, game.SCREEN_WIDTH), 3, 0)

    def run(self):
        '''need documentation'''
        if super(AstarGame, self).startup():
            while self.update():
                self.draw()
        super(AstarGame, self).shutdown()
