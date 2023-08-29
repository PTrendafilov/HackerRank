#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    days_dict = {'Day':1, 'Shares':5, 'Likes': 2, 'Cumulative':0}
    
    for i in range(1,n+1):
        days_dict['Likes']=math.floor(days_dict['Shares']/2)
        days_dict['Cumulative']+=days_dict['Likes']
        days_dict['Shares']=days_dict['Likes']*3
        days_dict['Day']+=1
        
    return days_dict['Cumulative']
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
