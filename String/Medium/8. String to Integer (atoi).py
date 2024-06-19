# 8. String to Integer (atoi)

# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

# The algorithm for myAtoi(string s) is as follows:

# Whitespace: Ignore any leading whitespace (" ").
# Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity is neither present.
# Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
# Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
# Return the integer as the final result.

 

# Example 1:

# Input: s = "42"

# Output: 42

# Explanation:

# The underlined characters are what is read in and the caret is the current reader position.
# Step 1: "42" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "42" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "42" ("42" is read in)
#            ^
# Example 2:

# Input: s = " -042"

# Output: -42

# Explanation:

# Step 1: "   -042" (leading whitespace is read and ignored)
#             ^
# Step 2: "   -042" ('-' is read, so the result should be negative)
#              ^
# Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
#                ^
# Example 3:

# Input: s = "1337c0d3"

# Output: 1337

# Explanation:

# Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
#              ^
# Example 4:

# Input: s = "0-1"

# Output: 0

# Explanation:

# Step 1: "0-1" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)
#           ^
# Example 5:

# Input: s = "words and 987"

# Output: 0

# Explanation:

# Reading stops at the first non-digit character 'w'.

 

# Constraints:

# 0 <= s.length <= 200
# s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.

#NOTE: #* Very easy the algorithm i will use is tat we will se if the traversing didgit is in 1-9 , and the basecondition is that if traversing character leading with 0 then we will skip it and move to next character and if we encounter anything except 0-9 then we will stop traversing and initially we got netaive "-" we will consider 
def myAtoi(s: str) -> int:
    s = s.lstrip()  # Step 1: Trim leading whitespace

    if not s:
        return 0  # If string is empty or contains only whitespace

    sign = 1  # Default to positive
    if s[0] == '+':
        sign = 1
        s = s[1:]  # Remove the sign character
    elif s[0] == '-':
        sign = -1
        s = s[1:]  # Remove the sign character

    result = 0
    for char in s:
        if char.isdigit():# * here Checking it's a digit , if not stop the loop
            result = result * 10 + int(char)# we are moving one by one 
        else:
            break  # Stop processing when a non-digit character is encountered

    result *= sign  # Apply the sign
    result = max(-2**31, min(result, 2**31 - 1))  # Constrain to 32-bit range

    return result

# Examples
print(myAtoi("42"))          # Output: 42
print(myAtoi("   -042"))     # Output: -42
print(myAtoi("1337c0d3"))    # Output: 1337
print(myAtoi("0-1"))         # Output: 0
print(myAtoi("words and 987")) # Output: 0
