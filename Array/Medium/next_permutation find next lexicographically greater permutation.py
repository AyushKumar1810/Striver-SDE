# Problem Statement: Given an array Arr[] of integers, rearrange the numbers of the given array into the lexicographically next greater permutation of numbers.

# If such an arrangement is not possible, it must rearrange to the lowest possible order (i.e., sorted in ascending order).

# Examples
# Example 1 :

# Input format:
#  Arr[] = {1,3,2}
# Output
# : Arr[] = {2,1,3}
# Explanation: 
# All permutations of {1,2,3} are {{1,2,3} , {1,3,2}, {2,1,3} , {2,3,1} , {3,1,2} , {3,2,1}}. So, the next permutation just after {1,3,2} is {2,1,3}.
# Example 2:

# Input format:
#  Arr[] = {3,2,1}
# Output: 
# Arr[] = {1,2,3}
# Explanation: 
# # As we see all permutations of {1,2,3}, we find {3,2,1} at the last position. So, we have to return the topmost permutation.

def next_permutation(arr):
    # Find the first element from the right such that arr[i] > arr[i-1]
    i = len(arr) - 1
    while i > 0 and arr[i] <= arr[i - 1]:
        i -= 1

    # If no such element is found, reverse the array
    if i == 0:
        arr.reverse()
        return arr

    # Find the smallest element to the right of arr[i-1] that is greater than arr[i-1]
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1

    # Swap arr[i-1] and arr[j]
    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    # Sort the subarray to the right of arr[i-1] in ascending order
    arr[i:] = sorted(arr[i:])

    return arr

# Example usage:
arr1 = [1, 3, 2]
arr2 = [3, 2, 1]

print("Next permutation of", arr1, ":", next_permutation(arr1))
print("Next permutation of", arr2, ":", next_permutation(arr2))
