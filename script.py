import numpy as np
from matplotlib import pyplot as plt
data = np.loadtxt('out')

label = np.loadtxt('mnist_label.txt')

xdata = data[:,0]
ydata = data[:,1]

plt.scatter(xdata, ydata, c=label, cmap=plt.cm.get_cmap("jet",10))
plt.colorbar(ticks=range(10))
plt.show()
