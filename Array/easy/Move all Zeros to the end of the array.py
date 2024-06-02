# Problem Statement: You are given an array of integers, your task is to move all the zeros in the array to the end of the array and move non-negative integers to the front by maintaining their order.

# Examples
# Example 1:
# Input:
#  1 ,0 ,2 ,3 ,0 ,4 ,0 ,1
# Output:
#  1 ,2 ,3 ,4 ,1 ,0 ,0 ,0
# Explanation:
#  All the zeros are moved to the end and non-negative integers are moved to front by maintaining order

# Example 2:
# Input:
#  1,2,0,1,0,4,0
# Output:
#  1,2,1,4,0,0,0
# Explanation:
#  All the zeros are moved to the end and non-negative integers are moved to front by maintaining order
#NOTE: Approach is simple we take all the non zeros element and add to initial then just append 0 to the end
def moveZeros(arr):
    insert_pos=0
    for num in arr:
        if num!=0:
            arr[insert_pos] = num#we are putting non zero element in the initial points of array
            insert_pos+=1#  then we are increasing array pointer

    while insert_pos < len(arr): # we have to make sure our pointer doesn't cross the array length 
        arr[insert_pos]=0
        insert_pos+=1
    return arr
# Example usage:
arr1 = [1, 0, 2, 3, 0, 4, 0, 1]
print(moveZeros(arr1))  # Output: [1, 2, 3, 4, 1, 0, 0, 0]

arr2 = [1, 2, 0, 1, 0, 4, 0]
print(moveZeros(arr2))  # Output: [1, 2, 1, 4, 0, 0, 0]
