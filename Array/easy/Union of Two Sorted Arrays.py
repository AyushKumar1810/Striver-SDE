# Problem Statement: Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.

# The union of two arrays can be defined as the common and distinct elements in the two arrays.NOTE: Elements in the union should be in ascending order.

# Examples
# Example 1:
# Input:

# n = 5,m = 5.
# arr1[] = {1,2,3,4,5}  
# arr2[] = {2,3,4,4,5}
# Output:

#  {1,2,3,4,5}

# Explanation: 

# Common Elements in arr1 and arr2  are:  2,3,4,5
# Distnict Elements in arr1 are : 1
# Distnict Elemennts in arr2 are : No distinct elements.
# Union of arr1 and arr2 is {1,2,3,4,5} 

# Example 2:
# Input:

# n = 10,m = 7.
# arr1[] = {1,2,3,4,5,6,7,8,9,10}
# arr2[] = {2,3,4,4,5,11,12}
# Output:
#  {1,2,3,4,5,6,7,8,9,10,11,12}
# Explanation:
 
# Common Elements in arr1 and arr2  are:  2,3,4,5
# Distnict Elements in arr1 are : 1,6,7,8,9,10
# Distnict Elemennts in arr2 are : 11,12
# Union of arr1 and arr2 is {1,2,3,4,5,6,7,8,9,10,11,12} 

def union_sorted_arrays(arr1, arr2):
    n,m = len(arr1) , len(arr2)
    i , j = 0 , 0 
    result = []
    while i < n and j < m :
        # Skip duplicates in arr1
        while i > 0 and i < n and  arr1[i]==arr1[i-1]:
            i+=1
         # Skip duplicates in arr2
        while j > 0 and j < m and arr2[j] == arr2[j-1]:
            j+=1

        if i < n and j < m:
            if arr1[i] < arr2[j]:
                result.append(arr1[i])
                i+=1
            elif arr1[i] > arr2[j]:
                result.append(arr2[j])
                j+=1
            else :
                result.append(arr1[i])

        while i < n :
            if i > 0 and arr1[i]!=arr1[i-1]:
                result.append(arr1[i])
            i+=1
        while j < m:
            if j > 0 and arr2[j] != arr2[j - 1]:
                result.append(arr2[j])
            j += 1
    return result
# Example usage:
arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 3, 4, 4, 5]
print(union_sorted_arrays(arr1, arr2))  # Output: [1, 2, 3, 4, 5]

arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]
print(union_sorted_arrays(arr1, arr2))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
