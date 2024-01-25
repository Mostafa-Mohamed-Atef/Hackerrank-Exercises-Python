import math
import os
import random
import re
import sys

def solve(s):
    c = s.split(' ')
    cf = ''
    for i in c:
        ct = i.capitalize()
        cf +=ct + ' '
    return cf[:-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
