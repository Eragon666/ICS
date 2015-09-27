from numpy import random

def decision(probability):
    """ Makes a decision based on a probability """
    return random.random_sample() < probability

def decisionLogarithmic(probability):
    """ Makes a decision based on a probability """
    return random.random_sample() < probability*probability*probability
