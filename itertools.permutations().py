"""
You are given a string .
Your task is to print all possible permutations of size  of the string in lexicographic sorted order.
"""

from itertools import permutations

x, y = list(input().split())
result = list(permutations(x, int(y)))
for i in sorted(result):
    print(*i,sep='')