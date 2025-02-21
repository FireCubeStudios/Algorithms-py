# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    # Sliding window + set
    # Expand the window to the right until a duplicate is found
    # Then shrink the window from the left to the right until duplicate is gone
    # Continue until end of string is reached
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "": return 0
        maxLength = 0
        start = 0 # Start index, aka left side of sliding window
        end = 0 # End index, aka right of sliding window
        subset = set() # Set to check for duplicate characters in window
        while True:
            maxLength = max(maxLength, end - start)
            if end == len(s): break # Sliding window reached end of string
            if s[end] in subset: # If duplicate then shrink sliding window left to right until duplicate gone
                subset.remove(s[start])
                start += 1
            else: # Expand sliding window to right until duplicate found
                subset.add(s[end])
                end += 1
        return maxLength    
    

print(Solution().lengthOfLongestSubstring("aab")) # ans = 2
print(Solution().lengthOfLongestSubstring("abcabcbb")) # ans = 3