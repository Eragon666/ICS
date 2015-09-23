#!/usr/bin/python

import ast

import mosquito as m
import human as h

class simulation():

    def __init__(self, config):
        self.config = config

    def initalizeGrid(self):
        h.human(1,2,3)
        m.mosquito(1,2,3)

if __name__ == '__main__':

    with open('config.txt', 'r') as inf:
        config = ast.literal_eval(inf.read())

    sim = simulation(config)

    sim.initalizeGrid()
