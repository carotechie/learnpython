#!/bin/python

import math
import os
import random
import re
import sys

# Complete the introTutorial function below.
def introTutorial(V, arr):
    for i in range(len(arr)):
       if arr[i] == V:
         result=i
    print(str(result))
    return result

if __name__ == '__main__':
    

    V = int(raw_input())

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    result = introTutorial(V, arr)

    