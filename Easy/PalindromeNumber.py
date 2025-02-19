class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x < 0): # Negative numbers are not palindromes e.g -121 is 121-
            return False 
        else: # Convert to string and check if first and last chars are the same until the middle
            num = str(x)
            for i in range((int)(len(num) / 2)):
                if(num[i] != num[len(num) - 1 - i]): 
                    return False
            return True
        
s = Solution()
print(s.isPalindrome(-21))
            