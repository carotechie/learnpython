#!/bin/python

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    k=len(arr)
    sum1=0
    sum2=0
    for i in range(0,k):
        sum1=arr[i][i]+sum1
        sum2=arr[k-1-i][i]+sum2
        res=abs(sum1-sum2)
    return res


if __name__ == '__main__':
    
    n = int(raw_input())

    arr = []

    for _ in xrange(n):
        arr.append(map(int, raw_input().rstrip().split()))

    result = diagonalDifference(arr)


