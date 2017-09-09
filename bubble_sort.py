
def bubble_sort(a):
    count = len(a) - 1
    for i in xrange(len(a)):
        for j in xrange(count):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
            print a
        count -= 1
        print
    return a

a = [54,26,93,17,77,31,44,55,20]
b = bubble_sort(a)
print b

