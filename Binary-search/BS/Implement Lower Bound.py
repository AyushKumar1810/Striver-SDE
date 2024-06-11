# Problem Statement: Given a sorted array of N integers and an integer x, write a program to find the lower bound of x.

# Pre-requisite: Binary Search algorithm

# Examples
# Example 1:
# Input Format:
#  N = 4, arr[] = {1,2,2,3}, x = 2
# Result:
#  1
# Explanation:
#  Index 1 is the smallest index such that arr[1] >= x.

# Example 2:
# Input Format:
#  N = 5, arr[] = {3,5,8,15,19}, x = 9
# Result:
#  3
# Explanation:
#  Index 3 is the smallest index such that arr[3] >= x.

#NOTE: we can solve this problem By two ways Linear search as well as optimal way Binary search
def lowerBound(arr: [int], n: int, x: int) -> int:
    for i in range(n):
        if arr[i] >= x:
            #lower bound found
            return i
    return n

if __name__ == "__main__":
    arr = [3, 5, 8, 15, 19]
    n = 5
    x = 9
    ind = lowerBound(arr, n, x)
    print("The lower bound is the index:", ind)

    #Binary search 
    def Lower(arr ,n,x):
        low , high = 0 , n-1
        ans = n
        while low <= high:
            mid = (low + high)//2
            if arr[mid] >=x:
                ans = mid
                high = mid -1
            else:
                low = low+1
        return ans  
arr = [3, 5, 8, 15, 19]
n = 5
x = 9
ind = Lower(arr, n, x)
print("The lower bound is the index:", ind)