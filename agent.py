'''Agent class'''
import vectormath
from vectormath import Vector2
import pygame
import constants
if __name__ == '__main__':
    import main as Main
    Main.main()

class Agent(object):
    '''Agent'''

    def __init__(self):
        self.position = Vector2(0, 0)
        self.velocity = Vector2(10, 0)
        self.maxvelocity = 10
        self.force = Vector2(10, 0)
        self.heading = Vector2(0, 0)
        self.surface = pygame.Surface((75, 50), pygame.SRCALPHA)
        points = [(0, 0), (75, 25), (0, 50), (0, 0)]
        pygame.draw.lines(self.surface, constants.RED, False, points, 1)

    def seek(self, target):
        '''seek'''
        distance = self.position.distance(target.position)
        normdistance = distance.normalize()
        scaledis = normdistance.scalarmult(self.maxvelocity)
        return scaledis.sub_vectors(self.velocity)

    def add_force(self):
        '''force'''

    def draw(self, screen):
        '''draw object'''
        screen.blit(self.surface, self.position.vec, None, 0)

