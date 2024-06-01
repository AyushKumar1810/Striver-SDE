# Problem Statement: Given an array of N integers, left rotate the array by one place.

# Examples
# Example 1:
# Input:
#  N = 5, array[] = {1,2,3,4,5}
# Output:
#  2,3,4,5,1
# Explanation:
 
# Since all the elements in array will be shifted 
# toward left by one so ‘2’ will now become the 
# first index and and ‘1’ which was present at 
# first index will be shifted at last.


# Example 2:
# Input:
#  N = 1, array[] = {3}
# Output:
#  3
# Explanation:
#  Here only element is present and so 
# the element at first index will be shifted to 
# last index which is also by the way the first index.
#NOTE : just put 0th index to the last index for that we need to store 0th element to some temporeial variable and last index we have to add to the temp

def solve(arr, n):
    temp=arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp
    for i in range(n):
        print(arr[i] , end = " ")
n = 5
arr = [1, 2, 3, 4, 5]
solve(arr, n)