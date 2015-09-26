#!/usr/bin/python

class human:

    # 0 = normaal = groen, 1 = infected = rood, 2 = immuun = blauw 
    #colorList = ['green','red','blue']

    def __init__(self, x, y, status):
        self.x = x
        self.y = y
        self.status = status

    # def getColor(self):
    #     return self.status

        #if (self.status == 1):
        #    print 'No I am infected, I dont want Malaria :('
        #else:
        #    print 'wohoo I am save at '+ str(x) + ', ' + str(y) + ' !'
