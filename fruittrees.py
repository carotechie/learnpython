#!/bin/python

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    ai=0
    oi=0
    for i in range(len(apples)):
        if (a+ apples[i])>= s and (a+apples[i]) <= t:
            ai=ai+1
    
    print(str(ai))

    for i in range(len(oranges)):
        if (b+ oranges[i])>= s and (b+oranges[i]) <= t:
            oi=oi+1
    
    print(str(oi))

if __name__ == '__main__':
    st = raw_input().split()

    s = int(st[0])

    t = int(st[1])

    ab = raw_input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = raw_input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = map(int, raw_input().rstrip().split())

    oranges = map(int, raw_input().rstrip().split())

    countApplesAndOranges(s, t, a, b, apples, oranges)
