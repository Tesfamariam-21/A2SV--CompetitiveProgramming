#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    for i in range(1, n):
        j = i
        num = float("inf")
        
        while j > 0 and arr[j-1] >arr[j]:
            num = arr[j]
            arr[j] = arr[j-1] 
            # arr[j-1], arr[j] = arr[j], arr[j-1]
            print(*arr)
            arr[j-1] = num
            j -= 1
    
    print(*arr)
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
