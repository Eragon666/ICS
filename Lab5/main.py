#!/usr/bin/python

import ast

import mosquito as m
import human as h

import numpy as np
import random


class simulation():

    def __init__(self, config):
        """ Initialize the class and save the config """
        self.config = config

    def initalizeGrid(self):
        """ Initialize the grid and the human and mosquito classes """
        config = self.config

        # Numpy array with the size of the grix
        self.humanGrid = np.ndarray(shape=(config['grid-x'] +1, 
            config['grid-y'] + 1), dtype=object)

        self.mosquitoGrid = np.ndarray(shape=(config['grid-x'] + 1,
            config['grid-y'] + 1, config['max-mosq']), dtype=object)

        self.addHumans()

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
        humanGrid = self.humanGrid

        # Get the numbers of humans in the initial state
        popHuman = int(config['pop-human'])

        nrinfected = popHuman*config['init-distr-human']

        # Generate a list with randomly chosen infected humans based on
        # init-distr-human config value
        infected = random.sample(xrange(popHuman), int(nrinfected))

        for i in range(1, popHuman):
            if i in infected:
                status = 1 #Infected
            else:
                status = 0 #Not infected

            found = False

            # Make sure that every grid place has only one human
            while (not found):
                coordinates = self.getCoordinates()
                x = coordinates[0]
                y = coordinates[1]

                if (grid[x][y] == None):
                    found = True

            humanGrid[x][y] = h.human(x, y,status)

    def addMosquitos(self):
        """ Add the mosquitos to the grid, there can be humans and mosquitos on
        the same field and even multiple mosquitos on one field. """

        config = self.config
        grid = self.grid

        # Get the numbers of mosquitos in the initial state
        popMosq = int(config['pop-human'])

        nrinfected = popMosq*config['init-distr-mosq']

        infected = random.sample(xrange(popMosq), int(nrinfected))

        for i in range(1, popMosq):
            if i in infected:
                status = 1 #infected
            else:
                status = 0

            coordinates = self.getCoordinates()
            x = coordinates[0]
            y = coordinates[1]

            m.mosquito(1,2,status)

    def getCoordinates(self):
        x = random.randint(0, self.config['grid-x'])
        y = random.randint(0, self.config['grid-y'])

        return (x, y)

if __name__ == '__main__':

    with open('config.txt', 'r') as inf:
        config = ast.literal_eval(inf.read())

    sim = simulation(config)

    sim.initalizeGrid()
