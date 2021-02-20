#!/usr/bin/env python
# coding: utf-8

# Gift Distribution
# Gourav Siddhad

#################################################################

import numpy as np

#################################################################


def get_response(N, M, C):
    maxn = 0
    unique, counts = np.unique(C, return_counts=True)
    print('Color:Count', dict(zip(unique, counts)))
    maxn = max(counts)
    if maxn > M:
        return "NO"
    else:
        return "YES"

#################################################################


N, M = input('Enter N and M (N M) : ').split()
N, M = int(N), int(M)

C = input('Enter list of colors of the gifts (c1, c2, ..., cn) : ').split()
C = np.array(C)

if len(C) != N:
    print('C must contain', N, 'elements, but it has ', len(C), 'elements')
else:
    res = get_response(N, M, C)
    print()
    print(res)

#################################################################
