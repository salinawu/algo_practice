class Solution:

    # keep track of start and end indices. 
    # if the last index value hasn't been seen, add it and see if length is greater than the current max
    # if the last index value has been seen, "start over" by increasing the start index
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j, res = 0, 0, 0
        seen = []

        while j < len(s) and i < len(s):
            if s[j] in seen:
                seen.remove(s[i])
                i += 1
            else:
                seen.append(s[j])
                j += 1
                res = max(res, j - 1)

        return res