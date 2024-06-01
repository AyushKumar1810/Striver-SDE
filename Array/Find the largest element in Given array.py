# Problem Statement: Given an array, we have to find the largest element in the array.

# Examples
# Example 1:
# Input:
#  arr[] = {2,5,1,3,0};
# Output:
#  5
# Explanation:
#  5 is the largest element in the array. 

# Example2:
# Input:
#  arr[] = {8,10,5,7,9};
# Output:
#  10
# Explanation:
#  10 is the largest element in the array. 

#1:Brute Force Space Complexity: O(N)
#NOTE: sort the array and return the last element 😁
def Largest (arr):
    arr.sort()
    return arr[-1]
arr1 = [2, 5, 1, 3, 0]
arr2 = [8, 10, 5, 7, 9]
print("the largest element in the array is :" , Largest(arr1))
print("the largest element in the array is :" , Largest(arr2))

#2: using Max O(1) space complexivity
#NOTE: create a max array which will be 1st element(0th index) we will compared max with i+1 if it's greater then we will update otherwise not
def findLargestElement(arr, n):
    max=arr[0]
    for i in range(n):
        if max < arr[i]:
            max=arr[i]
    return max
arr1 = [2, 5, 1, 3, 0]
n = 5
max = findLargestElement(arr1, n)
print("The largest element in the array is:", max)


arr2 = [8, 10, 5, 7, 9]
n = 5
max = findLargestElement(arr2, n)
print("The largest element in the array is:", max)


