'''concrete game'''

from gametemplate import GameTemplate
import agent
import pygame
import constants
import vectormath


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
        self.target.position = vectormath.Vector2(pygame.mouse.get_pos())
        for event in self._events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    for i in self.gameobjects:
                        i.targetagent = self.target
                        i.Wander = False
                        i.Flee = False
                        i.Seek = True
                        print "agent at (%d, %d)" % i.position.vec
                if event.key == pygame.K_f:
                    for i in self.gameobjects:
                        i.targetagent = self.target
                        i.Wander = False
                        i.Seek = False
                        i.Flee = True
                        print "agent at (%d, %d)" % i.position.vec
                if event.key == pygame.K_w:
                    for i in self.gameobjects:
                        i.Seek = False
                        i.Flee = False
                        i.Wander = True
                        print "agent at (%d, %d)" % i.position.vec
            if event.type == pygame.MOUSEMOTION:
                print "mouse at (%d, %d)" % event.pos
        for i in self.gameobjects:
            i.update(self.deltatime)
        print self.deltatime
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


if __name__ == '__main__':
    import main as Main
    Main.main()
