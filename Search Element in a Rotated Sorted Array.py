# Problem Statement: Given an integer array arr of size N, sorted in ascending order (with distinct values) and a target value k. Now the array is rotated at some pivot point unknown to you. Find the index at which k is present and if k is not present return -1.

# Examples
# Example 1:
# Input Format: arr = [4,5,6,7,0,1,2,3], k = 0
# Result: 4
# Explanation: Here, the target is 0. We can see that 0 is present in the given rotated sorted array, nums. Thus, we get output as 4, which is the index at which 0 is present in the array.

# Example 2:
# Input Format: arr = [4,5,6,7,0,1,2], k = 3
# Result: -1
# Explanation: Here, the target is 3. Since 3 is not present in the given rotated sorted array. Thus, we get the output as -1.

#NOTE: we have 3 simple & Complex steps
# 1st : we will use Binary search on whole array
#2nd we will find the minimum element 
#3rd : we will use binary search on two parts one from low to min-1 and other from min to hight -1 
#NOTE : minimum elements is that element which is samllest to it's right and left Both {x>min<y} 

# Detailed Explanation:
# Initial Setup: Initialize two pointers, left and right, to the beginning and end of the array, respectively.
# Binary Search Loop: Continue the loop as long as left is less than or equal to right.
# Check Middle Element: Calculate the middle index and compare the middle element with the target.
# Determine Sorted Half:
# If the left part is sorted (arr[left] <= arr[mid]):
# Check if the target is within the range of the sorted left part (arr[left] <= target < arr[mid]).
# If yes, narrow the search to the left half (right = mid - 1).
# If no, search in the right half (left = mid + 1).
# If the right part is sorted (arr[mid] <= arr[right]):
# Check if the target is within the range of the sorted right part (arr[mid] < target <= arr[right]).
# If yes, narrow the search to the right half (left = mid + 1).
# If no, search in the left half (right = mid - 1).
# Element Found: If the target is found at the middle index, return the index.
# Element Not Found: If the loop ends without finding the target, return -1.
from typing import List


class Solution:
    def search(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == k:
                return mid
            
            # Determine if the left part is sorted
            if arr[left] <= arr[mid]:
                # Check if the target is in the left sorted part
                if arr[left] <= k < arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Otherwise, the right part must be sorted
            else:
                # Check if the target is in the right sorted part
                if arr[mid] < k <= arr[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1

# Example usage
sol = Solution()
print(sol.search([4, 5, 6, 7, 0, 1, 2, 3], 0))  # Expected output: 4
print(sol.search([4, 5, 6, 7, 0, 1, 2], 3))    # Expected output: -1
