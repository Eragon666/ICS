#!/usr/bin/python

from globalFunctions import decision, decisionLogarithmic

class human:

    # 0 = normaal = groen, 1 = infected = rood, 2 = immuun = blauw 
    colorList = ['green','red','blue']

    def __init__(self, x, y, status, mother, config, medicine=False):
        self.x = x
        self.y = y
        self.status = status
        self.infectedOn = 0
        self.fatalInfection = 0
        self.medicine = medicine
        self.mother = mother
        self.config = config

    def getColor(self):
        """ Get the color for the human for the draw step """
        return self.colorList[self.status]

    def checkLife(self):
        """ Check if the human dies because of malaria """

        # If the infection is deadly, check if it's time to die already
        if self.fatalInfection == True and decisionLogarithmic((self.infectedOn/
                float(self.config['death-delay']))):
            self.mother(4)
            return True

        # If access to good medicine, cure is short. Check if cured already
        elif self.medicine == True and decisionLogarithmic((self.infectedOn /
                float(self.config['cure-medicine']))):
            self.infectedOn = 0
            self.status = 0
            self.mother(3)
            self.checkImmune()

        # If no access to good medicine, check if cured
        elif decisionLogarithmic((self.infectedOn/float(self.config['cure']))):
            self.infectedOn = 0
            self.status = 0
            self.mother(3)
            self.checkImmune()

        # Increase the time already infected
        else:
            self.infectedOn += 1



    def checkImmune(self):
        """ Check if the human becomes immune after malaria infection """

        if decision(float(self.config['immunity-chance'])):
            self.status = 2
            self.mother(2)

    def humanStung(self, mosquito, config):
        """ Check what happens to the human and the mosquito if the mosquito 
            stung the human"""
        # the mosquito has eaten and isn't hungry anymore,
        # it's also immediatly making eggs
        mosquito.hungry = 0
        mosquito.oviposition += 1

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
            #print "human infected"

            # Check if it's fatal and no access to good medicine
            if self.medicine ==  False and decision(config['death-rate']):
                self.fatalInfection = 1
                self.mother(1)

            return
