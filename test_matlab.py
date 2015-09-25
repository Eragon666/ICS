import matplotlib
matplotlib.use('GTKAgg') 
from time import time
import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 1000, 0, 1])
plt.ion()
plt.show()

tic = time()
for i in range(100):
	plt.cla()
	plt.axis([0, 1000, 0, 1])
	y = np.random.random()
	plt.scatter(i, y)
	plt.draw()

print "Matplotlib average FPS: %.2f" %(100/(time()-tic))