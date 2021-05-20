class Solution:
    numberMapping = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return [i for i in self.numberMapping[digits[0]]]
        sol = []
        for i in self.numberMapping[digits[0]]:
            sol += [i + combo for combo in self.letterCombinations(digits[1:])]
        return sol
            