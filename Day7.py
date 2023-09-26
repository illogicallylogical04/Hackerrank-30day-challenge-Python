#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
    arr = arr[::-1]
    s = ''
    
    for i in arr:
        s += str(i) + ' '
        
    s = s.rstrip()
    print(s)
