#!/usr/bin/env python
# coding: utf-8

# Lake Wobegon Hiring Strategy
# Gourav Siddhad

#################################################################

import numpy as np
import matplotlib.pyplot as plt
import random

#################################################################

A = list(np.random.uniform(low=60, high=100, size=(15)))
B = list(np.random.uniform(low=60, high=100, size=(15)))

meanA = [70]*15
minA = [60]*15
meanB = [70]*15
minB = [60]*15

#################################################################

while(1):
    print('{:04d}-{:04d}'.format(len(A), len(B)), end='\r')

    if (len(A) >= 5000 and len(B) >= 5000):
        break

    num = random.randint(60, 100)
    if len(A) < 5000 and num > meanA[-1]:
        A.append(num)
        meanA.append(np.mean(A))
        minA.append(np.min(A))
    if len(B) < 5000 and num > minB[-1]:
        B.append(num)
        meanB.append(np.mean(B))
        minB.append(np.min(B))

#################################################################

fig = plt.figure(figsize=(10, 5), dpi=300)
plt.plot(meanA, label='A mean', color='green')
plt.plot(meanB, label='B mean', color='red')
plt.grid(True)
plt.title('Comparison of average scores of employees')
plt.xlabel('# Employees')
plt.ylabel('Average Score')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('20911004_A05_Q5.png', dpi=300,
            bbox_inches='tight', pad_inches=0.2)
plt.show()

#################################################################
