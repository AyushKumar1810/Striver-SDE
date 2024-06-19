# 1903. Largest Odd Number in String
# Hint
# You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.

# A substring is a contiguous sequence of characters within a string.

 

# Example 1:

# Input: num = "52"
# Output: "5"
# Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.
# Example 2:

# Input: num = "4206"
# Output: ""
# Explanation: There are no odd numbers in "4206".
# Example 3:

# Input: num = "35427"
# Output: "35427"
# Explanation: "35427" is already an odd number.
 

# Constraints:

# 1 <= num.length <= 105
# num only consists of digits and does not contain any leading zeros.
#NOTE : we willl traverse the given string from backwards (Right to left){because we want largest that's why moving from right to left } , then we will check if it's odd , if arr[i]%2!=0 , if it's then we will simply return the startingindex to that point of index (return num[:i+1])
def largestOddNumber(num: str) -> str:
    # Traverse the string from right to left
    for i in range(len(num)-1,-1,-1): # we want max value so we are moving right to left 
        # Check if the current character is an odd digit
        if int(num[i])%2 !=0:# at any apoint we are getting odd numbers just return from starting index to that Point 
            # Return the substring from the start to the current position
            return num[:i+1] # If odd return it 
         # If no odd digit is found, return an empty string
    return ""
# Example usage:
print(largestOddNumber("52"))       # Output: "5"
print(largestOddNumber("4206"))     # Output: ""
print(largestOddNumber("35427"))    # Output: "35427"