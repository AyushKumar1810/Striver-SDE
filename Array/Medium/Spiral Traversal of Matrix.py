# Problem Statement: Given a Matrix, print the given matrix in spiral order.

# Examples:

# Example 1:
# Input: Matrix[][] = { { 1, 2, 3, 4 },
# 		      { 5, 6, 7, 8 },
# 		      { 9, 10, 11, 12 },
# 	              { 13, 14, 15, 16 } }

# Outhput: 1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10.
# Explanation: The output of matrix in spiral form.

# Example 2:
# Input: Matrix[][] = { { 1, 2, 3 },
# 	              { 4, 5, 6 },
# 		      { 7, 8, 9 } }
			    
# Output: 1, 2, 3, 6, 9, 8, 7, 4, 5.
# Explanation: The output of matrix in spiral form.

def printSpiral(mat):
    # Define ans array to store the result.
    ans = []
 
    n = len(mat) # no. of rows
    m = len(mat[0]) # no. of columns
  
    # Initialize the pointers reqd for traversal.
    top = 0
    left = 0
    bottom = n - 1
    right = m - 1

    # Loop until all elements are not traversed.
    while (top <= bottom and left <= right):
        # For moving left to right
        for i in range(left, right + 1):
            ans.append(mat[top][i])

        top += 1

        # For moving top to bottom.
        for i in range(top, bottom + 1):
            ans.append(mat[i][right])

        right -= 1

        # For moving right to left.
        if (top <= bottom):
            for i in range(right, left - 1, -1):
                ans.append(mat[bottom][i])

            bottom -= 1

        # For moving bottom to top.
        if (left <= right):
            for i in range(bottom, top - 1, -1):
                ans.append(mat[i][left])

            left += 1

    return ans

#Matrix initialization.
mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]
                     
ans = printSpiral(mat)

print(ans)

