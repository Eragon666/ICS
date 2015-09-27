from numpy import random
import math

# def decisionLogarithmic(probability):
#     """ Makes a decision based on a probability """
#     if 0 < probability <= 0.99:
#         return random.random_sample() < -math.log10(float(1-probability))/2.0
#     elif probability == 0:
#         return False
#     else:
#         return True

def decisionLogarithmic(probability):
    return random.random_sample() < (probability*probability*probability)

def decision(probability):
    """ Makes a decision based on a probability """
    return random.random_sample() < probability

