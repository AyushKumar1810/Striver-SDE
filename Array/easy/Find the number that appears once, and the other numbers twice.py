# Problem Statement: Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.

# Examples
# Example 1:
# Input Format:
#  arr[] = {2,2,1}
# Result:
#  1
# Explanation:
#  In this array, only the element 1 appear once and so it is the answer.

# Example 2:
# Input Format:
#  arr[] = {4,1,2,1,2}
# Result:
#  4
# Explanation:
#  In this array, only element 4 appear once and the other elements appear twice. So, 4 is the answer.
#NOTE : there will be two approach One is Go with HashMap and another is with XOR , the problem is with hashmap is that space complexivity will be O(N) but with XOR it will be O(1)

# Intuition:
# Two important properties of XOR are the following:

# XOR of two same numbers is always 0 i.e. a ^ a = 0. ← Property 1.
# XOR of a number with 0 will result in the number itself i.e. 0 ^ a = a.  ← Property 2

def getSingleElement(arr):
    xorr=0
    for num in arr:
        xorr=xorr^num
    return xorr
def main():
    arr = [4, 1, 2, 1, 2]
    ans = getSingleElement(arr)
    print("The single element is:", ans)

if __name__ == "__main__":
    main()