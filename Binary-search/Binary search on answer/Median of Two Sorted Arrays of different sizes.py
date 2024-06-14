# Problem Statement: Given two sorted arrays arr1 and arr2 of size m and n respectively, return the median of the two sorted arrays. The median is defined as the middle value of a sorted list of numbers. In case the length of the list is even, the median is the average of the two middle elements.

# Examples
# Example 1:
# Input Format:
#  n1 = 3, arr1[] = {2,4,6}, n2 = 3, arr2[] = {1,3,5}
# Result:
#  3.5
# Explanation:
#  The array after merging 'a' and 'b' will be { 1, 2, 3, 4, 5, 6 }. As the length of the merged list is even, the median is the average of the two middle elements. Here two medians are 3 and 4. So the median will be the average of 3 and 4, which is 3.5.

# Example 2:
# Input Format:
#  n1 = 3, arr1[] = {2,4,6}, n2 = 2, arr2[] = {1,3}
# Result:
#  3
# Explanation:
#  The array after merging 'a' and 'b' will be { 1, 2, 3, 4, 6 }. The median is simply 3.

def findMedianSortedArrays(nums1, nums2):
    # Ensure nums1 is the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    x, y = len(nums1), len(nums2)
    low, high = 0, x
    
    while low <= high:
        partitionX = (low + high) // 2
        partitionY = (x + y + 1) // 2 - partitionX
        
        maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        minX = float('inf') if partitionX == x else nums1[partitionX]
        
        maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        minY = float('inf') if partitionY == y else nums2[partitionY]
        
        if maxX <= minY and maxY <= minX:
            # We have partitioned array at the correct place
            if (x + y) % 2 == 0:
                return (max(maxX, maxY) + min(minX, minY)) / 2
            else:
                return max(maxX, maxY)
        elif maxX > minY: # We are too far on the right side for partitionX
            high = partitionX - 1
        else: # We are too far on the left side for partitionX
            low = partitionX + 1
    
    raise ValueError("Input arrays are not sorted")

# Example 1:
n1, arr1 = 3, [2, 4, 6]
n2, arr2 = 3, [1, 3, 5]
print(findMedianSortedArrays(arr1, arr2))  # Output: 3.5

# Example 2:
n1, arr1 = 3, [2, 4, 6]
n2, arr2 = 2, [1, 3]
print(findMedianSortedArrays(arr1, arr2))  # Output: 3
