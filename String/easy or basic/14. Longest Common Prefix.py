# 14. Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.
def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    # Initialize the prefix as the first string
    prefix = strs[0]
    
    # Compare the prefix with each string in the list
    for string in strs[1:]:
        # Update the prefix
        while string[:len(prefix)] != prefix and prefix:
            prefix = prefix[:len(prefix)-1]
        
        # If the prefix is empty, return an empty string
        if not prefix:
            return ""
    
    return prefix

# Example usage:
print(longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
print(longestCommonPrefix(["dog", "racecar", "car"]))    # Output: ""
