'''Agent class'''
import vectormath


class Agent(object):
    '''Agent'''

    def __init__(self):
        self.position = (0, 0)
        self.velocity = (0, 0)
        self.maxvelocity = 10
        self.force = (0, 0)

    def seek(self, target):
        '''seek'''
        dis = vectormath.distance(self.position, target.position)
        vectormath.normalize(dis)
        for i in dis:
            i * self.maxvelocity
        self.velocity = (dis[0] - self.velocity[0], dis[1] - self.velocity[1])




