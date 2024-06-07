# Problem Statement: This problem has 3 variations. They are stated below:

# Variation 1: Given row number r and column number c. Print the element at position (r, c) in Pascal’s triangle.

# Variation 2: Given the row number n. Print the n-th row of Pascal’s triangle.

# Variation 3: Given the number of rows n. Print the first n rows of Pascal’s triangle.
# Example 1:
# Input Format:
#  N = 5, r = 5, c = 3
# Result:
#  6 (for variation 1)
# 1 4 6 4 1 (for variation 2)

# 1 
# 1 1 
# 1 2 1 
# 1 3 3 1 
# 1 4 6 4 1    (for variation 3)

# Explanation:
#  There are 5 rows in the output matrix. Each row is formed using the logic of Pascal’s triangle.

# Example 2:
# Input Format:
#  N = 1, r = 1, c = 1
# Result:
#  1 (for variation 1)
#     1 (for variation 2)
#     1  (for variation 3)
# Explanation:
#  The output matrix has only 1 row.

#V1
import math

def nCr(n, r):
    res = 1

    # calculating nCr:
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)

    return res

def pascalTriangle(r, c):
    element = nCr(r - 1, c - 1)
    return element

if __name__ == '__main__':
    r = 5 # row number
    c = 3 # col number
    element = pascalTriangle(r, c)
    print(f"The element at position (r,c) is: {element}")
    
#V2
def pascalTriangle(n):
    ans = 1
    print(ans, end=" ") # printing 1st element

    #Printing the rest of the part:
    for i in range(1, n):
        ans = ans * (n - i)
        ans = ans // i
        print(ans, end=" ")
    print()

if __name__ == "__main__":
    n = 5
    pascalTriangle(n)
#V3
from typing import *

def generateRow(row):
    ans = 1
    ansRow = [1] #inserting the 1st element
    
    #calculate the rest of the elements:
    for col in range(1, row):
        ans *= (row - col)
        ans //= col
        ansRow.append(ans)
    return ansRow

def pascalTriangle(n : int) -> List[List[int]]:
    ans = []
    
    #store the entire pascal's triangle:
    for row in range(1, n+1):
        ans.append(generateRow(row))
    return ans

if __name__ == '__main__':
    n = 5
    ans = pascalTriangle(n)
    for it in ans:
        for ele in it:
            print(ele, end=" ")
        print()