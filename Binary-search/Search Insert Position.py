# Problem Statement: You are given a sorted array arr of distinct values and a target value x. You need to search for the index of the target value in the array.

# If the value is present in the array, then return its index. Otherwise, determine the index where it would be inserted in the array while maintaining the sorted order.

# Pre-requisite: Lower Bound & Binary Search

# Example 1:
# Input Format: arr[] = {1,2,4,7}, x = 6
# Result: 3
# Explanation: 6 is not present in the array. So, if we will insert 6 in the 3rd index(0-based indexing), the array will still be sorted. {1,2,4,6,7}.

# Example 2:
# Input Format: arr[] = {1,2,4,7}, x = 2
# Result: 1
# Explanation: 2 is present in the array and so we will return its index i.e. 1.
def searchInsert(arr: [int], x: int) -> int:
    n = len(arr)  # size of the array
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] >= x:
            ans = mid
            # look for smaller index on the left
            high = mid - 1
        else:
            low = mid + 1  # look on the right

    return ans

if __name__ == "__main__":
    arr = [1, 2, 4, 7]
    x = 6
    ind = searchInsert(arr, x)
    print("The index is:", ind)