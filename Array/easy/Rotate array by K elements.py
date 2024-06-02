# Rotate array by K elements

# Problem Statement: Given an array of integers, rotating array of elements by k elements either left or right.

# Examples:

# Example 1:
# Input: N = 7, array[] = {1,2,3,4,5,6,7} , k=2 , right
# Output: 6 7 1 2 3 4 5
# Explanation: array is rotated to right by 2 position .

# Example 2:
# Input: N = 6, array[] = {3,7,8,9,10,11} , k=3 , left 
# Output: 9 10 11 3 7 8
# Explanation: Array is rotated to right by 3 position.

def rotate_array(arr, k, direction):
    n=len(arr)
    k=k%n
    if direction=="right":
        return arr[-k:] + arr[:k]
    elif direction == "left":
        return arr[k:] + arr[:k]
    else :
        return arr
# Example usage for right rotation
arr1 = [1, 2, 3, 4, 5, 6, 7]
k1 = 2
direction1 = 'right'
rotated_arr1 = rotate_array(arr1, k1, direction1)
print(rotated_arr1)  # Output: [6, 7, 1, 2, 3, 4, 5]

# Example usage for left rotation
arr2 = [3, 7, 8, 9, 10, 11]
k2 = 3
direction2 = 'left'
rotated_arr2 = rotate_array(arr2, k2, direction2)
print(rotated_arr2)  # Output: [9, 10, 11, 3, 7, 8] 
    