# https://leetcode.com/problems/reverse-integer/description/

class Solution:
    def reverse(self, x: int) -> int:
        num: int = abs(x) # Convert to unsigned integer

        # Use modulo to reverse integer by extracting digits
        # Then add those digits to new number while ensuring correct placeholder
        y = 0
        while True:
            if num < 1: break # Exit loop when all digits reversed
            digit = num % 10
            num //= 10 # The //= operator performs integer division which rounds to 0 aka 57 / 10 = 5
            y *= 10
            y += digit

        y *= 1 if x > 0 else -1 # Restore original signage of integer
        if y > -2**31 and y < 2**31 - 1: # Check if result is within 32-bit integer range
            return y
        else: 
            return 0 # If answer goes outside signed 32-bit integer range then return 0
        
print(Solution().reverse(1234)) # ans = 4321