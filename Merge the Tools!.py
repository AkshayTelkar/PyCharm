def merge_the_tools(string, k):
    substr = []
    for i in range(int(len(string)/k)):
        while i < len(string) - 3:
            
    print(substr)

if __name__ == '__main__':
    string, k = input(), int(input())
    print(string)
    print(k)
    print(len(string)/k)
    merge_the_tools(string, k)
