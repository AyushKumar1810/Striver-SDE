# 96. Unique Binary Search Trees

# Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

 

# Example 1:


# Input: n = 3
# Output: 5
# Example 2:

# Input: n = 1
# Output: 1

#NOTE:#* we can use recussion to find no of binary tree with "n" nodes and we will initialise with a counter , count which will be updated we will return the count

#* Here the thing is that if "n" is the total nodes the on the left i-1 ( we are taking loop in 2 to n ) so i will be root then i-1 will be no of left nodes and n-1 will ne bo node in right tree for example : if i=4 then no of left node =3 and no of right will be n-i
def numTrees(n):
    if n==0:
        return 1
    if n==1:
        return 1
    dp=[0]*(n+1)
    dp[0]=1
    dp[1]=1
    for i in range(2,n+1):
        for j in range(1,i+1):
            dp[i]+=dp[j-1]*dp[i-j]
    return dp[n]
