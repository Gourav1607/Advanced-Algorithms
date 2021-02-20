#!/usr/bin/env python
# coding: utf-8

# Maximum Subset Sum
# Gourav Siddhad

#################################################################

import numpy as np

#################################################################

# To calculate sum of all elements > 0. Except first element


def maxsum(ar):
    res = 0
    for a in ar:
        if a > 0:
            res += a
    return res

# To calculate sum of all elements < 0. Except first element


def minsum(ar):
    res = 0
    for a in ar:
        if a < 0:
            res += a
    return res

#################################################################


ar = input('Enter elements seperated by space : ')
ar = np.array(ar.split(), dtype='int')

# maxs is the maximum sum possible without first element
maxs = maxsum(ar[1:])
# mins is the maximum sum possible including first element, and negation
mins = -1*(minsum(ar[1:]) + ar[0])

# Check and Print the maximum possible sum
print(max(maxs, mins))

#################################################################
