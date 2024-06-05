# Problem Statement: You are given an array of ‘N’ integers. You need to find the length of the longest sequence which contains the consecutive elements.

# Examples
# Example 1:
# Input:
#  [100, 200, 1, 3, 2, 4]

# Output:
#  4

# Explanation:
#  The longest consecutive subsequence is 1, 2, 3, and 4.

# Input:
#  [3, 8, 5, 7, 6]

# Output:
#  4

# Explanation:
#  The longest consecutive subsequence is 5, 6, 7, and 8.

#NOTE : The basic approach came to my mind is that  we will sort given array and we will traverse till the differnce is 1 then it will be in sequence i.e 3-2 =1 .then we will take difference of j-i+1 that will be iur answer ; we will use two pointers approach : one will be at 0th index and other will be at 1st index and we will compare arr[i] with arr[j] if the difference is 1 then it will be in sequence nd we will increase j pointer by 1 , if the difference is not 1 then we will increase Both i and j pointers Both and we will check and repeat the same steps 

def longest_consecutive_sequence(arr):
    if not arr:
        return 0
    arr.sort()
    max_length =1
    current_length = 1
    for i in range(1,len(arr)):
        if arr[i] == arr[i-1] +1: # basically it's just checking the diffrence is 1 or not by adding 1 to Previous elements will defeinetly equal 
            current_length+=1
        elif arr[i]!=arr[i-1]+1:
            current_length=1
        max_length=max(max_length , current_length)
    return max_length
# Example usage:
arr1 = [100, 200, 1, 3, 2, 4,5,-1,0 ]
arr2 = [3, 8, 5, 7, 6]

print("Longest consecutive sequence length in arr1:", longest_consecutive_sequence(arr1))
print("Longest consecutive sequence length in arr2:", longest_consecutive_sequence(arr2))

#NOTE : for avaoidng The sorting and Higher Time complexivity we will use "set " that has storing time complexivity of O(1)

def longest_consecutive_sequence(arr):
    if not arr:
        return 0

    num_set = set(arr)
    max_length = 0

    for num in arr:
        # Check if the number is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            # Count the length of the sequence
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            # Update the maximum length
            max_length = max(max_length, current_length)

    return max_length

# Example usage:
arr1 = [100, 200, 1, 3, 2, 4]
arr2 = [3, 8, 5, 7, 6]

print("Longest consecutive sequence length in arr1:", longest_consecutive_sequence(arr1))
print("Longest consecutive sequence length in arr2:", longest_consecutive_sequence(arr2))
