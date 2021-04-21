

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        
        if len(tokens) == 0:
            return 0
        if len(tokens) == 1:
            return tokens[0]
        
         # operators follow their operands
        
        operators = ["+", "-", "*", "/"]
        
        stack = []
        for i in tokens:
            if i in operators:
                b = stack.pop()
                a = stack.pop()
                operator = i
                
                eval_string = ""
                eval_string += str(a)
                eval_string += operator
                eval_string += str(b)
                answer = int(eval(eval_string))
                
                stack.append(answer)
            else:
                stack.append(i)
                
        return stack[0]
                
          
