'''Agent class'''
import vectormath
from vectormath import Vector2
import pygame
import constants


class Agent(object):
    '''Agent'''

    def __init__(self):
        self.position = Vector2(0, 0)
        self.velocity = Vector2(1, 0)
        self.maxvelocity = 10
        self.force = Vector2(0, 0)
        self.heading = Vector2(0, 0)

    def seek(self, target):
        '''seek'''
        distance = self.position.distance(target.position)
        normdistance = distance.normalize()
        scaledis = normdistance.scalarmult(self.maxvelocity)
        return scaledis.sub_vectors(self.velocity)

    def add_force(self):
        '''force'''
        self.position = (self.position.add_vectors(self.velocity))
        self.velocity = (self.velocity.add_vectors(self.force))

    def draw(self, screen):
        '''draw object'''
        points = [(50, 50), (50, 100), (150, 75), (50, 50)]
        pygame.draw.lines(screen, constants.GREEN, False, points, 1)
        pygame.Surface.blit(screen, (0, 0), None, 0)

