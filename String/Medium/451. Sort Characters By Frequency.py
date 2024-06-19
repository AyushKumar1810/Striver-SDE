# 451. Sort Characters By Frequency

# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

# Return the sorted string. If there are multiple answers, return any of them.

 

# Example 1:

# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:

# Input: s = "cccaaa"
# Output: "aaaccc"
# Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
# Note that "cacaca" is incorrect, as the same characters must be together.
# Example 3:

# Input: s = "Aabb"
# Output: "bbAa"
# Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.

#* simple Our approach will be very easy we will use "ord" to find each no of occurance and hashmap ww can use it and those frequency is max will update according to that 
from collections import Counter

def frequencySort(s: str) -> str:
    # Step 1: Count the frequency of each character
    freq = Counter(s)
    
    # Step 2: Sort characters by frequency in decreasing order
    sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    
    # Step 3: Construct the result string
    result = ''.join([char * count for char, count in sorted_chars])
    
    return result

# Examples
print(frequencySort("tree"))  # Output: "eert" or "eetr"
print(frequencySort("cccaaa"))  # Output: "aaaccc" or "cccaaa"
print(frequencySort("Aabb"))  # Output: "bbAa" or "bbaA"

