# Problem Statement: Given an array of N integers. Every number in the array except one appears twice. Find the single number in the array.

# Pre-requisite: Binary Search Algorithm

# Examples
# Example 1:
# Input Format:
#  arr[] = {1,1,2,2,3,3,4,5,5,6,6}
# Result:
#  4
# Explanation:
#  Only the number 4 appears once in the array.

# Example 2:
# Input Format:
#  arr[] = {1,1,3,5,5}
# Result:
#  3
# Explanation:
#  Only the number 3 appears once in the array.

#NOTE:
# Algorithm:
# The steps are as follows:

# If n == 1: This means the array size is 1. If the array contains only one element, we will return that element only.
# If arr[0] != arr[1]: This means the very first element of the array is the single element. So, we will return arr[0].
# If arr[n-1] != arr[n-2]: This means the last element of the array is the single element. So, we will return arr[n-1].
# Place the 2 pointers i.e. low and high: Initially, we will place the pointers excluding index 0 and n-1 like this: low will point to index 1, and high will point to index n-2 i.e. the second last index.
# Calculate the ‘mid’: Now, inside a loop, we will calculate the value of ‘mid’ using the following formula:
# mid = (low+high) // 2 ( ‘//’ refers to integer division)
# Check if arr[mid] is the single element:
# If arr[mid] != arr[mid-1] and arr[mid] != arr[mid+1]: If this condition is true for arr[mid], we can conclude arr[mid] is the single element. We will return arr[mid].
# If (mid % 2 == 0 and arr[mid] == arr[mid+1])
# or (mid%2 == 1 and arr[mid] == arr[mid-1]): This means we are in the left half and we should eliminate it as our single element appears on the right. So, we will do this:
# low = mid+1.
# Otherwise, we are in the right half and we should eliminate it as our single element appears on the left. So, we will do this: high = mid-1.

from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # # num_count={} # we are taking hashmap to count no of time digits repeated 
        # # for num in nums :
        # #     if num in num_count:
        # #         num_count[num]+=1 # If we found duplicate then we will increase it's count
        # #     else :
        # #         num_count[num]=1 # If not Remains 1 
        # # for num , count in num_count.items(): # If count is 1 then return that value 
        # #     if count==1:
        # #         return num
# Now for efficient solution we shall solve it with using Binary to get time complexivity of O(Log(n))
        left , right = 0 , len(nums)-1
        while left  < right :
            mid = left + (right-left)//2
            if mid %2==1:
                mid -=1
            if nums[mid]!=nums[mid+1]:
                right=mid
            else :
                left = mid +2

        return nums[left]
    

def singleNonDuplicate(arr):
    n = len(arr)  # Size of the array

    # Edge cases:
    if n == 1:
        return arr[0]
    if arr[0] != arr[1]:
        return arr[0]
    if arr[n - 1] != arr[n - 2]:
        return arr[n - 1]

    low = 1
    high = n - 2
    while low <= high:
        mid = (low + high) // 2

        # If arr[mid] is the single element:
        if arr[mid] != arr[mid + 1] and arr[mid] != arr[mid - 1]:
            return arr[mid]

        # We are in the left:
        if (mid % 2 == 1 and arr[mid] == arr[mid - 1]) or (mid % 2 == 0 and arr[mid] == arr[mid + 1]):
            # Eliminate the left half:
            low = mid + 1
        # We are in the right:
        else:
            # Eliminate the right half:
            high = mid - 1

    # Dummy return statement:
    return -1

arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
ans = singleNonDuplicate(arr)
print("The single element is:", ans)