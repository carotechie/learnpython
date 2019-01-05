#!/bin/python
import math
import os
import random
import re
import sys

# Complete the bigSorting function below.
def bigSorting(unsorted) :
    unsorted.sort(key=long)
    
    print(unsorted)
    return unsorted

if __name__ == '__main__' :
    
    n = int(raw_input())
    unsorted = []
    for _ in xrange(n):
        unsorted_item = raw_input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    