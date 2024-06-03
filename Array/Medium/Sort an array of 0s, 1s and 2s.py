# Problem Statement: Given an array consisting of only 0s, 1s, and 2s. Write a program to in-place sort the array without using inbuilt sort functions. ( Expected: Single pass-O(N) and constant space)

# Examples
# Input:
#  nums = [2,0,2,1,1,0]
# Output
# : [0,0,1,1,2,2]

# Input:
#  nums = [2,0,1]
# Output:
#  [0,1,2]

# Input:
#  nums = [0]
# Output:
#  [0]
#NOTE : we count the appreacance of 0 ,1 and 2  Then we will iterate throught eacg one , 0 ,1 and 2 to that extend and we will add that much 0,1, and two on that range 
def sortArray(arr):
    cnt_0,cnt_1,cnt_2 = 0 ,0 , 0 
    for num in arr :
        if num ==0:
            cnt_0+=1
        elif num==1:
            cnt_1+=1
        else:
            cnt_2+=1
    for i in range(cnt_0):
        arr[i]=0
    for i in range(cnt_0 , cnt_0+cnt_1):
        arr[i] = 1
    for i in range(cnt_0+cnt_1, len(arr)):
        arr[i]=2
n = 6
arr = [0, 2, 1, 2, 0, 1]
sortArray(arr)
print("After sorting:")
for num in arr:
    print(num, end=" ")
print()

#NOTE : Optimal Approach
def sortArray(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
n = 6
arr = [0, 2, 1, 2, 0, 1]
sortArray(arr)
print("After sorting:")
for num in arr:
    print(num, end=" ")
print()