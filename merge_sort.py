
def merge_sort(alist):
    print alist
    length = len(alist)
    if length > 1:
        divide = length // 2

        lefthalf = alist[:divide]
        righthalf = alist[divide:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                k += 1
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
                k += 1

        if i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        if j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1

        print "Merged list", alist

    return alist



alist = [23, 45, 123, 82, 53, 5,29,423,23,42,45,123]
merge_sort(alist)

'''
Result
[23, 45, 123, 82, 53, 5, 29, 423, 23, 42, 45, 123]
[23, 45, 123, 82, 53, 5]
[23, 45, 123]
[23]
[45, 123]
[45]
[123]
Merged list [45, 123]
Merged list [23, 45, 123]
[82, 53, 5]
[82]
[53, 5]
[53]
[5]
Merged list [5, 53]
Merged list [5, 53, 82]
Merged list [5, 23, 45, 53, 82, 123]
[29, 423, 23, 42, 45, 123]
[29, 423, 23]
[29]
[423, 23]
[423]
[23]
Merged list [23, 423]
Merged list [23, 29, 423]
[42, 45, 123]
[42]
[45, 123]
[45]
[123]
Merged list [45, 123]
Merged list [42, 45, 123]
Merged list [23, 29, 42, 45, 123, 423]
Merged list [5, 23, 23, 29, 42, 45, 45, 53, 82, 123, 123, 423]
'''

