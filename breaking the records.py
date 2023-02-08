#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    maxsc =scores[0]
    minsc =scores[0]
    maxscore =0
    minscore =0
    for i in range(len(scores)):
        if(scores[i]>maxsc):
            maxsc = scores[i]
            maxscore+=1
        if(scores[i]<minsc ):
            minsc  = scores[i]
            minscore +=1
    return [maxscore, minscore ]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()