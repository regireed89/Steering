'''concrete game'''

from gametemplate import GameTemplate
import agent
import pygame
import constants
import vectormath
if __name__ == '__main__':
    import main as Main
    Main.main()


class ConcreteGame(GameTemplate):
    '''need documentation'''

    def __init__(self, name):
        '''need documentation'''
        super(ConcreteGame, self).__init__()
        self.name = name
        self.gameobjects = []
        self.target = agent.Agent()
        self.target.position = 

    def addtobatch(self, gameobject):
        '''add gameobjects to this game'''
        self.gameobjects.append(gameobject)

    def update(self):
        '''update this games logic'''
        self.clock.tick(60)
        if not super(ConcreteGame, self).update():
            return False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        for event in pygame.event.get():
            if event.type == pygame.K_s:
                for i in self.gameobjects:
                    i.seek(self.target)
                    i.draw(self.screen)
        return True

    def draw(self):
        '''draw all gameobjects added to this game'''
        super(ConcreteGame, self).draw()
        for i in self.gameobjects:
            i.draw(self.screen)

    def run(self):
        '''need documentation'''
        if super(ConcreteGame, self).startup():
            while self.update():
                self.draw()
        super(ConcreteGame, self).shutdown()
