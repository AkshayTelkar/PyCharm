"""
You are given  words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond
with the input order of appearance of the word. See the sample input/output for clarification.
=Note: Each input line ends with a "\n" character
"""

from collections import OrderedDict

ordered_dict = OrderedDict()
for _ in range(int(input())):
    word = input()
    ordered_dict[word] = ordered_dict.get(word, 0) + 1
print(ordered_dict)
print(len(ordered_dict))
print(*ordered_dict.values())