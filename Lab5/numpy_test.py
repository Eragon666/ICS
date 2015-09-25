
import numpy
import time


#numpy.random.choice([0, 1], size=1000, p=[.1, .9])
#(numpy.random.rand(1000) > 0.1).astype(int)

repetitions = 600000

start= time.clock()
for i in range(1000):
	(numpy.random.rand(repetitions) > 0.1).astype(int)
end= time.clock()
time= (end-start)/1000

print time

