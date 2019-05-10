"""
You are given a string .
Your task is to print all possible combinations, up to size , of the string in lexicographic sorted order.
"""

from itertools import combinations

a, b = list(input().split())

for i in range(int(b)):
    result = list(combinations(sorted(a), 1 + i))
    for i in result:
        print(*i,sep='')
