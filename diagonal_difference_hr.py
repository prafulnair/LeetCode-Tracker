#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    left_sum = 0
    right_sum = 0
    
    for i in range(0, len(arr[0])):
        for j in range(0, len(arr)):
            if i == j:
                left_sum+=arr[i][j]
                
    counter = len(arr[0]) -1 
    for row in arr:
        element = row[counter]
        right_sum+=element
        counter-=1
        
    return abs(left_sum-right_sum)
                
    """
    00 01 02 03
    10 11 12 13
    20 21 22 23
    30 31 32 33
    """
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()


