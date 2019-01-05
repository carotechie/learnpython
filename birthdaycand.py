#!/bin/python

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    maxcand=max(ar)
    bdcand=ar.count(maxcand)
    print('Max cand:'+str(maxcand))
    print(str(bdcand)


if __name__ == '__main__':  
    ar = map(int, raw_input().rstrip().split())

    result = birthdayCakeCandles(ar)

