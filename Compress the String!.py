from itertools import groupby

a = list(map(int, input()))
result = []
for k, group in groupby(a):
    result.append(tuple((len(list(group)), k)))

print(*result)

"""
ip: 1222311
op: (1, 1) (3, 2) (1, 3) (2, 1)
"""