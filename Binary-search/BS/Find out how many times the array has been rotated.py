# Problem Statement: Given an integer array arr of size N, sorted in ascending order (with distinct values). Now the array is rotated between 1 to N times which is unknown. Find how many times the array has been rotated. 

# Pre-requisites: Find minimum in Rotated Sorted Array,  Search in Rotated Sorted Array II & Binary Search algorithm

# Examples
# Example 1:
# Input Format:
#  arr = [4,5,6,7,0,1,2,3]
# Result:
#  4
# Explanation:
#  The original array should be [0,1,2,3,4,5,6,7]. So, we can notice that the array has been rotated 4 times.

# Example 2:
# Input Format:
#  arr = [3,4,5,1,2]
# Result:
#  3
# Explanation:
#  The original array should be [1,2,3,4,5]. So, we can notice that the array has been rotated 3 times.
#NOTE: The approach is very simple You just have to find the minimum element in that array and retrun the index that will be the "No of times The array has been rotated"

import sys
def findKRotation(arr : [int]) -> int: # type: ignore
    low = 0
    high = len(arr) - 1
    ans = float('inf')
    index = -1
    while low <= high:
        mid = (low + high) // 2

        # If search space is already sorted,
        # then arr[low] will always be
        # the minimum in that search space
        if arr[low] <= arr[high]:
            if arr[low] < ans:
                index = low
                ans = arr[low]
            break

        # If left part is sorted
        if arr[low] <= arr[mid]:
            # Keep the minimum
            if arr[low] < ans:
                index = low
                ans = arr[low]

            # Eliminate left half
            low = mid + 1
        else:  # If right part is sorted
            # Keep the minimum
            if arr[mid] < ans:
                index = mid
                ans = arr[mid]

            # Eliminate right half
            high = mid - 1

    return index
if __name__ == "__main__":
    arr = [4, 5, 6, 7, 0, 1, 2, 3]
    ans = findKRotation(arr)
    print("The array is rotated", ans, "times.")
    print(ans)
