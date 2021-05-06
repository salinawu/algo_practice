class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        index = 0
        
        # if len(strs) == 0:
        #     return prefix
        
        while True:
            
            if all(index < len(str1) and str1[index] == str2[index] for elem in strs):
                prefix += strs[0][index]
            else:
                return prefix
            
            index += 1
            
            
            
                