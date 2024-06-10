# Search Element in Rotated Sorted Array II

# Problem Statement: Given an integer array arr of size N, sorted in ascending order (may contain duplicate values) and a target value k. Now the array is rotated at some pivot point unknown to you. Return True if k is present and otherwise, return False. 

# Pre-requisite: Search Element in Rotated Sorted Array I & Binary Search algorithm

# Examples
# Example 1:
# Input Format:
#  arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 3
# Result:
#  True
# Explanation:
#  The element 3 is present in the array. So, the answer is True.

# Example 2:
# Input Format:
#  arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 10
# Result:
#  False
# Explanation:
#  The element 10 is not present in the array. So, the answer is False.

#NOTE:Approach:
# Binary Search: Use binary search to divide the array into two halves.
# Identify Sorted Part: Determine which part (left or right) of the array is sorted.
# Handle Duplicates: If there are duplicates, it might be tricky to determine the sorted part. We handle this by adjusting the pointers when duplicates are found.
# Narrow Down Search: Decide where to search next based on the sorted part and the target value.
# Detailed Steps:
# Initial Setup: Initialize two pointers, left and right, to the beginning and end of the array.
# Binary Search Loop: Continue the loop as long as left is less than or equal to right.
# Check Middle Element: Calculate the middle index and compare the middle element with the target.
# Handle Duplicates: If the elements at left, mid, and right are equal, increment left and decrement right to skip the duplicates.
# Determine Sorted Half:
# If the left part is sorted (arr[left] <= arr[mid]):
# Check if the target is within the range of the sorted left part (arr[left] <= target < arr[mid]).
# If yes, narrow the search to the left half (right = mid - 1).
# If no, search in the right half (left = mid + 1).
# If the right part is sorted (arr[mid] <= arr[right]):
# Check if the target is within the range of the sorted right part (arr[mid] < target <= arr[right]).
# If yes, narrow the search to the right half (left = mid + 1).
# If no, search in the left half (right = mid - 1).
# Element Found: If the target is found at the middle index, return True.
# Element Not Found: If the loop ends without finding the target, return False.

from typing import List

def search_rotated_array(arr: List[int], k: int) -> bool:
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == k:
            return True
        
        # Handle duplicates: skip them
        if arr[left] == arr[mid] == arr[right]:
            left += 1
            right -= 1
        # Left part is sorted
        elif arr[left] <= arr[mid]:
            if arr[left] <= k < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right part is sorted
        else:
            if arr[mid] < k <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return False

# Example usage
print(search_rotated_array([7, 8, 1, 2, 3, 3, 3, 4, 5, 6], 3))  # Expected output: True
print(search_rotated_array([7, 8, 1, 2, 3, 3, 3, 4, 5, 6], 10))  # Expected output: False
