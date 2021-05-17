class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        total, power = 0, 0
        reversedString = s[::-1]
        
        for c in reversedString:
            # if digit, make sure it's right power of ten (since we're reversed)
            # and add it to current digit total
            
            if c.isdigit():
                total += 10**power * int(c)
                power += 1
            elif c != ' ':
                # if there's a total, add it to the stack as "left"
                if power:
                    stack.append(total)
                    total, power = 0, 0
                # if we see '(' since we reversed we need to evaluate stack
                if c == '(':
                    res = self.evaluate_stack(stack)
                    stack.pop()
                    stack.append(res)
                # add any operators
                else:
                    stack.append(c)
                    
        if power:
            stack.append(total)
            
        return self.evaluate_stack(stack)
                    
    def evaluate_stack(self, stack):
        # evaluate what is in the stack. continue popping
        res = 0

        while stack and stack[-1] != ')':
            c = stack.pop()
            if c == '+':
                res += stack.pop()
            elif c == '-':
                res -= stack.pop()
            else:
                res = c
                
        return res