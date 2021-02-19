#!/usr/bin/env python
# coding: utf-8

# Birthday Paradox
# Gourav Siddhad

#################################################################

import numpy as np

#################################################################

def simplify(a, b):
    c = int(np.gcd(a, b))
    a, b = a//c, b//c
    return int(a), int(b)

#################################################################

n, k = input('Enter n and k (n k) : ').split()
n, k = int(n), int(k)

num, den = int(1), int(1)
for i in range(k):
    tn = np.power(2, n) - i
    td = np.power(2, n)
    tn, td = simplify(tn, td)
    num *= tn
    den *= td
    num, den = simplify(num, den)

num = den - num
num, den = simplify(num, den)

print(num, den)

#################################################################
