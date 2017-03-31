'''vector math library'''
import math


class Vector2(object):
    '''vector math'''

    def __init__(self, (x, y)):
        '''init'''
        self.x = x
        self.y = y
        self.vec = (self.x, self.y)

    def magnitude(self):
        '''magnitude'''
        return math.sqrt((self.x * self.x) + (self.y * self.y))

    def normalize(self):
        '''normalize'''
        return Vector2((self.x / self.magnitude(), self.y / self.magnitude()))

    def distance(self, vector2):
        '''distance'''
        return Vector2((self.x - vector2.x, self.x - vector2.y))

    def add_vectors(self, vector):
        '''add vetors'''
        return Vector2(((self.x + vector.x), (self.y + vector.y)))

    def sub_vectors(self, vector):
        '''subtract vectors'''
        return Vector2(((self.x - vector.x), (self.y - vector.y)))

    def scalarmult(self, scale):
        '''scale vector'''
        return Vector2((self.x * scale, self.y * scale))

    def dot_product(self, vector):
        '''dot product'''
        return (self.x * vector.x) + (self.y * vector.y)
    def __add__(self, other):
        return self.add_vectors(other)

    def __mul__(self, scalar):
        return self.scalarmult(scalar)
    
    def __sub__(self, other):
        return self.sub_vectors(other)
