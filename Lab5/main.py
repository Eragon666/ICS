#!/usr/bin/python

import ast

import mosquito as m
import human as h
import grid as g

import numpy as np
import random


class simulation():

    def __init__(self, config):
        """ Initialize the class and save the config """
        self.config = config

    def initalizeGrid(self):
        """ Initialize the grid and the human and mosquito classes """
        config = self.config

        # Numpy array with the size of the grid
        self.grid = np.ndarray(shape=(config['grid-x'],
            config['grid-y']), dtype=object)

        # Add a grid instance to the array
        for (x,y), value in np.ndenumerate(self.grid):
            self.grid[x][y] = g.grid(x, y)

        self.addHumans()
        self.addMosquitos()

        # Twee opties om de grid op te slaan: 
        # 1: Zoals het nu ongeveer is, 1 human grid en 1 los mosquito grid.
        # Beetje vaag zo aangezien ik niet goed weet hoe groot je die mosquito
        # grid moet maken (de derde array) zodat je er meerdere mosquitos op
        # kan zetten. En dan heb je een hele hoop lege array keys, en je weet
        # niet precies welke daar nou vol van zitten.
        # 2: Een class per grid vlakje, dus bij grid.py met daarin een class
        # die dan heeft opgeslagen of er een mens is (met de object/link naar
        # die class), en vervolgens een list die je kan appenden met mosquitos.
        # Je kan in die class dan dus ook lokale berekening doen, hoeveel
        # muggen komen hier bijvoorbeeld. En daar checken of het mens die daar
        # zit wordt gestoken etc.

    def addHumans(self):
        """Add humans to the grid, only one human can be on each field"""

        config = self.config
        grid = self.grid

        # Get the numbers of humans in the initial state
        popHuman = int(config['pop-human'])

        #nrinfected = popHuman*config['init-distr-human']

        # Generate a list with randomly chosen infected humans based on
        # init-distr-human config value
        #infected = random.sample(xrange(popHuman), int(nrinfected))
        infected = (np.random.rand(popHuman) > config['init-distr-human']).astype(int)

        for i in range(0, popHuman-1):
            status = infected[i]

            found = False

            # Make sure that every grid place has only one human
            while (not found):
                (x,y) = self.getCoordinates()

                if (grid[x][y].checkFreedom() == True):
                    found = True

            if i%1000 == 0:
                print i

            grid[x][y].moveIn(h.human(x, y,status))

    def addMosquitos(self):
        """ Add the mosquitos to the grid, there can be humans and mosquitos on
        the same field and even multiple mosquitos on one field. """

        config = self.config
        grid = self.grid

        # Get the numbers of mosquitos in the initial state
        popMosq = int(config['pop-mosq'])

        #nrinfected = popMosq*config['init-distr-mosq']
        #infected = random.sample(xrange(popMosq), int(nrinfected))
        infected = (np.random.rand(popMosq) > config['init-distr-mosq']).astype(int)

        for i in range(1, popMosq-1):
            status = infected[i]

            (x,y) = self.getCoordinates()

            if i%1000 == 0:
                print i

            grid[x][y].flyIn(m.mosquito(x,y,status))

    def getCoordinates(self):
        x = random.randint(0, self.config['grid-x'] - 1)
        y = random.randint(0, self.config['grid-y'] - 1)

        return (x, y)

if __name__ == '__main__':

    with open('config.txt', 'r') as inf:
        config = ast.literal_eval(inf.read())

    sim = simulation(config)

    sim.initalizeGrid()
