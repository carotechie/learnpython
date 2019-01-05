#!/bin/python

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos=0
    neg=0
    zer=0
    for i in arr:
       if i > 0:
            pos=pos+1
       else:
           if i < 0:
                neg=neg+1
           else: 
                zer=zer+1
    pos=pos*1.0/len(arr)
    neg=neg*1.0/len(arr)
    zer=zer*1.0/len(arr)
    print(float(pos))
    print(str(neg))
    print(str(zer))

if __name__ == '__main__':
    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    plusMinus(arr)
