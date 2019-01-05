#!/bin/python

import math
import os
import random
import re
import sys
import numpy as np

# Complete the plusMinus function below.
def plusMinus(arr):
    np_arr=np.array(arr)
    pos=(np_arr[np_arr>0]).size*1.0/np_arr.size
    neg=(np_arr[np_arr>0]).size*1.0/np_arr.size
    zer=(np_arr[np_arr==0]).size*1.0/np_arr.size
    print(str(pos))
    print(str(neg))
    print(str(zer))

if __name__ == '__main__':
    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    plusMinus(arr)
