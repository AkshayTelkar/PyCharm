def word(string):
    count1 = 0
    if string[0] == 'S':
        count1 = count1 + 1
    return count1


b = list(map(lambda x: word(x), ['San Jose', 'San Francisco', 'Santa Fe', 'Houston']))
print(sum(b))
