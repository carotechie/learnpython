#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    time=s.split(':')
    
    if (time[2])[2:] == 'PM':
        time[0]=int(time[0])+12
    
    if time[0] == '12':
        print('here')
        time[0] = '00'

    if str(time[0]) == '24':
        print('I entered')
        time[0] = '12'

    TF=str(time[0])+':'+time[1]+':'+(time[2])[:2]
    print(str(TF))
    return TF
    #

if __name__ == '__main__':
    
    s = raw_input()

    result = timeConversion(s)

    
