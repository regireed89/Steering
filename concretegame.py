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
        self.deltatime = 0
        self.fps = 30
        milliseconds = self.clock.tick(self._fps)
        self._deltatime = milliseconds / 1000.0
        self.target = agent.Agent()
        

    def addtobatch(self, gameobject):
        '''add gameobjects to this game'''
        self.gameobjects.append(gameobject)

    def update(self):
        '''update this games logic'''
        milliseconds = self.clock.tick(self._fps)
        self._deltatime = milliseconds / 1000.0
        if not super(ConcreteGame, self).update():
            return False
        self.target.position = vectormath.Vector2(pygame.mouse.get_pos())
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    for i in self.gameobjects:
                        i.targetagent = self.target
                        i.Seek = True
                        i.update(self.deltatime)
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
