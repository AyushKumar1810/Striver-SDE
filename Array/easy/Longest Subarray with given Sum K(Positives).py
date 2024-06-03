# Problem Statement: Given an array and a sum k, we need to print the length of the longest subarray that sums to k.

# Examples
# Example 1:
# Input Format: N = 3, k = 5, array[] = {2,3,5}
# Result: 2
# Explanation: The longest subarray with sum 5 is {2, 3}. And its length is 2.

# Example 2:
# Input Format: N = 5, k = 10, array[] = {2,3,5,1,9}
# Result: 3
# Explanation: The longest subarray with sum 10 is {2, 3, 5}. And its length is 3.
def getLongestSubarray(a,k):
    n= len(a)
    left , right = 0 , 0 
    sum = a[0]
    max_Len=0
    while right < n :
        while left <=right and sum > k :
            sum= sum - a[left]
            left = left +1
        if sum ==k:
            max_Len = max(max_Len , right - left +1)
        right = right +1 
        if right < n :sum= sum + a[right]
    return max_Len
if __name__ == "__main__":
	a = [2, 3, 5, 1, 9]
	k = 10

	length = getLongestSubarray(a, k)
	print(f"The length of the longest subarray is: {length}")

