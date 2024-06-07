# Problem Statement: Given an array of N integers, your task is to find unique triplets that add up to give a sum of zero. In short, you need to return an array of all the unique triplets [arr[a], arr[b], arr[c]] such that i!=j, j!=k, k!=i, and their sum is equal to zero.

# Pre-requisite: 2 Sum Problem

# Examples
# Example 1:
# Input:
#  nums = [-1,0,1,2,-1,-4]

# Output:
#  [[-1,-1,2],[-1,0,1]]

# Explanation:
#  Out of all possible unique triplets possible, [-1,-1,2] and [-1,0,1] satisfy the condition of summing up to zero with i!=j!=k

# Example 2:
# Input:
#  nums=[-1,0,1,0]
# Output:
#  Output: [[-1,0,1],[-1,1,0]]
# Explanation:
#  Out of all possible unique triplets possible, [-1,0,1] and [-1,1,0] satisfy the condition of summing up to zero with i!=j!=k

def triplet(n, arr):
    st=set()
    for i in range(n):
        hashsets=set()
        for j in range(i+1,n):
            third = -(arr[i]+arr[j])
            if third in hashsets:
                temp = [arr[i] , arr[j] , third]
                temp.sort()
                st.add(tuple(temp))
            hashsets.add(arr[j])
    ans=list(st)
    return ans
arr = [-1, 0, 1, 2, -1, -4]
n = len(arr)
ans = triplet(n, arr)
for it in ans:
    print("[", end="")
    for i in it:
        print(i, end=" ")
    print("]", end=" ")
print()