# Given a sorted array of N integers, write a program to find the index of the last occurrence of the target key. If the target is not found then return -1.

# Note: Consider 0 based indexing

# Examples:

# Example 1:
# Input: N = 7, target=13, array[] = {3,4,13,13,13,20,40}
# Output: 4
# Explanation: As the target value is 13 , it appears for the first time at index number 2.

# Example 2:
# Input: N = 7, target=60, array[] = {3,4,13,13,13,20,40}
# Output: -1
# Explanation: Target value 60 is not present in the array
#NOTE : for last occurance 
def last(arr,n,target):
    low , high = 0 , n-1
    ans=n
    while low < high :
        mid = (low + high )//2
        if arr[mid]==target:
            ans = mid
            low = mid +1
        elif target < arr[mid]:
            high = mid -1
        else:
            low = mid +1
    return ans
#NOTE : for First Occurance , if we got the elemen the we will search in the left of that , it means hight = mid -1 (we have to shrink our limit to start - mid ) 

def first(arr,n , target):
    start , end = 0  , n-1
    result = n
    while start < end :
        mid = start + (end - start )/2
        if arr[mid] == target:
            ans = mid
            end = mid -1
        elif arr[mid] < target:
            start = mid +1
        else:
            end = mid -1
    return ans 


