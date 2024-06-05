# Problem Statement: Given an array, print all the elements which are leaders. A Leader is an element that is greater than all of the elements on its right side in the array.

# Examples
# Example 1:
# Input:

#  arr = [4, 7, 1, 0]
# Output
# :
#  7 1 0
# Explanation:

#  Rightmost element is always a leader. 7 and 1 are greater than the elements in their right side.

# Example 2:
# Input:

#  arr = [10, 22, 12, 3, 0, 6]
# Output:

#  22 12 6
# Explanation:

#  6 is a leader. In addition to that, 12 is greater than all the elements in its right side (3, 0, 6), also 22 is greater than 12, 3, 0, 6.

#NOTE: One approach is in my mind if we are at arr[i] then we will sort best of it's right sides arr[i:] and  we will compare it with arr[-1]{Last element because it will be largest} and after that if arr[i] > arr[-1] then that will be Leader , If Not then we will increase our pointer to i=i+1 and we will do same thing 

def find_leaders(arr):
    leaders = []
    n = len(arr)

    for i in range(n):
        right_subarray = arr[i+1:]
        if right_subarray:
            largest_in_right = max(right_subarray)# here basically we have avoid searching and then comparing the arr[i] with arr[i-1] instead we have find the max afterwards arr[i] 
            if arr[i] > largest_in_right:
                leaders.append(arr[i])
        else:
            leaders.append(arr[i]) # if no right elements exist that means only single element so tat will be leader

    return leaders

# Example usage:
arr1 = [4, 7, 1, 0]
arr2 = [10, 22, 12, 3, 0, 6]

print("Leaders in arr1:", find_leaders(arr1))
print("Leaders in arr2:", find_leaders(arr2))

#NOTE : In The previous code we have encounter Repeatitative sorting so to avaoid this we will optimised of solution : Our approach will be go to the last element arr[-1] append to the solution array and the traverse from  right to left (in reverse order) . then compare next element with previous on eif it's greater than it then it will be also candidate for leader so we will add to solution as for ledaer it should be greater than then it will be leader that's why we traverse from right to left
def find_leaders_optimized(arr):
    leader=[]
    n=len(arr)
    max_from_right=arr[-1] # we went to last element and store in some variable
    leader.append(max_from_right) # then addes to our answer variable
    for i in range(n-2,-1,-1): #traversing leaving the last element 
        if arr[i] > max_from_right: # if 2nd last is greater than the last elements then it's a leader then we will add into our answer array
            leader.append(arr[i]) 
            max_from_right = arr[i]
    leader.reverse()
    return leader
arr1 = [4, 7, 1, 0]
arr2 = [10, 22, 12, 3, 0, 6]

print("Leaders in arr1:", find_leaders_optimized(arr1))
print("Leaders in arr2:", find_leaders_optimized(arr2))
