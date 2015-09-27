#!/usr/bin/python
import numpy as np
import time
import matplotlib
matplotlib.use('GTKAgg')
from matplotlib import pyplot as plt

class plotter:

    def __init__(self, config):
        self.config = config
        plt.figure(figsize=(20,10))
        plt.axis([0, config['grid-x'], 0, config['grid-y']])
        plt.ion()
        plt.show()

    def run(self, x, y, objectSizes, colors):
        """
        Display the simulation using matplotlib, optionally using blit for speed
        """
        plt.cla()
        plt.axis([0, self.config['grid-x'], 0, self.config['grid-y']])
        plt.scatter(x, y, s=objectSizes, c=colors)
        plt.draw()

