# Problem Statement: Given an array of N integers, your task is to find unique quads that add up to give a target value. In short, you need to return an array of all the unique quadruplets [arr[a], arr[b], arr[c], arr[d]] such that their sum is equal to a given target.

# Example 1:
# Input Format:
#  arr[] = [1,0,-1,0,-2,2], target = 0
# Result:
#  [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Explanation:
#  We have to find unique quadruplets from the array such that the sum of those elements is equal to the target sum given that is 0. The result obtained is such that the sum of the quadruplets yields 0.

# Example 2:
# Input Format:
#  arr[] = [4,3,3,4,4,2,1,2,1,1], target = 9
# Result:
#  [[1,1,3,4],[1,2,2,4],[1,2,3,3]]
# Explanation:
#  The sum of all the quadruplets is equal to the target i.e. 9.
from typing import List
import itertools

def fourSum(nums: List[int], target: int) -> List[List[int]]:
    n = len(nums)
    st = set()

    # checking all possible quadruplets:
    for i in range(n):
        for j in range(i+1, n):
            hashset = set()
            for k in range(j+1, n):
                # taking bigger data type to avoid integer overflow:
                sum_ = nums[i] + nums[j] + nums[k]
                fourth = target - sum_
                if fourth in hashset:
                    temp = [nums[i], nums[j], nums[k], fourth]
                    temp.sort()
                    st.add(tuple(temp))
                # put the kth element into the hashset:
                hashset.add(nums[k])

    ans = [list(t) for t in st]
    return ans


if __name__ == '__main__':
    nums = [4, 3, 3, 4, 4, 2, 1, 2, 1, 1]
    target = 9
    ans = fourSum(nums, target)
    print("The quadruplets are:")
    for it in ans:
        print("[", end="")
        for ele in it:
            print(ele, end=" ")
        print("]", end=" ")
    print()