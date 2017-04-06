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
        self.position = Vector2((0, 300))
        self.velocity = Vector2((300, 0))
        self.maxvelocity = 250.0
        self.mass = 1
        self.force = Vector2((0, 0))
        self.heading = self.velocity.normalize
        self.direction = Vector2((0, 0))
        self.acceleration = Vector2((0, 0))
        self.surface = pygame.Surface((100, 50), pygame.SRCALPHA)
        self.surface.fill((0, 0, 0))
        points = [(0, 0), (75, 25), (0, 50), (0, 0)]
        pygame.draw.lines(self.surface, constants.RED, False, points, 1)
        self.Seek = False
        self.Flee = False
        self.Wander = False
        self.targetagent = None
        self.radius = 10
        self.distance = 5

    def seek(self, target):
        '''seek'''
        distance = target.position.distance(self.position)
        normdistance = distance.normalize
        scaledis = normdistance.scalarmult(self.maxvelocity)
        seekforce = scaledis.sub_vectors(self.velocity)
        return seekforce

    def flee(self, target):
        '''flee'''
        #return self.seek(target) * -1.0
        distance = self.position.distance(target.position)
        normdistance = distance.normalize
        scaledis = normdistance.scalarmult(self.maxvelocity)
        fleeforce = scaledis.sub_vectors(self.velocity)
        return fleeforce

    def wander(self, distance, radius):
        '''wander'''
        center_circle = self.velocity.normalize
        center_circle = center_circle.scalarmult(distance)
        displacement = Vector2((0, 1))
        dis = displacement.scalarmult(radius)
        wander_angle = 10
        wander_angle = wander_angle + (random.randrange(0, 10) * 1) - (1 * .5)
        dis.x = math.cos(wander_angle) * dis.magnitude
        dis.y = math.sin(wander_angle) * dis.magnitude
        wanderforce = center_circle + dis
        return wanderforce

    def add_force(self, force):
        '''add force'''
        self.force = self.force + force
        self.force = self.force * (1 / self.mass)

    def draw(self, screen):
        '''draw object'''
        screen.blit(self.surface, self.position.vec)

    def update(self, deltatime):
        '''update'''
        if self.Seek is True:
            self.add_force(self.seek(self.targetagent))

        if self.Flee is True:
            self.add_force(self.flee(self.targetagent))

        if self.Wander is True:
            self.add_force(self.wander(self.distance, self.radius))

        self.acceleration = self.force
        self.heading = self.velocity.normalize
        self.velocity = self.heading * self.velocity.magnitude + self.acceleration * deltatime
        if self.velocity.magnitude > self.maxvelocity:
            self.velocity = self.velocity.normalize * self.maxvelocity
        self.position = self.position + self.velocity * deltatime


if __name__ == '__main__':
    import main as Main
    Main.main()
