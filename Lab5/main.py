#!/usr/bin/python

import ast

import mosquito as m
import human as h
import random


class simulation():

    def __init__(self, config):
        """ Initialize the class and save the config """
        self.config = config

    def initalizeGrid(self):
        """ Initialize the grid and the human and mosquito classes """
        config = self.config

        # Get the numbers of humans and mosquitos in the initial state
        popHuman = int(config['pop-human'])
        popMosq = int(config['pop-mosq'])

        nrinfected = popHuman*config['init-distr-human']

        # Generate a list with randomly chosen infected humans based on
        # init-distr-human config value
        infected = random.sample(xrange(popHuman), int(nrinfected))

        for i in range(1, popHuman):
            if i in infected:
                status = 1 #Infected
            else:
                status = 0 #Not infected

            h.human(1,2,status)

        nrinfected = popMosq*config['init-distr-mosq']

        infected = random.sample(xrange(popMosq), int(nrinfected))

        for i in range(1, popMosq):
            if i in infected:
                status = 1 #infected
            else:
                status = 0

            m.mosquito(1,2,status)

if __name__ == '__main__':

    with open('config.txt', 'r') as inf:
        config = ast.literal_eval(inf.read())

    sim = simulation(config)

    sim.initalizeGrid()
