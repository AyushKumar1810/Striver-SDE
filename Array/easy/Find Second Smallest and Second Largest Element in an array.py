# Find Second Smallest and Second Largest Element in an array
# Problem Statement: Given an array, find the second smallest and second largest element in the array. Print ‘-1’ in the event that either of them doesn’t exist.

# Examples
# Example 1:
# Input:
#  [1,2,4,7,7,5]
# Output:
#  Second Smallest : 2
# 	Second Largest : 5
# Explanation:
#  The elements are as follows 1,2,3,5,7,7 and hence second largest of these is 5 and second smallest is 2

# Example 2:
# Input:
#  [1]
# Output:
#  Second Smallest : -1
# 	Second Largest : -1
# Explanation:
#  Since there is only one element in the array, it is the largest and smallest element present in the array. There is no second largest or second smallest element present.

#NOTE: The noraml / Brute force approach will be sort the array for 2nd largest return 2nd last elements and for 2nd smallest Return 2nd element of the array But it will be not efficient 😁
#NOTE 1 : the better Approach will be take largest/ samllest and comapre wityh each arr[i] if it's less than it then we should return it and if differnce is low then it is 2nd smallest/2nd largst

def getElements(arr, n):
    if n==0 or n==1:
        print(-1,-1)
    small = float('inf')
    second_small=float('inf')
    large=float('-inf')
    second_large=float('-inf')
    for i in range(n): #that is 1st iteration for finding largest and smallest
        small=min(small,arr[i])
        large=max(large,arr[i])
    for i in range(n):# 2nd iteration for finding second_lagest/second_smallest
        if arr[i] < second_small and arr[i]!=small:
            second_small=arr[i]
        if arr[i] > second_large and arr[i]!=large:
            second_large=arr[i]
    print("Second smallest is", second_small)
    print("Second largest is", second_large)
arr = [1, 2, 4, 6, 7, 5]
n = len(arr)
getElements(arr, n)
#Time-O(2N)

#NOTE : Best Approach (In one Go)
def secondSmallest(arr, n):
    if (n < 2):
        return -1
    small = float('inf')
    second_small = float('inf')
    for i in range(n):
        if (arr[i] < small):
            second_small = small
            small = arr[i]
        elif (arr[i] < second_small and arr[i] != small):
            second_small = arr[i]
    return second_small




def secondLargest(arr, n):
    if (n < 2):
        return -1
    large = float('-inf')
    second_large = float('-inf')
    for i in range(n):
        if (arr[i] > large):
            second_large = large
            large = arr[i]
        elif (arr[i] > second_large and arr[i] != large):
            second_large = arr[i]
    return second_large




arr = [1, 2, 4, 7, 7, 5]
n = len(arr)
sS = secondSmallest(arr, n)
sL = secondLargest(arr, n)
print("Second smallest is", sS)
print("Second largest is", sL)
