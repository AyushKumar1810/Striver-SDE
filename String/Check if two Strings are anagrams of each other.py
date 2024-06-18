# Problem Statement: Given two strings, check if two strings are anagrams of each other or not.

# Examples:

# Example 1:
# Input: CAT, ACT
# Output: true
# Explanation: Since the count of every letter of both strings are equal.

# Example 2:
# Input: RULES, LESRT 
# Output: false
# Explanation: Since the count of U and T  is not equal in both strings.

#NOTE: use hshmap and track the no of occurnace , value , count we can get from hashmap then we can compare value if it's same retrun True else False
#NOTE we can use XOR opertion also but we have to sort it first

def are_anagrams(s1: str, s2: str) -> bool:
    # Check length first
    if len(s1) != len(s2):
        return False
    
    # Initialize frequency dictionaries
    freq_s1 = {}
    freq_s2 = {}
    
    # Count frequency for each character in s1
    for char in s1:
        if char in freq_s1:
            freq_s1[char] += 1
        else:
            freq_s1[char] = 1
    
    # Count frequency for each character in s2
    for char in s2:
        if char in freq_s2:
            freq_s2[char] += 1
        else:
            freq_s2[char] = 1
    
    # Compare the frequency dictionaries
    return freq_s1 == freq_s2

# Example usage:
print(are_anagrams("CAT", "ACT"))  # Output: True
print(are_anagrams("RULES", "LESRT"))  # Output: False
