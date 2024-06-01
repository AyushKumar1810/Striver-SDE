# Example 1:
# Input:
#  N = 5, array[] = {1,2,3,4,5}
# Output
# : True.
# Explanation:
#  The given array is sorted i.e Every element in the array is smaller than or equals to its next values, So the answer is True.Example 2:
# Input:
#  N = 5, array[] = {5,4,6,7,8}
# Output
# : False.
# Explanation:
#  The given array is Not sorted i.e Every element in the array is not smaller than or equal to its next values, So the answer is False.

# Here element 5 is not smaller than or equal to its future elements.
#NOTE: just take array and iterate it and  sort it and then again iterate then sorted one . so we will check if arr[i]!=sorted_array[j] then we will simply return false as the sorted array is not similar so orignal array is not sorted , But will take Time of O(N^2)

#NOTE: for better approac we can iterate one time Given aray and we will check arr[i] < arr[i-1] (that means 1st index is smaller than 0th index ) that is not the case in sorted array in ascending order

def isSorted(arr, n):
    for i in range(1,n):
        if arr[i] < arr[i - 1]:
            return False
    return True

arr = [1, 2, 3, 4, 5]
n = 5
print("True" if isSorted(arr, n) else "False")
