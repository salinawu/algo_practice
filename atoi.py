class Solution:
    def myAtoi(self, s: str) -> int:
        finalString = ''
        multiplier = None
        strippedString = s.strip()
        
        for char in strippedString:
            if char == '-' and multiplier == None and len(finalString) == 0:
                multiplier = -1
            elif char == '+' and multiplier == None and len(finalString) == 0:
                multiplier = 1
            elif char.isdigit():
                finalString += char
            else:
                break

        if len(finalString) == 0:
            return 0
        
        if multiplier == None:
            multiplier = 1
            
        finalNumber = multiplier * int(finalString)
        minBoundary = -2 ** 31
        maxBoundary = (2 ** 31) - 1
        if finalNumber < minBoundary:
            return minBoundary
        elif finalNumber > maxBoundary:
            return maxBoundary
        else:
            return finalNumber