'''Agent class'''
import vectormath
from vectormath import Vector2


class Agent(object):
    '''Agent'''

    def __init__(self):
        self.position = Vector2(0, 0)
        self.velocity = Vector2(0, 0)
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
        self.position = (self.position + self.velocity)
        self.velocity = (self.velocity + self.force)


