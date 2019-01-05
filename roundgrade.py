#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    #
    res=0
    for i in range(len(grades)):
        if grades[i] >= 38:            
            res=(grades[i]/5 + 1)*5 - grades[i]
            print(str(res))
            if res <= 3:
                grades[i]=(grades[i]/5 + 1)*5
            
    print(str(grades))
    return grades

if __name__ == '__main__':

    n = int(raw_input())

    grades = []
    for _ in xrange(n):
        grades_item = int(raw_input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    
