from numpy import random
import math

def decisionLogarithmic(probability):
    """ Makes a decision based on a probability """
    if 0 < probability <= 0.97:
        return random.random_sample() < -math.log10(float(1-probability))/1.5
    elif probability > 0.97:
        return True
    else:
        return False

def decision(probability):
    """ Makes a decision based on a probability """
    return random.random_sample() < probability

