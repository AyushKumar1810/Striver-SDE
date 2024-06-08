# Problem Statement: Given a sorted array of N integers and an integer x, write a program to find the upper bound of x.

# Pre-requisite: Binary Search algorithm

# Examples
# Example 1:
# Input Format:
#  N = 4, arr[] = {1,2,2,3}, x = 2
# Result:
#  3
# Explanation:
#  Index 3 is the smallest index such that arr[3] > x.

# Example 2:
# Input Format:
#  N = 6, arr[] = {3,5,8,9,15,19}, x = 9
# Result:
#  4
# Explanation:
#  Index 4 is the smallest index such that arr[4] > x.

def upper(arr,n,x):
    low,high = 0 , n-1
    ans = n
    while low < high :
        mid = (low + high) //2
        if arr[mid] > x :
            ans = mid
            high = mid-1
        else:
            low = mid +1
    return ans
arr = [3, 5, 8, 9, 15, 19]
n = 6
x = 9
ind = upper(arr, n, x)
print("The upper bound is the index:", ind)