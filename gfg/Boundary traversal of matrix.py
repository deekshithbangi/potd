'''
You are given a matrix of dimensions n x m. The task is to perform boundary traversal on the matrix in a clockwise manner.

Example 1:

Input:
n = 4, m = 4
matrix[][] = {{1, 2, 3, 4},
         {5, 6, 7, 8},
         {9, 10, 11, 12},
         {13, 14, 15,16}}
Output: 1 2 3 4 8 12 16 15 14 13 9 5
Explanation:
The matrix is:
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
The boundary traversal is:
1 2 3 4 8 12 16 15 14 13 9 5
'''

class Solution:
    
    #Function to return list of integers that form the boundary 
    #traversal of the matrix in a clockwise manner.
    def BoundaryTraversal(self,matrix, n, m):
        a = [] 
        if n>0 and m>0:
            for col in range(m):
                a.append(matrix[0][col]) 
            for row in range(1,n):
                a.append(matrix[row][m-1]) 
            if n>1:
                for col in range(m-2,-1,-1):
                    a.append(matrix[n-1][col])
            if m>1:
                for row in range(n-2,0,-1):
                    a.append(matrix[row][0])
        return a