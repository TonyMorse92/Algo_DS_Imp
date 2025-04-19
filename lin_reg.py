import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

x = np.arange(0,10,1)
y = x + random.uniform(0,3)

# y = mx + b
slope = np.polyfit(x,y,1)
poly1d_fn = np.poly1d(slope)


plt.plot(x, y, 'yo', x, poly1d_fn(x), '--k')

plt.xlim(0,5)
plt.ylim(0,12)


plt.show()
