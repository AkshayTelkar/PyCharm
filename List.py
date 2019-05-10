if __name__ == '__main__':
    N = int(input())

commands = []
for i in range(N):
    inp = [commands.append(input().split())]

list_1 = []
for command in commands:
    if command[0] == 'insert':
        list_1.insert(int(command[1]), int(command[2]))
    elif command[0] == 'print':
        print(list_1)
    elif command[0] == 'remove':
        del list_1[list_1.index(int(command[1]))]
    elif command[0] == 'append':
        list_1.append(int(command[1]))
    elif command[0] == 'sort':
        list_1.sort()
    elif command[0] == 'pop':
        list_1.pop()
    else:
        if command[0] == 'reverse':
            list_1.reverse()