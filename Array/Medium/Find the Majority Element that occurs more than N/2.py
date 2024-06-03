# Problem Statement: Given an array of N integers, write a program to return an element that occurs more than N/2 times in the given array. You may consider that such an element always exists in the array.

# Examples
# Example 1:
# Input Format
# : N = 3, nums[] = {3,2,3}
# Result
# : 3
# Explanation
# : When we just count the occurrences of each number and compare with half of the size of the array, you will get 3 for the above solution. 

# Example 2:
# Input Format:
#   N = 7, nums[] = {2,2,1,1,1,2,2}

# Result
# : 2

# Explanation
# : After counting the number of times each element appears and comparing it with half of array size, we get 2 as result.

# Example 3:
# Input Format:
#   N = 10, nums[] = {4,4,2,4,3,4,4,3,2,4}

# Result
# : 4
#Solution : (Better): UISNG HASHMAP Count the occurance if it's greater then N/2 the return it
from itertools import count


from collections import Counter

def majorityElement(arr):
    # Size of the given array
    n = len(arr)

    # Count the occurrences of each element using Counter
    counter = Counter(arr)

    # Searching for the majority element
    for num, count in counter.items():
        if count > (n // 2):
            return num

    return -1

arr  = [2, 2, 1, 1, 1, 2, 2]
ans = majorityElement(arr)
print("The majority element is:", ans)
            
#NOTE:Optimal Approach: Moore’s Voting Algorithm:
# Approach: 
# Initialize 2 variables:
# Count –  for tracking the count of element
# Element – for which element we are counting
# Traverse through the given array.
# If Count is 0 then store the current element of the array as Element.
# If the current element and Element are the same increase the Count by 1.
# If they are different decrease the Count by 1.
# The integer present in Element should be the result we are expecting 

def majorityElement(arr):
    # Size of the given array
    n = len(arr)
    cnt = 0  # Count
    el = None  # Element

    # Applying the algorithm
    for i in range(n):
        if cnt == 0:
            cnt = 1
            el = arr[i]
        elif el == arr[i]:
            cnt += 1
        else:
            cnt -= 1

    # Checking if the stored element is the majority element
    cnt1 = 0
    for i in range(n):
        if arr[i] == el:
            cnt1 += 1

    if cnt1 > (n / 2):
        return el
    return -1


arr = [2, 2, 1, 1, 1, 2, 2]
ans = majorityElement(arr)
print("The majority element is:", ans)