import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.250, 2.5, 0.01)
s = 1 + np.sin(2 * np.pi * t)*np.exp(-t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()



from math import sin, exp, pi
from random import random
fitnessfunction = lambda t: 1 + sin(2 * pi * t)*exp(-t)

xopt = .25 + 2.25*random()
yopt = fitnessfunction(xopt)

max_generation = 5
for itr in range(max_generation):
       xnew = .25 + 2.25 * random()
       ynew = fitnessfunction(xnew)

       if ynew<yopt:
              xopt = xnew
              yopt = ynew


print('xopt: %.02f' %xopt)
print('yopt: %.02f' %yopt)


ax.plot(xopt, yopt, 'o')

plt.show()