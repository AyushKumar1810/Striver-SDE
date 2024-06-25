# Given a triangle array, return the minimum path sum from top to bottom.

# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

 

# Example 1:

# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
# Example 2:

# Input: triangle = [[-10]]
# Output: -10
 

# Constraints:

# 1 <= triangle.length <= 200
# triangle[0].length == 1
# triangle[i].length == triangle[i - 1].length + 1
# -104 <= triangle[i][j] <= 104
 

# Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?
#NOTE:#! we can use DFS(level order traversal) and find the min element in each level and we will add them to get result 
def minimumTotal(triangle):
    if not triangle:
        return 0

    # Iterate from the second to last row to the first row
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            # Update the current element to the minimum path sum
            triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])

    # The result is the top element of the triangle
    return triangle[0][0]

# Example usage:
triangle1 = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(minimumTotal(triangle1))  # Output: 11

triangle2 = [[-10]]
print(minimumTotal(triangle2))  # Output: -10

#NOTE: the above will be not efficient , so we will use dp
def minimumTotal(triangle):
    dp=[0]*(len(triangle)+1)
    for row in triangle[::-1]:
        for i , n in enumerate(row):
            dp[i]= n + min(dp[i] , dp[i+1])
        return dp[0]