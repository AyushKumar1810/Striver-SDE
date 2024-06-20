# 1781. Sum of Beauty of All Substrings

# Hint
#* The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.

# For example, the beauty of "abaacc" is 3 - 1 = 2.
# Given a string s, return the sum of beauty of all of its substrings.

 

# Example 1:

# Input: s = "aabcb"
# Output: 5
# Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.
# Example 2:

# Input: s = "aabcbaa" 
# Output: 17

#!Here's how we can solve this problem:

# Generate all substrings: Iterate through all possible substrings of the given string s.
# Calculate beauty for each substring: For each substring, calculate the frequency of each character, then determine the beauty by finding the difference between the maximum and minimum frequency.
# Sum the beauties: Sum up the beauty values of all substrings to get the final result.
def beautySum(s: str) -> int:
    def calculateBeauty(freq):
        max_freq = max(freq.values())
        min_freq = min(freq.values())
        return max_freq - min_freq

    total_beauty = 0
    n = len(s)

    # Iterate over all possible starting points of substrings
    for i in range(n):
        freq = {}  # Dictionary to store the frequency of characters
        
        # Iterate over all possible ending points of substrings starting at i
        for j in range(i, n):
            char = s[j]
            if char in freq:
                freq[char] += 1# will increase that specific character count by 1
            else:
                freq[char] = 1
            
            # Only calculate beauty if the substring has at least 2 different characters
            if len(freq) > 1:
                total_beauty += calculateBeauty(freq)
    
    return total_beauty

# Example usage:
s1 = "aabcb"
s2 = "aabcbaa"

print(beautySum(s1))  # Output: 5
print(beautySum(s2))  # Output: 17

# class Solution:
#     def beautySum(self, s: str) -> int:
#         res = 0
#         for i in range(len(s)):
#             count = defaultdict(int)
#             for j in range(i,len(s)):
#                 count[s[j]] += 1
#                 minF = min(count.values())
#                 maxF = max(count.values())
#                 res += (maxF -minF)
#         return res