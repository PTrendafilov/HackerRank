import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s):
    unique_chars = set(s)
    
    max_length = 0
    for first in unique_chars:
        for second in unique_chars:
            if first != second:
                filtered_string = [char for char in s if char == first or char == second]
                
                if all(filtered_string[i] != filtered_string[i+1] for i in range(len(filtered_string)-1)):
                    max_length = max(max_length, len(filtered_string))

    return max_length
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
