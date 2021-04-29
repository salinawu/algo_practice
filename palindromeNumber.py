class Solution:
    def isPalindrome(self, x: int) -> bool:
        # return str(x) == str(x)[::-1]
        if x < 0:
            return False 
        
        digits = []
        while x > 0:
            digits.append(x % 10)
            x = x // 10
        
        return digits == digits[::-1]