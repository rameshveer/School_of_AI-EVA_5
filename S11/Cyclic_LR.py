#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 10:51:36 2020

@author: rameshveer
"""

import numpy as np
import matplotlib.pyplot as plt

# 2 x step_size = 1 cycle
step_size = 50

lr_min = 0.01
lr_max = 0.1

#total no of iterations we require
req_iterations = 500

# creating a 1000 equivalent values for our iteration values
iter = np.linspace(0, req_iterations, 1000)

lr = []


# Loop thru the iterations and create cyclic lr list 

for iterations in iter:
    cycle = np.floor(1 + iterations / (2 * step_size))

    x = np.abs( (iterations/step_size) - (2 * cycle) + 1 )

    lr_t = ( lr_min + (lr_max - lr_min) * (1 - x) )
    
    lr.append(lr_t)

print(lr)

#plot the cyclic curve with btw LR & iterations

plt.xlabel('iterations')
plt.ylabel('L R')
plt.plot(iter, lr)
