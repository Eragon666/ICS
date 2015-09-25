#!/usr/bin/python
import numpy as np
import time
import matplotlib
matplotlib.use('GTKAgg')
from matplotlib import pyplot as plt



def run(niter=100, x, y, colors):
    """
    Display the simulation using matplotlib, optionally using blit for speed
    """

    colors = np.random.rand(50)

    # create figure and set it to a big size
    plt.figure(figsize=(20,10))
    plt.axis([0, dims[0], 0, dims[1]])
    plt.ion()
    plt.show()

    tic = time.time()
    for i in xrange(niter):
        x = dims[0] * np.random.random_sample((50000,))
        y = dims[1] * np.random.random_sample((50000,))
        plt.cla()
        plt.axis([0, dims[0], 0, dims[1]])
        plt.scatter(x, y, s=1, c=colors)
        plt.draw()

    print "Average FPS: %.2f" % (niter / (time.time() - tic))

if __name__ == '__main__':
    run()