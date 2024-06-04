# Problem Statement: Given an integer array arr, find the contiguous subarray (containing at least one number) which
# has the largest sum and returns its sum and prints the subarray.

# Examples
# Example 1:
# Input:
#  arr = [-2,1,-3,4,-1,2,1,-5,4] 
# Output:
#  6 

# Explanation:
#  [4,-1,2,1] has the largest sum = 6. 

# Examples 2:
# Input:
#  arr = [1] 

# Output:
#  1 

# Explanation:
#  Array has only one element and which is giving positive sum of 1. 
#NOTE :simple we will use Sliding window concepts 
import sys

def maxSubarraySum(arr, n):
    maxi = -sys.maxsize-1 # maximum sum
    sum=0
    for i in range(n):
        sum+=arr[i]
        if sum>maxi:
            maxi = sum
        if sum <0 :
            sum=0
    return maxi
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(arr)
maxSum = maxSubarraySum(arr, n)
print("The maximum subarray sum is:", maxSum)


# import sys

# def maxSubarraySum(arr, n):
#     maxi = -sys.maxsize-1 # maximum sum
#     sum = 0
#     for i in range(n):
#         sum +=arr[i]
#         if sum > maxi:
#             maxi=sum
#         if sum < 0:
#             sum =0
#     return maxi