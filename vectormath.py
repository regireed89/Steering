'''vector math library'''
import math


def magnitude(vector):
    '''magnitude'''
    return math.sqrt((vector[0] * vector[0]) + (vector[1] * vector[1]))

def normalize(vector):
    '''normalize'''
    return (vector[0]/magnitude(vector), vector[1]/magnitude(vector))

def distance(vector1, vector2):
    '''distance'''
    return (vector1[0] - vector2[0], vector1[1] - vector2[1])
