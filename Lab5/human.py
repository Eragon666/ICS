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
        return self.colorList[self.status]

    def checkLife(self, deathDelay, immunityChange):
        #if the human is infected, check if it dies based on death-rate and
        # how long he has the disease
        if decision((self.infectedOn / float(deathDelay))):

            # if he the infection was not fatal he becomes better, and possibly immune
            if human.fatalInfection == 0:
                human.infectedOn = 0
                human.fatalInfection = 0
                human.status = 0

                if decision(float(immunityChange)):
                     human.status = 2

             # if the infection was fatal the human dies and a new baby is born
            else:
                human = None
                # find a free cell, create a human and place it
                (freeX,freeY) = self.findHomeHuman()
                self.grid[x][y].moveIn(h.human(x, y, 0))

         # if the human is not dead or better,  increase the amount of days it has the sickness
        else:
            self.infectedOn += 1
