#!/bin/python

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    total=sum(arr)
    max_vals=total-min(arr)
    min_vals=total - max(arr)
    
    print(str(min_vals)+ ' '+str(max_vals))
    
if __name__ == '__main__':
    arr = map(int, raw_input().rstrip().split())

    miniMaxSum(arr)
