# Problem Statement: Given an array and a sum k, we need to print the length of the longest subarray that sums to k.

# Examples
# Example 1:
# Input Format:
#  N = 3, k = 5, array[] = {2,3,5}
# Result:
#  2
# Explanation:
#  The longest subarray with sum 5 is {2, 3}. And its length is 2.

# Example 2:
# Input Format
# : N = 3, k = 1, array[] = {-1, 1, 1}
# Result:
#  3
# Explanation:
#  The longest subarray with sum 1 is {-1, 1, 1}. And its length is 3.

#NOTE : As it contains negative so we can't use two Pointers approach so we have to use hashMap
def getLongestSubarray(a,k):
    n = len(a) # size of the array.

    preSumMap = {}
    Sum = 0
    maxLen = 0
    for i in range(n):
        # calculate the prefix sum till index i:
        Sum += a[i]

        # if the sum = k, update the maxLen:
        if Sum == k:
            maxLen = max(maxLen, i + 1)

        # calculate the sum of remaining part i.e. x-k:
        rem = Sum - k

        # Calculate the length and update maxLen:
        if rem in preSumMap:
            length = i - preSumMap[rem]
            maxLen = max(maxLen, length)

        # Finally, update the map checking the conditions:
        if Sum not in preSumMap:
            preSumMap[Sum] = i

    return maxLen

if __name__ == "__main__":
    a = [-1, 1, 1]
    k = 1
    length = getLongestSubarray(a, k)
    print(f"The length of the longest subarray is: {length}")
