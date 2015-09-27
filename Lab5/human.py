#!/usr/bin/python

from globalFunctions import decision

class human:

    # 0 = normaal = groen, 1 = infected = rood, 2 = immuun = blauw 
    colorList = ['green','red','blue']

    def __init__(self, x, y, status):
        self.x = x
        self.y = y
        self.status = status
        self.infectedOn = 0
        self.fatalInfection = 0

    def getColor(self):
        """ Get the color for the human for the draw step """
        return self.colorList[self.status]

    def checkLife(self, deathDelay, immunityChange):
        """ Check if the human dies because of malaria """

        #if the human is infected, check if it dies based on death-rate and
        # how long he has the disease
        if decision((self.infectedOn / float(deathDelay))):

            # if he the infection was not fatal he becomes better, and possibly immune
            if self.fatalInfection == 0:
                self.infectedOn = 0
                self.fatalInfection = 0
                self.status = 0

                if decision(float(immunityChange)):
                     self.status = 2

             # if the infection was fatal the human dies and a new baby is born
            else:
                return False

         # if the human is not dead or cured,  increase the amount of days it has the sickness
        else:
            self.infectedOn += 1

    def humanStung(self, mosquito, config):
        """ Check what happens to the human and the mosquito if the mosquito 
            stung the human"""

        # If the human is immune, nothing happens
        if self.status == 2:
            return

        # Else if the mosquito is not infected, but the human is. Check if the 
        # human must become infected
        elif mosquito.infected == 0 and self.status == 1 and decision(config['prob-mosq-human']):
            mosquito.infected = 1
            return

        # If the mosquito is infected, check if the human becomes infected
        elif mosquito.infected == 1 and decision(config['prob-mosq-human']):
            self.status = 1

            # Check if it's fatal
            if decision(config['death-rate']):
                self.fatalInfection = 1

            return
