#!/bin/python3
#Simple Array Sum

import os
import sys

x = int(input())
y = list(map(int,input().rstrip().split()))
sum=0;
for i in range(x):
    sum+=y[i]
print(sum)