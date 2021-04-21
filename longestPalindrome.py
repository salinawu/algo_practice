class Solution:
    # i hate this problem 
    # dynamic programming
    def longestPalindrome(self, s: str) -> str:
        # keep track of whether palindrome in 2d array based on indices
        table = [[0 for i in s] for i in s]
        longest_palindrome = ''

        # every item is its own palindrome
        for i in range(len(s)):
            table[i][i] = 1
            longest_palindrome = s[i]
        
        # mark down 2-item palindromes for even length palindromes
        for index, i in enumerate(s[:-1]):
            if i == s[index + 1]:
                table[index][index + 1] = 1
                longest_palindrome = s[index:index + 2]

        # go thru 2d array from bottom right corner going up
        for i in range(len(s) - 2, -1, -1):
            for j in range(i + 1, len(s)):
                if (s[i] == s[j]) and (table[i+1][j-1] == 1 or (j - i == 1)):
                        longest_palindrome = longest_palindrome if len(longest_palindrome) > (j - i + 1) else s[i:j+1]
                        table[i][j] = 1

        return longest_palindrome
                    
