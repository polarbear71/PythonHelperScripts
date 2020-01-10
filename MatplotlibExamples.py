#! /usr/bin/env python3

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random

xlist = np.arange(0, 10, 1)
y1list = [i*2 for i in range(0,10)]
y2list = [i+1.5 for i in range(0,10)]
y3list = [i*2*random.random() for i in range(0,10)]


plt.plot(xlist, y1list)
plt.plot(xlist, y2list)
plt.plot(xlist, y3list)
plt.show()
