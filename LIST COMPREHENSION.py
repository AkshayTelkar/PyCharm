N = int(input())
a = []
for i in range(N):
    a.append(list(map(int,input())))
print(a)

for j in range(len(a)):
    for k in range(len(a[j])):
        print(a[j][k])


a = [list(map(int, input())) for i in range(int(input()))]
print(a)
res = [print(a[j][k]) for j in range(len(a)) for k in range(len(a[j]))]
