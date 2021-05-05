class Solution:
    # https://stackoverflow.com/questions/28777219/basic-program-to-convert-integer-to-roman-numerals
    
    def intToRoman(self, num: int) -> str:
        digitPlace = 0 
        written_num = ""
        
        while num > 0:
            digit = num % 10
            
            if digitPlace == 0:
                if digit < 4:
                    written_num = 'I' * digit + written_num
                elif digit == 4:
                    written_num = 'IV' + written_num
                elif digit == 9:
                    written_num = 'IX' + written_num
                else:
                    written_num = 'V' + ('I' * (digit - 5)) + written_num
                    
            elif digitPlace == 1:
                if digit < 4:
                    written_num = 'X' * digit + written_num
                elif digit == 4:
                    written_num = 'XL' + written_num
                elif digit == 9:
                    written_num = 'XC' + written_num
                else:
                    written_num = 'L' + ('X' * (digit - 5)) + written_num
                    
            elif digitPlace == 2:
                if digit < 4:
                    written_num = 'C' * digit + written_num
                elif digit == 4:
                    written_num = 'CD' + written_num
                elif digit == 9:
                    written_num = 'CM' + written_num
                else:
                    written_num = 'D' + ('C' * (digit - 5)) + written_num
                    
            else:
                written_num = 'M' * digit + written_num
                        
            
            num = floor(num / 10)
            digitPlace += 1
            
        
        return written_num 