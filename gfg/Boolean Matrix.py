'''
Given a boolean matrix of size RxC where each cell contains either 0 or 1, 
modify it such that if a matrix cell matrix[i][j] is 1 then all the cells in its ith row and jth column will become 1.
Input:
R = 4, C = 3
matrix[][] = {{ 1, 0, 0},
              { 1, 0, 0},
              { 1, 0, 0},
              { 0, 0, 0}}
Output: 
1 1 1
1 1 1
1 1 1
1 0 0 
Explanation:
The position of cells that have 1 in
the original matrix are (0,0), (1,0)
and (2,0). Therefore, all cells in row
0,1,2 are and column 0 are modified to 1.
'''

def booleanMatrix(matrix):
    rows, columns = len(matrix), len(matrix[0])
    rows_to_change = set()
    columns_to_change = set()

    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == 1:
                rows_to_change.add(i)
                columns_to_change.add(j)

    for row in rows_to_change:
        matrix[row] = [1] * columns

    for column in columns_to_change:
        for i in range(rows):
            matrix[i][column] = 1
                
