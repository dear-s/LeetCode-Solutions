
class Solution:
    def interpret(self, command: str) -> str:
        
        
        output = []
        
        i = 0
        while i < len(command):
            if command[i] == "G":
                output.append("G")
                i+=1
                
            elif command[i] == "(":
                # check next
                if i != len(command)-1 and command[i+1] == ")":
                    output.append("o")
                    i+=2
                elif i != len(command)-3 and command[i+1] == "a" and command[i+2] == "l" and command[i+3] == ")":
                    output.append("al")
                    i+=4
                
        # convert output into string
        
        string = "".join(x for x in output)
        
        return string
        
