# Problem Statement: You are given a strictly increasing array ‘vec’ and a positive integer 'k'. Find the 'kth' positive integer missing from 'vec'.

# Examples
# Example 1:
# Input Format:
#  vec[]={4,7,9,10}, k = 1
# Result:
#  1
# Explanation:
#  The missing numbers are 1, 2, 3, 5, 6, 8, 11, 12, ……, and so on. Since 'k' is 1, the first missing element is 1.
# Example 2:
# Input Format:
#  vec[]={4,7,9,10}, k = 4
# Result:
#  5
# Explanation:
#  The missing numbers are 1, 2, 3, 5, 6, 8, 11, 12, ……, and so on. Since 'k' is 4, the fourth missing element is 5.

#NOTE: we have to go through (1,inf) then we will take union of the given array with that and we will return the reaminaing value and we will resturn it's kth index value
def missingK(vec, n, k):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        missing = vec[mid] - (mid + 1)
        if missing < k:
            low = mid + 1
        else:
            high = mid - 1
    return k + high + 1

vec = [4, 7, 9, 10]
n = 4
k = 4
ans = missingK(vec, n, k)
print("The missing number is:", ans)

#Practice
def missingK(arr, n, k):
    low , high = 0 , n-1
    while low <= high:
        mid =( low + high )//2
        missing_num = arr[mid] - mid-1
        if missing_num < k:
            low=mid+1
        else:
            high = mid -1
    return high + k +1
arr = [4, 7, 9, 10]
n = 4
k = 4
ans = missingK(vec, n, k)
print("The missing number is:", ans)

