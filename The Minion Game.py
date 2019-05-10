"""
Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.
"""

def minion_game(string):
    vowel =['A','E','I','O','U']
    S = 0
    K = 0
    for i in range(len(string)):
        if string[i] in vowel:
            K += len(string)-i
        else:
            S += len(string)-i
    if S > K:
        print("Stuart"+" "+ "%d" % S)
    elif K > S:
        print("Kevin"+" "+'%d' % K)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)

"""
ip: BANANA
op: Stuart 12
"""