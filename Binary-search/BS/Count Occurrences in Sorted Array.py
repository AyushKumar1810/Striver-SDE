# Count Occurrences in Sorted Array

# Problem Statement: You are given a sorted array containing N integers and a number X, you have to find the occurrences of X in the given array.

# Examples
# Example 1:
# Input:
#  N = 7,  X = 3 , array[] = {2, 2 , 3 , 3 , 3 , 3 , 4}
# Output
# : 4
# Explanation:
#  3 is occurring 4 times in 
# the given array so it is our answer.

# Example 2:
# Input:
#  N = 8,  X = 2 , array[] = {1, 1, 2, 2, 2, 2, 2, 3}
# Output
# : 5
# Explanation:
#  2 is occurring 5 times in the given array so it is our answer.

#NOTE : Approach is very very simple find last occurance and the 1st occrance then subtract last - first then return it last-first  + 1 

def firstOccurrence(arr, n, k):
    low = 0
    high = n - 1
    first = -1

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] == k:
            first = mid
            # look for smaller index on the left
            high = mid - 1
        elif arr[mid] < k:
            low = mid + 1  # look on the right
        else:
            high = mid - 1  # look on the left

    return first


def lastOccurrence(arr, n, k):
    low = 0
    high = n - 1
    last = -1

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] == k:
            last = mid
            # look for larger index on the right
            low = mid + 1
        elif arr[mid] < k:
            low = mid + 1  # look on the right
        else:
            high = mid - 1  # look on the left

    return last


def firstAndLastPosition(arr, n, k):
    first = firstOccurrence(arr, n, k)
    if first == -1:
        return (-1, -1)
    last = lastOccurrence(arr, n, k)
    return (first, last)

def count(arr: [int], n: int, x: int) -> int:
    first, last = firstAndLastPosition(arr, n, x)
    if first == -1:
        return 0
    return last - first + 1

if __name__ == "__main__":
    arr = [2, 4, 6, 8, 8, 8, 11, 13]
    n = 8
    x = 8
    ans = count(arr, n, x)
    print("The number of occurrences is:", ans)