'''Agent class'''
import vectormath


class Agent(object):
    '''Agent'''

    def __init__(self):
        self.position = (0, 0)
        self.velocity = (0, 0)
        self.maxvelocity = 10
        self.force = (0, 0)
        self.heading = (0, 0)

    def seek(self, target):
        '''seek'''
        dis = vectormath.distance(self.position, target.position)
        vectormath.normalize(dis)
        dis * self.maxvelocity
        self.velocity = (dis[0] - self.velocity[0], dis[1] - self.velocity[1])
        return self.velocity

    def add_force(self):
        '''force'''
        self.position = (self.position + self.velocity)
        self.velocity = (self.velocity + self.force)
