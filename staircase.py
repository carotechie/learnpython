#!/bin/python

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(1,n+1):
        f=i
        while (n-f) != 0:
            sys.stdout.write(' ')
            f=f+1
        f=0
        while f != i:
            sys.stdout.write('#')
            f=f+1
        print('')


if __name__ == '__main__':
    n = int(raw_input())

    staircase(n)