#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    count1=0
    count2=0
    while (n>0):
        remainder=int(n%2)
        n=int(n/2)
        if (remainder==1):
            count1=count1+1
            if count1>count2:
                count2=count1
        else:
            count1=0
    print(count2)
