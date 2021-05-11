class Solution:
    def isValid(self, s: str) -> bool:
        parenDict = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        
        stack = []
        for c in s:
            if c in parenDict.keys():
                stack.append(c)
            elif len(stack) > 0 and c == parenDict[stack[-1]]:
                stack.pop()
            else: 
                return False
            
        if len(stack) > 0:
            return False
        
        return True