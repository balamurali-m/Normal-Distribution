# -*- coding: utf-8 -*-
"""
Standard Normal Distribution
Author: Balamurali M
"""

import numpy as np
import matplotlib.pyplot as plt

class norm1:
    def __init__(self, a1, b1, c1):
        self.a1 = a1
        self.b1 = b1
        self.c1 = c1
        
    def dist_curve(self):
        plt.plot(self.c1, 1/(self.b1 * np.sqrt(2 * np.pi)) *
            np.exp( - (self.c1 - self.a1)**2 / (2 * self.b1**2) ), linewidth=2, color='y')
        plt.show()

#mean 0 and sd 1 for the standard normal distribution
mean = 0
sd = 1

c = np.random.normal(mean, sd, 3000)
        
w1, x1, z1 = plt.hist(c, 100, normed=True) #hist

hist1 = norm1(mean, sd, x1)
plot1 = hist1.dist_curve()