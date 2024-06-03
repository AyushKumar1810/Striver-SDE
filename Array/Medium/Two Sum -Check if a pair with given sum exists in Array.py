# Problem Statement: Given an array of integers arr[] and an integer target.

# 1st variant: Return YES if there exist two numbers such that their sum is equal to the target. Otherwise, return NO.

# 2nd variant: Return indices of the two numbers such that their sum is equal to the target. Otherwise, we will return {-1, -1}.

# Note: You are not allowed to use the same element twice. Example: If the target is equal to 6 and num[1] = 3, then nums[1] + nums[1] = target is not a solution.

# Examples:

# Example 1:
# Input Format: N = 5, arr[] = {2,6,5,8,11}, target = 14
# Result: YES (for 1st variant)
#        [1, 3] (for 2nd variant)
# Explanation: arr[1] + arr[3] = 14. So, the answer is “YES” for the first variant and [1, 3] for 2nd variant.

# Example 2:
# Input Format: N = 5, arr[] = {2,6,5,8,11}, target = 15
# Result: NO (for 1st variant)
# 	[-1, -1] (for 2nd variant)
# Explanation: There exist no such two numbers whose sum is equal to the target.

#1st Variant: Return YES or NO
def two_sum_exists(arr, target):
    seen = {}
    for num in arr:
        required_sum = target - num
        if required_sum in seen :
            return "Yes"    
        seen[num] = True
    return "NO"
# Example usage:
arr1 = [2, 6, 5, 8, 11]
target1 = 14
print(two_sum_exists(arr1, target1))  # Output: YES

arr2 = [2, 6, 5, 8, 11]
target2 = 15
print(two_sum_exists(arr2, target2))  # Output: NO

# 2nd Variant: Return Indices
def two_sum_indices(arr, target):
    seen ={}
    for i , num in enumerate(arr):
        requiredsum= target - num 
        if requiredsum in seen:
            return [seen[requiredsum] , i]
        seen[num] = i
    return [-1,-1]
# Example usage:
arr1 = [2, 6, 5, 8, 11]
target1 = 14
print(two_sum_indices(arr1, target1))  # Output: [1, 3]

arr2 = [2, 6, 5, 8, 11]
target2 = 15
print(two_sum_indices(arr2, target2))  # Output: [-1, -1]