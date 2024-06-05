# Variety-1

# Problem Statement:

# There’s an array ‘A’ of size ‘N’ with an equal number of positive and negative elements. Without altering the relative order of positive and negative elements, you must return an array of alternately positive and negative values.

# Note: Start the array with positive elements.

# Examples: 

# Example 1:

# Input:
# arr[] = {1,2,-4,-5}, N = 4
# Output:
# 1 -4 2 -5

# Explanation: 

# Positive elements = 1,2
# Negative elements = -4,-5
# To maintain relative ordering, 1 must occur before 2, and -4 must occur before -5.

# Example 2:
# Input:
# arr[] = {1,2,-3,-1,-2,-3}, N = 6
# Output:
# 1 -3 2 -1 3 -2
# Explanation: 

# Positive elements = 1,2,3
# Negative elements = -3,-1,-2
# To maintain relative ordering, 1 must occur before 2, and 2 must occur before 3.
# Also, -3 should come before -1, and -1 should come before -2.

def RearrangebySign(A):
    n=len(A)
    arr=[0]*n # we will create an array of  same size as that of Given array Initialising with 0
    positiveIndex ,negativeIndex=0 ,1
    for i in range(n):
        if A[i]<0:
            arr[negativeIndex]=A[i]
            negativeIndex+=2
        else:
            arr[positiveIndex]=A[i]
            positiveIndex+=2
    return arr


def RearrangebySign(A):
    n=len(A)
    array=[0]*n
    postiveIndex , NegativeIndex=0,1
    for i in range(n):
        if A[i] <0:
            array[NegativeIndex] =  A[i]
            NegativeIndex+=2
        else:
            array[postiveIndex] =  A[i]
            postiveIndex+=2
    return array