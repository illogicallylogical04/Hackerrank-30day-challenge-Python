#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    for num in range(1,11):
        print('{0} x {1} = {2}'.format(n, num, n*num))
