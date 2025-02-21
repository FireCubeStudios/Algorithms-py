# https://leetcode.com/problems/reverse-integer/description/

class Solution:
    def reverse(self, x: int) -> int:
        num = abs(x) # Convert to unsigned integer

        # Use modulo to reverse integer by extracting digits
        # Then add those digits to new number while ensuring correct placeholder
        i = 10
        prev = 0
        y = 0
        while True:
            if num / (i / 10) < 1: break # Exit loop when all digits reversed
            digit = (int)(((num % i) - prev) / (i / 10))
            y *= 10
            y += digit
            i *= 10

        y *= 1 if x > 0 else -1 # Restore original signage of integer
        if y > -2**31 and y < 2**31 - 1: # Check if result is within 32-bit integer range
            return y
        else: 
            return 0 # If answer goes outside signed 32-bit integer range then return 0
        
print(Solution().reverse(1234))