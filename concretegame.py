'''concrete game'''

from gametemplate import GameTemplate
import agent
import pygame
import game


class ConcreteGame(GameTemplate):
    '''need documentation'''

    def __init__(self, name):
        '''need documentation'''
        super(ConcreteGame, self).__init__()
        self.name = name
        self.gameobjects = []
        self.target = agent.Agent()

    def addtobatch(self, gameobject):
        '''add gameobjects to this game'''
        self.gameobjects.append(gameobject)

    def update(self):
        '''update this games logic'''
        if not super(ConcreteGame, self).update():
            return False
        return True

    def draw(self):
        '''draw all gameobjects added to this game'''
        super(ConcreteGame, self).draw()
        for i in self.gameobjects:
            pygame.draw.circle(game.SCREEN, game.BLUE, (game.SCREEN_HEIGHT, game.SCREEN_WIDTH), 3, 0)

    def run(self):
        '''need documentation'''
        if super(ConcreteGame, self).startup():
            while self.update():
                self.draw()
        super(ConcreteGame, self).shutdown()
