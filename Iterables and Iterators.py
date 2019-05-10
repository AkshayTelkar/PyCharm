"""
find permutation of letter a in combination of string 'a a c d'
"""

from itertools import combinations

N = int(input())
a = list(input().split())
val = int(input())

result = list(combinations(a, val))
count = 0
for i in result:
    if 'a' in i:
        count += 1

print("%.3f" % (count/len(result)))

"""
ip: 
4
a a c d
2
op: 0.833
"""
