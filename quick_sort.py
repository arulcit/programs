def quick_sorting(alist,first,last):

    # If length of list less than 2, skip
    if last - first > 0:
        print alist
        start = first
        end = last
        select_num = alist[start] # Select the pivot value

        while True:
            x = 0
            # Loop from beginning until the value greater than first value is found
            while x < (last-first):
                if alist[start] > select_num:
                    break
                start += 1
                x += 1
            y = 0
            # Loop from end towards start until the value less than first value is found
            while y < (last-first):
                if alist[end] < select_num:
                    break
                end -= 1
                y += 1
            # If start point and end point did not cross each other, exchange
            if end > start:
                alist[start],alist[end] = alist[end],alist[start]
            # start point and end point crossed each other, exchange start value
            # with correct position and pass the left side and right side to recursive
            # quick sorting
            else:
                alist[first], alist[end] = alist[end], alist[first]
                quick_sorting(alist,first,end-1)
                quick_sorting(alist,end+1,last)
                break



alist = [54,26,93,17,77,31,44,55,20]

quick_sorting(alist,0,len(alist) - 1 )

print alist

'''
OUTPUT:
[54, 26, 93, 17, 77, 31, 44, 55, 20]
[31, 26, 20, 17, 44, 54, 77, 55, 93]
[17, 26, 20, 31, 44, 54, 77, 55, 93]
[17, 26, 20, 31, 44, 54, 77, 55, 93]
[17, 20, 26, 31, 44, 54, 77, 55, 93]
[17, 20, 26, 31, 44, 54, 55, 77, 93]
'''

