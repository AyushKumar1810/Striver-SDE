# Problem Statement: Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and then return the matrix.

# Examples
# Examples 1:
# Input:
#  matrix=[[1,1,1],[1,0,1],[1,1,1]]

# Output:
#  [[1,0,1],[0,0,0],[1,0,1]]

# Explanation:
#  Since matrix[2][2]=0.Therfore the 2nd column and 2nd row wil be set to 0.
 
# Input:
#  matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]

# Output:
# [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

# Explanation:
# Since matrix[0][0]=0 and matrix[0][3]=0. Therefore 1st row, 1st column and 4th column will be set to 0

#NOTE:we are making a two hash map row , col , if we found 0 then we will mark that row and col hashmap value to 1 and we will contunue and after that we will re itterate and go to it and when we wfind 1 in col or 1 in row hashmap we will make it all col or row to 0 ..
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        Rows=[0]*rows
        Cols=[0]*cols
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    Rows[i]=1
                    Cols[j]=1
        for i in range(rows):
            for j in range(cols):
                if Rows[i] or Cols[j]:
                    matrix[i][j]=0
        return matrix
