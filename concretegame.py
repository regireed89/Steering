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
        pygame.font.init()
        self.font = pygame.font.SysFont('mono', 24, bold=True)

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
            velo = "velocity:{}".format(i.velocity.vec)
            v = self.font.render(velo, True, (255, 255, 255))
            self.screen.blit(v, (0, 0))
            pos = "position:{}".format(i.position.vec)
            p = self.font.render(pos, True, (255, 255, 255))
            self.screen.blit(p, (0, 20))
            head = "heading:{}".format(i.heading.vec)
            h = self.font.render(head, True, (255, 255, 255))
            self.screen.blit(h, (0, 40))
            force = "force:{}".format(i.force.vec)
            f = self.font.render(force, True, (255, 255, 255))
            self.screen.blit(f, (0, 60))

    def run(self):
        '''need documentation'''
        if super(ConcreteGame, self).startup():
            while self.update():
                self.draw()
        super(ConcreteGame, self).shutdown()


if __name__ == '__main__':
    import main as Main
    Main.main()
