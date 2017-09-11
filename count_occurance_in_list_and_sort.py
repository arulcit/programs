from collections import Counter

word = "CountNumberOfLettersInMe"

a = Counter(word)
print a
# Counter({'e': 4, 't': 3, 'r': 2, 'u': 2, 'n': 2, 'O': 1,
#          'C': 1, 'b': 1, 'f': 1, 'I': 1, 'M': 1, 'm': 1,
#          'L': 1, 'o': 1, 'N': 1, 's': 1})

print dict(a)
#{'C': 1, 'I': 1, 'M': 1, 'L': 1, 'O': 1, 'N': 1, 'b': 1, 'e': 4, 'f': 1, 'm': 1,
# 'o': 1, 'n': 2, 's': 1, 'r': 2, 'u': 2, 't': 3}

b = a.most_common()
print b
#[('e', 4), ('t', 3), ('r', 2), ('u', 2), ('n', 2), ('O', 1), ('C', 1), ('b', 1),
# ('f', 1), ('I', 1), ('M', 1), ('m', 1), ('L', 1), ('o', 1), ('N', 1), ('s', 1)]

#Now Sort it by number of occurrances

c = sorted(b,key = lambda a:a[1],reverse=True)

print c
#[('e', 4), ('t', 3), ('r', 2), ('u', 2), ('n', 2), ('O', 1), ('C', 1), ('b', 1),
# ('f', 1), ('I', 1), ('M', 1), ('m', 1), ('L', 1), ('o', 1), ('N', 1), ('s', 1)]

#Now Sort by alphabets

d = sorted(b,key=lambda a:a[0])

print d
#[('C', 1), ('I', 1), ('L', 1), ('M', 1), ('N', 1), ('O', 1), ('b', 1),
# ('e', 4), ('f', 1), ('m', 1), ('n', 2), ('o', 1), ('r', 2), ('s', 1), ('t', 3), ('u', 2)]

