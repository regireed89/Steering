'''Agent class'''
import vectormath
from vectormath import Vector2
import pygame
import constants
import random
import math

class Agent(object):
    '''Agent'''

    def __init__(self):
        self.position = Vector2((0, 0))
        self.velocity = Vector2((1, 0))
        self.maxvelocity = 10
        self.mass = 5
        self.force = Vector2((0, 0))
        self.heading = Vector2((0, 0))
        self.direction = Vector2((0, 0))
        self.acceleration = Vector2((0, 0))
        self.surface = pygame.Surface((75, 50), pygame.SRCALPHA)
        self.surface.fill((0, 0, 0))
        points = [(0, 0), (75, 25), (0, 50), (0, 0)]
        pygame.draw.lines(self.surface, constants.RED, False, points, 1)
        self.Seek = False
        self.Flee = False
        self.Wander = False
        self.targetagent = None
        # radius = 1
        # distance = 1

    def seek(self, target):
        '''seek'''
        distance = target.position.distance(self.position)
        normdistance = distance.normalize()
        scaledis = normdistance.scalarmult(self.maxvelocity)
        self.force = scaledis.sub_vectors(self.velocity)
        return self.force

    def flee(self, target):
        '''flee'''
        distance = self.position.distance(target.position)
        normdistance = distance.normalize()
        scaledis = normdistance.scalarmult(self.maxvelocity)
        self.force = scaledis.sub_vectors(self.velocity)
        return self.force

    # def wander(self, distance, radius):
    #     '''wander'''
    #     center_circle = self.velocity.normalize()
    #     center_circle = center_circle.scalarmult(distance)
    #     displacement = Vector2((0, 1))
    #     wander_angle = wander_angle + (random.randrange(0, 10) * 1) - (1 * .5)
    #     displacement.x = math.cos(wander_angle) * 

    def add_force(self, force, deltatime):
        '''force'''
        self.force = force.scalarmult(deltatime)
        self.acceleration = force.scalarmult(1/self.mass)
        self.velocity = self.velocity.add_vectors(self.force).scalarmult(deltatime)
        self.direction = self.velocity
        self.heading = self.direction
        if self.velocity.magnitude > 20:
            self.velocity = self.velocity.scalarmult(1/20)
        self.position = self.position.add_vectors(self.velocity)

    def draw(self, screen):
        '''draw object'''
        screen.blit(self.surface, self.position.vec, None, 0)

    def update(self, deltatime):
        '''update'''
        if self.Seek is True:
            self.add_force(self.seek(self.targetagent), deltatime)
        if self.Flee is True:
            self.add_force(self.flee(self.targetagent), deltatime)
        self.acceleration = self.force * (1 / self.mass)
        self.velocity = self.velocity + self.acceleration * deltatime
        self.position = self.position + self.velocity * deltatime

if __name__ == '__main__':
    import main as Main
    Main.main()

