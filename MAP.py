def maping(ele):
    return int(ele) + int(ele)

arr = list(input())
result = []
for i in arr:
    result.append(maping(i))


#Optimised
print(list(map(lambda x: maping(x), arr)))