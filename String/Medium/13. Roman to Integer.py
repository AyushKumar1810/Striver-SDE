# 13. Roman to Integer
# Hint
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

 

# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

#NOTE: #* Here we can see roman no can be represented by 7 symbol so we define these 7 symbol with their equivalent inetger value and we itterate through Given string and if if it's in that then we will update and make sum and retrun it

def romanToInt(s: str) -> int:
    # Step 1: Create a dictionary to map Roman numerals to integers
    roman_to_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    # Step 2: Initialize the total sum to 0
    total = 0
    n = len(s)
    
    # Step 3: Iterate through the string
    for i in range(n):
        # Get the value of the current Roman numeral
        current_value = roman_to_int[s[i]]
        
        # Check if the current numeral is the last one or not
        if i < n - 1:
            next_value = roman_to_int[s[i + 1]]
            # Step 4: Apply the subtraction rule
            if current_value < next_value:
                total -= current_value
            else:
                total += current_value
        else:
            # For the last character, just add its value
            total += current_value
    
    return total

# Examples
print(romanToInt("III"))      # Output: 3
print(romanToInt("LVIII"))    # Output: 58
print(romanToInt("MCMXCIV"))  # Output: 1994
