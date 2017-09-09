
def bubble_sort(a):
    count = len(a) - 1
    exchanges = None
    for i in xrange(len(a)):
        if exchanges == False:
            break
        exchanges = False
        for j in xrange(count):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                exchanges = True
            print a
        count -= 1
        print
    return a

a = [54,26,93,17,77,31,44,55,20]
alist=[20,30,40,90,50,60,70,80,100,110]

b = bubble_sort(alist)
print b

