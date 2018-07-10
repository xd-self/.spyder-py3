# -*- coding: utf-8 -*-
import numpy as np
from pandas import Series, DataFrame
import pandas as pd
import matplotlib.pyplot as plt

s1 = Series(np.arange(15))
'''fig = plt.figure()
ax1 = fig.add_subplot(1,3,1)
ax2 = fig.add_subplot(1,3,2)
ax3 = fig.add_subplot(1,3,3)

ax1.plot(s1)'''
s2 = np.random.randn(10)
fig, axe = plt.subplots(2,3,sharex=True,sharey=True)



fig.subplots_adjust(wspace=0,hspace=0)# not effective?


