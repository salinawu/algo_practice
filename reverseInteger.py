class Solution:

    # can also get abs value and reverse, then add '-' if original was negative
    def reverse(self, x: int) -> int:
        intAsStr = str(x)
        returnString = ''
        for index, char in enumerate(intAsStr[::-1]):
            if char == '-': # number is negative and we're done
                returnString = '-' + returnString
            elif not (char == '0' and len(returnString) == 0 and len(intAsStr) > 1): # don't add trailing zeros
                returnString += char

        if -2 ** 31 <= int(returnString) < 2 ** 31:
            return returnString
        else:
            return '0'

# -12000 => -12
