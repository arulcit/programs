grid = [['A', 'F', 'H', 'D', 'T', 'K', 'G', 'E', 'P', 'G'],
        ['G', 'R', 'E', 'E', 'N', 'G', 'R', 'E', 'E', 'N'],
        ['U', 'R', 'G', 'E', 'P', 'R', 'E', 'K', 'W', 'E'],
        ['P', 'Q', 'R', 'A', 'C', 'E', 'E', 'P', 'W', 'E'],
        ['U', 'A', 'F', 'J', 'T', 'E', 'N', 'P', 'Q', 'N'],
        ['P', 'Q', 'U', 'S', 'N', 'N', 'A', 'Z', 'X', 'V']]

input = "GREEN"

import re

def find_letter_in_matrix(grid, input1):
    row_length = len(grid)
    match_list = []

    for iindex in xrange(row_length):
        each_row = grid[iindex]
        each_row_string = "".join(each_row)  
        search_each_row = re.finditer(input1, each_row_string) #useful logic to remember - re.finditer()
        for each_match in search_each_row:
            match_list.append((iindex,each_match.start()))
            print "Matched row and column is %d,%d" % (iindex,each_match.start())

    for row2, i in enumerate(zip(*grid)): #useful logic to remember - zip
        each_column1 = "".join(i)  
        search_column = re.finditer(input1, each_column1)
        for each_column in search_column:
            match_list.append((each_column.start(),row2))
            print "Matched row and column is %d,%d" % (each_column.start(),row2)

    return match_list

print find_letter_in_matrix(grid,input)

'''
Output:
Matched row and column is 1,0
Matched row and column is 1,5
Matched row and column is 1,5
Matched row and column is 0,6
[(1, 0), (1, 5), (1, 5), (0, 6)]
'''

