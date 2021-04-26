class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        
        output = ""
        rows = [[] for i in range(numRows)]

        middle_index_max = numRows - 2
        mod_num = numRows + middle_index_max
        
        for index, char in enumerate(s):
            comparator = index % mod_num
            
            # case where the number is on the diagonal
            if comparator >= numRows:
                rows[middle_index_max - (comparator % numRows)].append(char)

            # all other cases
            else:
                rows[comparator].append(char)
        
        for row in rows:
            for char in row:
                output += char

        return output


# 0       6       12
# 1    5  7    11 13
# 2  4    8  10   14
# 3       9       15

# 0 - - - - 10 - - - -  20
# 1 - - - 9 11 - - - 19 21
# 2 - - 8 - 12 - - 18 - 22
# 3 - 7 - - 13 - 17 - - 23
# 4 6 - - - 14 16 - - - 24
# 5 - - - - 15  - - - - 25