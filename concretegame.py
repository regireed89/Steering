'''concrete game'''

from gametemplate import GameTemplate
import agent
import pygame
import constants


class ConcreteGame(GameTemplate):
    '''need documentation'''

    def __init__(self, name):
        '''need documentation'''
        super(ConcreteGame, self).__init__()
        self.screen = pygame.display.set_mode(
            (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        while 1:
            # 5 - clear the screen before drawing it again
            self.screen.fill(0)
            # 6 - draw the screen elements
            self.screen.blit(self.screen, (100, 100))
            # 7 - update the screen
            pygame.display.flip()
            # 8 - loop through the events
            for event in pygame.event.get():
                # check if the event is the X button
                if event.type == pygame.QUIT:
                    # if it is quit the game
                    pygame.quit()
                    exit(0)
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
            pygame.draw.circle(self.screen, constants.GREEN, (400, 300, 10, 10), (100))
            pygame.display.flip()
            pygame.display.update()

    def run(self):
        '''need documentation'''
        if super(ConcreteGame, self).startup():
            while self.update():
                self.draw()
        super(ConcreteGame, self).shutdown()
