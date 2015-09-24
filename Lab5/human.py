#!/usr/bin/python

class human:

    def __init__(self, x, y, status):
        self.x = x
        self.y = y
        self.status = status

        if (self.status == 1):
            print 'No I am infected, I dont want Malaria :('
        else:
            print 'wohoo I am save at '+ str(x) + ', ' + str(y) + ' !'
