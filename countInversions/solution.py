from os import *
from sys import *
from collections import *
from math import *


def getInversions(arr, n):
    '''
    TC: O(n^2)
    SC: O(1)
    '''
    
    inversions = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]: inversions += 1
    return inversions


# TS1
arr = [3, 2, 1]
output = 3

# TS2
arr=[2, 5, 1, 3, 4]
output = 4


n = len(arr)

print(getInversions(arr, n))
