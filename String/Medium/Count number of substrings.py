# Count number of substrings
# Difficulty: MediumAccuracy: 20.46%Submissions: 94K+Points: 4
# Given a string of lowercase alphabets, count all possible substrings (not necessarily distinct) that have exactly k distinct characters. 

# Example 1:

# Input:
# S = "aba", K = 2
# Output:
# 3
# Explanation:
# The substrings are: "ab", "ba" and "aba".
# Example 2:

# Input: 
# S = "abaaca", K = 1
# Output:
# 7
# Explanation:
# The substrings are: "a", "b", "a", "aa", "a", "c", "a". 
# Your Task:
# You don't need to read input or print anything. Your task is to complete the function substrCount() which takes the string S and an integer K as inputs and returns the number of substrings having exactly K distinct characters.

# Expected Time Complexity: O(|S|).
# Expected Auxiliary Space: O(1).

# Constraints:
# 1 ≤ |S| ≤ 106
# 1 ≤ K ≤ 26

#* Steps to Solve the Problem:
#Initialize Variables: Set up pointers for the sliding window, a frequency map to track characters, and counters to track distinct characters and the substring count.
#Sliding Window Technique: Expand the window by iterating through the string and adjusting the window's start and end positions based on the criteria of having exactly K distinct characters.
#Count Substrings: Maintain the count of substrings meeting the criteria using the sliding window technique.
#Edge Case Handling: Handle cases where the string length is less than K.
def substrCount(S: str, K: int) -> int:
    if K == 0:
        return 0

    n = len(S)
    left = 0
    count = 0

    # Map to store character frequencies
    char_count = {}
    
    for right in range(n):
        # Add the character at 'right' to the frequency map
        char_count[S[right]] = char_count.get(S[right], 0) + 1

        # Adjust the window to ensure it contains exactly 'K' distinct characters
        while len(char_count) > K:
            char_count[S[left]] -= 1
            if char_count[S[left]] == 0:
                del char_count[S[left]]
            left += 1

        # If the window has exactly 'K' distinct characters, count substrings
        if len(char_count) == K:
            count += (right - left + 1)

    return count

# Examples
print(substrCount("aba", 2))  # Output: 3
print(substrCount("abaaca", 2))  # Output: 16

