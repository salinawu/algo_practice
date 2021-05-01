class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        reverseS = s[::-1]
        reverseP = p[::-1]
        matchingChar = None

        while len(reverseP) > 0:
            char = reverseP[0]

            if char == '*':
                matchingChar = reverseP[1]
                reverseP = reverseP[2:]

            # elif char == '.': # match one character
            #     reverseS = reverseS[1:]

            elif matchingChar == '.':
                

            elif matchingChar != None and len(reverseS):
                if matchingChar == '.': # match any char
                    matchingChar = reverseS[0]

                while reverseS[0] == matchingChar:
                    reverseS = reverseS[1:]

            elif char != reverseS[0] and char != '.':
                return False

            else:
                reverseP = reverseP[1:]
                reverseS = reverseS[1:]

        if matchingChar != None and len(reverseS):
            if matchingChar == '.': # match any char
                matchingChar = reverseS[0]

            while reverseS[0] == matchingChar:
                reverseS = reverseS[1:]

        if len(reverseS):
            return False 

        return True
