#!/usr/bin/python

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

