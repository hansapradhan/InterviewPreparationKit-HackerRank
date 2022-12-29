#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&isFullScreen=false&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    i = 0
    counter = 0
    while i<len(c)-1:
        if(i<len(c)-2 and c[i+2]==0):
            i+=1
        i+=1
        counter+=1
    return counter
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
