# Problem Statement: Given an array of integers and an integer k, return the total number of subarrays whose sum equals k.

# A subarray is a contiguous non-empty sequence of elements within an array.

# Pre-requisite: Longest subarray with given sum

# Examples
# Example 1:
# Input Format:
#  N = 4, array[] = {3, 1, 2, 4}, k = 6
# Result:
#  2
# Explanation:
#  The subarrays that sum up to 6 are [3, 1, 2] and [2, 4].

# Example 2:
# Input Format:
#  N = 3, array[] = {1,2,3}, k = 3
# Result:
#  2
# Explanation:
#  The subarrays that sum up to 3 are [1, 2], and [3].

from collections import defaultdict

def findAllSubarraysWithGivenSum(arr, k):
    n = len(arr) # size of the given array.
    mpp = defaultdict(int)
    preSum = 0
    cnt = 0

    mpp[0] = 1 # Setting 0 in the map.
    for i in range(n):
        # add current element to prefix Sum:
        preSum += arr[i]

        # Calculate x-k:
        remove = preSum - k

        # Add the number of subarrays to be removed:
        cnt += mpp[remove]

        # Update the count of prefix sum
        # in the map.
        mpp[preSum] += 1

    return cnt


if __name__ == '__main__':
    arr = [3, 1, 2, 4]
    k = 6
    cnt = findAllSubarraysWithGivenSum(arr, k)
    print("The number of subarrays is:", cnt)