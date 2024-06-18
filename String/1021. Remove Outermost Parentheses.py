# 1021. Remove Outermost Parentheses
# Hint
# A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

# For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
# A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

# Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

# Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

 

# Example 1:

# Input: s = "(()())(())"
# Output: "()()()"
# Explanation: 
# The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
# After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
# Example 2:

# Input: s = "(()())(())(()(()))"
# Output: "()()()()(())"
# Explanation: 
# The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
# After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
# Example 3:

# Input: s = "()()"
# Output: ""
# Explanation: 
# The input string is "()()", with primitive decomposition "()" + "()".
# After removing outer parentheses of each part, this is "" + "" = "".

#NOTE: simple if this ( comes then Afterthat This ) should be com eotherwise will remove it , if we directly encounter ) then just remove 

# def removeOuterParentheses(s: str) -> str:
#     result = []
#     balance = 0
#     for char in s:
#         if char == '(':
#             if balance > 0:
#                 result.append(char)
#             balance += 1
#         elif char==')':
#             balance-=1
#             if balance>0:
#                 result.append(char)
#     return ''.join(result)
# # Example usage:
# print(removeOuterParentheses("(()())(())"))           # Output: "()()()"
# print(removeOuterParentheses("(()())(())(()(()))"))   # Output: "()()()()(())"
# print(removeOuterParentheses("()()"))                 # Output: ""

# BY uisng stack pop / append method

def removeOuterParentheses(s: str) -> str:
    result = []
    stack = []
    
    for char in s:
        if char == '(':
            if stack:
                result.append(char)
            stack.append(char)
        elif char == ')':
            stack.pop()
            if stack:
                result.append(char)
    
    return ''.join(result)

# Example usage:
print(removeOuterParentheses("(()())(())"))           # Output: "()()()"
print(removeOuterParentheses("(()())(())(()(()))"))   # Output: "()()()()(())"
print(removeOuterParentheses("()()"))                 # Output: ""

