# 1614. Maximum Nesting Depth of the Parentheses

# Hint
# *Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.



# Example 1:

# Input: s = "(1+(2*3)+((8)/4))+1"

# Output: 3

# Explanation:

# Digit 8 is inside of 3 nested parentheses in the string.

# Example 2:

# Input: s = "(1)+((2))+(((3)))"

# Output: 3

# Explanation:

# Digit 3 is inside of 3 nested parentheses in the string.

# Example 3:

# Input: s = "()(())((()()))"

# Output: 3

#!NOTE: Easy , we initially Traverse it and then we will se if '(' then we will incease counter and we will store in max , if we encouter this ')' then we will reset the counter to 1 and we will keep looking and at last we will return the max

# *Initialize a Counter: Use a counter to keep track of the current depth of nesting.
# *Track Maximum Depth: Keep a variable to track the maximum depth encountered during the traversal of the string.
# *Traverse the String: Iterate through each character in the string:
#* Increment the counter when encountering an opening parenthesis (.
# *Decrement the counter when encountering a closing parenthesis ).
# *Update the maximum depth after each increment.
#* Return the Maximum Depth: After traversing the string, the variable tracking the maximum depth will hold the desired result.

def maxDepth(s: str) -> int:
    current_depth , max_depth = 0 , 0
    for char in s:
        if char=='(':#* simple we only have to see openeing bracket that will be max nested parentheses
            current_depth+=1
            max_depth = max(current_depth,max_depth)

        elif char==')':
            current_depth-=1
    return max_depth
# Examples
print(maxDepth("(1+(2*3)+((8)/4))+1"))  # Output: 3
print(maxDepth("(1)+((2))+(((3)))"))    # Output: 3
print(maxDepth("()(())((()()))"))       # Output: 3



# def maxDepth(s: str) -> int:
#     current, maximum=0,0
#     for char in s:
#         if char =='(':
#             current+=1
#             maximum=max(current,maximum)
#         elif char ==')':
#             current-=1
#     return maximum