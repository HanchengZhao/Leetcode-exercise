def leftmostColWith1(matrix):
    if len(matrix) == 0:
        return -1 # not exist
    leftmost = len(matrix[0]) # default value to check whether 1 exists
    row, col = len(matrix)-1, len(matrix[0])-1 # row and col number
    for i in xrange(row, -1, -1): # start from the bottom right
        while col >= 0 and matrix[i][col] == 1:
            leftmost = min(leftmost, col)
            col -= 1
    return leftmost if leftmost != len(matrix[0]) else -1

print leftmostColWith1([[0,1,1,1,1],
                        [1,1,1,1,1],
                        [0,0,1,1,1],
                        [0,0,0,1,1]]) # 1
print leftmostColWith1([[0,0,0,0,0]]) # -1

