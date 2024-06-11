# Problem Statement: Given two numbers N and M, find the Nth root of M. The nth root of a number M is defined as a number X when raised to the power N equals M. If the 'nth root is not an integer, return -1.

# Examples
# Example 1:
# Input Format:
#  N = 3, M = 27
# Result:
#  3
# Explanation:
#  The cube root of 27 is equal to 3.

# Example 2:
# Input Format:
#  N = 4, M = 69
# Result:
#  -1
# Explanation:
#  The 4th root of 69 does not exist. So, the answer is -1.

def func(mid, n, m):
    ans = 1
    for i in range(1, n + 1):
        ans *= mid
        if ans > m:
            return 2
    if ans == m:
        return 1
    return 0

def NthRoot(n: int, m: int) -> int:
    low = 1
    high = m
    while low <= high:
        mid = (low + high) // 2
        midN = func(mid, n, m)
        if midN == 1:
            return mid
        elif midN == 0:
            low = mid + 1
        else:
            high = mid - 1
    return -1

n = 3
m = 27
ans = NthRoot(n, m)
print("The answer is:", ans)


#Easy and simplified and get rejected duting interview 😂
import math

def find_nth_root(N, M):
    if N == 0 or M == 0:
        return -1

    # Calculate the Nth root of M using math.pow function
    root = math.pow(M, 1/N)

    # Check if the computed root raised to the power of N gives M
    if root.is_integer():
        return int(root)
    else:
        return -1

# Example Usage:
N = 3
M = 27
print(find_nth_root(N, M)) # Output: 3

N = 4
M = 69
print(find_nth_root(N, M)) # Output: -1
