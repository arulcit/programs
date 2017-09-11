word = "CountNumberOfLettersInMe"
dict1 = {}
for i in word:
    dict1[i] = dict1.get(i,0) + 1
print dict1
#{'O': 1, 'C': 1, 'b': 1, 'e': 4, 'f': 1, 'I': 1, 'M': 1, 'm': 1, 'L': 1, 'o': 1, 'N': 1, 's': 1, 'r': 2, 'u': 2, 't': 3, 'n': 2}

#If this is needed in tuple format
from collections import Counter
b = Counter(dict1)
print b.most_common()
#[('e', 4), ('t', 3), ('n', 2), ('r', 2), ('u', 2), ('C', 1), ('I', 1), ('M', 1), ('L', 1), ('O', 1), ('N', 1), ('b', 1), ('f', 1), ('m', 1), ('o', 1), ('s', 1)]
