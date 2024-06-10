# Problem Statement: Given an integer array arr of size N, sorted in ascending order (with distinct values). Now the array is rotated between 1 to N times which is unknown. Find the minimum element in the array. 

# Pre-requisites: Search in Rotated Sorted Array I,  Search in Rotated Sorted Array II & Binary Search algorithm

# Examples
# Example 1:
# Input Format:
#  arr = [4,5,6,7,0,1,2,3]
# Result:
#  0
# Explanation:
#  Here, the element 0 is the minimum element in the array.

# Example 2:
# Input Format:
#  arr = [3,4,5,1,2]
# Result:
#  1
# Explanation:
#  Here, the element 1 is the minimum element in the array.

#NOTE: Minimum no postition is basically the no of times the array is rotated 
#we will divide the array in two parts one one is sorted and one is not sorted and after that we will imply binary search on that and find minimum in both and comapre and retrun the min

import sys
def findMin(arr: [int]):
    low = 0
    high = len(arr) - 1
    ans = sys.maxsize

    while low <= high:
        mid = (low + high) // 2

        # search space is already sorted
        # then arr[low] will always be
        # the minimum in that search space:
        if arr[low] <= arr[high]:
            ans = min(ans, arr[low])
            break
            
        if arr[low] <= arr[mid]:  # if left part is sorted
            ans = min(ans, arr[low])  # keep the minimum
            low = mid + 1  # eliminate left half

        else:  # if right part is sorted
            ans = min(ans, arr[mid])  # keep the minimum
            high = mid - 1  # eliminate right half

    return ans

if __name__ == "__main__":
    arr = [4, 5, 6, 7, 0, 1, 2, 3]
    ans = findMin(arr)
    print("The minimum element is:", ans)

# #practice
# while low <= high:
#     mid = start+end //2
#     if arr[low] <=arr[high]:
#         anas=min(anas,arr[low])
#         break
#     if arr[low] < arr[mid]:
#         anss= min(anas,arr[low])
#         low=mid+1
#     else:
#         anas=min(anss,arr[high])
#         high=mid-1
