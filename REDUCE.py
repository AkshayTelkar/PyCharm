from functools import reduce

def addition(array):
    add = 0
    for i in array:
        add += int(i)
    return add

arr = list(input())
print(addition(arr))

#Optimised
print(int(map(reduce(lambda x, y: int(x) + int(y), arr))))