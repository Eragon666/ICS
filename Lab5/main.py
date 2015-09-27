#!/usr/bin/python

import ast
import time

import mosquito as m
import human as h
import grid as g
import plot as p

import numpy as np
import random

class simulation():

    def __init__(self, config):
        """ Initialize the class and save the config """
        self.config = config
        self.t = 0
        self.deads = 0
        self.infected = 0
        self.imume = 0
        self.cured = 0

    def motherStats(self, resp):
        """ Callback function for childs to return their status and gather
        statistics """

        # a person is infected
        if resp == 1:
            self.infected += 1

        # a person is now imume
        elif resp == 2:
            self.imume += 1

        # a person is cured
        elif resp == 3:
            self.cured += 1

        # a person died
        elif resp == 4:
            self.deads += 1

    def initalizeGrid(self):
        """ Initialize the grid and the human and mosquito classes """
        config = self.config

        # Numpy array with the size of the grid
        self.grid = np.ndarray(shape=(config['grid-x'],
            config['grid-y']), dtype=object)

        self.plotX  = []
        self.plotY  = []
        self.plotType = []
        self.plotSize = []

        # Add a grid instance to the array
        for x in xrange(0, config['grid-y']):
            for y in xrange(0, config['grid-x']):
                self.grid[x][y] = g.grid(x, y,config)

        self.addHumans()
        self.addMosquitos()


    def addHumans(self):
        """Add humans to the grid, only one human can be on each field"""

        # Get the numbers of humans in the initial state
        popHuman = int(self.config['pop-human'])

        # Generate a list with randomly chosen infected humans based on
        # init-distr-human config value
        infected = (np.random.rand(popHuman) < self.config['init-distr-human']).astype(int)
        #print infected

        for i in xrange(0, popHuman-1):
            found = False

            # Make sure that every grid place has only one human
            (x,y) = self.findHomeHuman()

            self.grid[x][y].moveIn(h.human(x, y, infected[i], self.motherStats))

    def findHomeHuman(self):
        """ Find a free cell for a human """
        while (True):
            (x,y) = self.getCoordinates()

            if (self.grid[x][y].checkFreedom() == True):
                return (x,y)


    def cycleOfLife(self, x, y):
        """ Deaths of humans by sickness and keeping the human population stable
        by generating new humans if needed """

        human = self.grid[x][y].human
        # return if no (infected) human, nothing to do here
        if human == None or human.status != 1:
            return True

        # Check what happens to the human, if false is returns the human died
        elif human.checkLife(self.config['death-delay'], 
                self.config['immunity-change']) == False:
            # Human died, remove from grid
            self.grid[x][y].moveOut()
            (freeX,freeY) = self.findHomeHuman()
            self.grid[x][y].moveIn(h.human(x, y, 0, self.motherStats))

    def getCoordinates(self):
        """ Generate a pair of coordinates, return it as a tuple"""
        x = random.randint(0, self.config['grid-x'] - 1)
        y = random.randint(0, self.config['grid-y'] - 1)

        return (x, y)


    def step(self):
        """ Do all the steps """
        plotX = []
        plotY = []
        plotType = []
        plotSize = []

        self.t += 1

        # Speed up of the code, use local vars in for loops
        xAppend = plotX.append
        yAppend = plotY.append
        typeAppend = plotType.append
        sizeAppend = plotSize.append
        step = self.stepMosquitos
        cycle = self.cycleOfLife
        grid = self.grid

        infectedNow = 0

        for x in xrange(0, config['grid-y'] - 1):
            start = time.time()

            for y in xrange(0, config['grid-x'] - 1):
                # Mosquitos take a step, and check for human deaths
                step(x, y)
                cycle(x,y)
                (status, objectSize) = grid[x][y].getInhabitants()

                # add values to plot lists
                if status != False:
                    if status == 'red':
                        infectedNow += 1
                    xAppend(int(x))
                    yAppend(int(y))
                    typeAppend(status)
                    sizeAppend(objectSize)

        prevalence = float(infectedNow)/float(self.config['pop-human']) * 100.0

        print 'People infected atm: ' + str(infectedNow) + ' so prevalence = ' + str(prevalence)

        self.plotX = plotX
        self.plotY = plotY
        self.plotType = plotType
        self.plotSize = plotSize

    def addMosquitos(self):
        """ Add the mosquitos to the grid, there can be humans and mosquitos on
        the same field and even multiple mosquitos on one field. """

        # Get the numbers of mosquitos in the initial state
        popMosq = int(self.config['pop-mosq'])

        # Generate for each mosquito if it's infected or not and if it's hungry 
        # in the initial state. Based on the initial distribution.
        infected = (np.random.rand(popMosq) < self.config['init-distr-mosq']).astype(int)
        hungry = (np.random.rand(popMosq) < self.config['init-hungry-mosq']).astype(int)

        t = self.t
        randint = np.random.randint
        maxAge = self.config['mosq-max-age']

        for i in xrange(1, popMosq-1):
            (x,y) = self.getCoordinates()
            self.grid[x][y].flyIn(m.mosquito(x, y, t, infected[i], hungry[i],
                randint(maxAge)))

    def stepMosquitos(self, x, y):
        """ Calculate the step for the mosquitos """
        # Loop through the list of mosquitos and remove the mosquito from the
        # list if checkMosquito returns False
        grid = self.grid
        check = self.checkMosquito

        grid[x][y].mosquitos[:] = [ z for z in grid[x][y].mosquitos
                if check(z, (x,y)) ]


    def checkMosquito(self, mosquito, current):
        """ Check if the mosquitos stays in the same place """

        # Do the calculations for the next position of the mosquito
        (x, y) = mosquito.step(config['grid-x'] - 1, config['grid-y'] - 1,
                self.t, self.config['mosq-max-age'])

        # If x is -1, the mosquito died
        if x == -1:
            return False

        # If the mosquito did not move, return True
        elif current == (x, y):
            return True

        # Else place the mosquito in another cell and return False so the
        # mosquitos gets removed from the current field
        # The mosquito also eats blood of a human if there is one in its new cell
        else:
            self.grid[x][y].flyIn(mosquito)
            return False



if __name__ == '__main__':

    with open('config.txt', 'r') as inf:
        config = ast.literal_eval(inf.read())

    sim = simulation(config)
    plotter = p.plotter(config)

    start = time.time()
    sim.initalizeGrid()
    end = time.time()
    print end-start

    startSteps = time.time()

    for i in xrange(20):
        startSteps = time.time()
        sim.step()
        endSteps = time.time()

        startSteps2 = time.time()

        # Do not plot all the steps
        #if (i % 5 == 0):
        plotter.run(sim.plotX,sim.plotY,sim.plotSize,sim.plotType)

        endSteps2 = time.time()
        print "Step number:",i, " steptime:",endSteps-startSteps, " Plotter:",endSteps2-startSteps2

    print 'People died from Malaria: ' + str(sim.deads) + ', cured = ' + str(sim.cured) + ', imume = ' + str(sim.imume)

    #print sim.plotSize

    #print (endSteps-startSteps)/25


