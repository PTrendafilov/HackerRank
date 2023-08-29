#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def beautifulDays(i, j, k):
    # Write your code here
    beautiful_days = 0
    days_list = []
    for day in range(i,j+1):
        days_list.append(day)
    
    for day in days_list:
        reversed_day=str(day)[::-1]
        
        if abs(int(reversed_day)-day)%k==0:
            beautiful_days+=1
            #print(f'{day} - {reversed_day} = {day-int(reversed_day)}')
    return beautiful_days
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
