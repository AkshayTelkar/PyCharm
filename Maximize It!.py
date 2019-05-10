"""
You are given a function . You are also given  lists. The  list consists of  elements.

You have to pick one element from each list so that the value from the equation below is maximized:

%denotes the element picked from the  list . Find the maximized value  obtained.

 denotes the modulo operator.
"""

from itertools import product

N_List, M = map(int, (input().split()))
List = []
for _ in range(N_List):
    List.append(list(map(int, input().split())))

for i in List:
    del i[0]

L_Product = list(product(*List))
max = 0
for j in L_Product:
    if (sum(list(map(lambda x: x ** 2, j))) % M) > max:
        max = sum(list(map(lambda x: x ** 2, j))) % M

print(max)

"""
3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10
op: 206
"""