# Problem Statement: Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array.

# Examples:

# Example 1:

# Input: prices = {1, 1, 0, 1, 1, 1}

# Output: 3

# Explanation: There are two consecutive 1’s and three consecutive 1’s in the array out of which maximum is 3.

# Input: prices = {1, 0, 1, 1, 0, 1} 

# Output: 2

# Explanation: There are two consecutive 1's in the array. 
#NOTE: take two variable prev_count and count , then traverse the array if arr[i] == 1 then increase the count and if arr[i]==0 then count=0 Then return the max(prev_count,count)
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        cnt = 0
        maxi = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
            else:
                cnt = 0
            maxi = max(maxi, cnt)
        return maxi




if __name__ == "__main__":
    nums = [1, 1, 0, 1, 1, 1]
    obj = Solution()
    ans = obj.findMaxConsecutiveOnes(nums)
    print("The maximum  consecutive 1's are", ans)
