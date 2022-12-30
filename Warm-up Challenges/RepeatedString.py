#!/bin/python3

import math
import os
import random
import re
import sys

# Question Link:
#  https://www.hackerrank.com/challenges/repeated-string?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    l = s.len()
    c = s.count('a',0,l)
    # calculating nos of a's
    num= (n/l) * c
    
    # for remaining if n%l!=0
    num+= s.count('a',0,n%l)   
    return num

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
