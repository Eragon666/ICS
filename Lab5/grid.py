#!/usr/bin/pythony

import numpy as np
from globalFunctions import decision
import mosquito as m

class grid:

    def __init__(self, x, y,config):
        self.x = x
        self.y = y
        self.human = None
        self.mosquitos = []
        self.config = config

    def checkFreedom(self):
        """Check if the human can live here or that there is already an
        inhabitant on this grid"""
        if self.human == None:
            return True
        else:
            return False

    def moveIn(self, human):
        """Add a human to this cell"""
        self.human = human

    def moveOut(self):
        """Remove the human from the cell"""
        #print 'Another dead man'
        self.human = None

    def flyIn(self, mosquito):
        """Fly the mosquito into the cell, multiple mosquitos can be in one
        cell"""
        self.mosquitos.append(mosquito)
        self.devourHumans(mosquito)

    def devourHumans(self,mosquito):
        """ eat a human if there is one and the is mosquito hungry """
        #print "Devour human: ", self.human , " Hunger:", mosquito.hungry

        if self.human != None and mosquito.hungry == 1:

            # Check the consequences of the bite to the human and the mosquito
            self.human.humanStung(mosquito, self.config)

            # the mosquito has eaten and isn't hungry anymore
            mosquito.hungry = 0

            # check if it is going to lay eggs: change of lays per lifetime/ maximum mosquito age
            # only if it has eaten and isn't hungry
            if decision(self.config['mosq-batches-lifetime'] / float(self.config['mosq-max-age'])):
                #print "Mother mosquito age:",mosquito.age
                append = self.mosquitos.append

                for x in xrange(0, self.config['mosq-eggs']):
                    append(m.mosquito(self.x, self.y, mosquito.t, mosquito.infected, 0, 0))
                #print "eitjes gelegd, # mosquitos nu:", len(self.mosquitos)

        # there is no human to eat so the mosquito becomes hungry from moving
        else: 
            self.hungry = 1

    def getMosquitos(self):
        """ return the list of mosquitos in this cell """
        return self.mosquitos

    def clearMosquitos(self):
        """ Clear the list of mosquitos in this cell """
        self.mosquitos = []

    def getInhabitants(self):
        """ return inhabitants in current cell """

        if self.human != None:
            return (self.human.getColor(), int(self.config['human-size']))
        elif not self.mosquitos:
            return (False, False)
        else:
            return (self.mosquitos[0].getColor(), int(self.config['mosquito-size']))

