
class Solution:
    def makeGood(self, s: str) -> str:
        
        
        if len(s) == 0:
            # good string
            return s
        
        if len(s) == 1:
            return s # good
        
        i = 0
        while i < len(s)-1:
            if s[i+1] != s[i] and (s[i+1].lower() == s[i] or s[i].lower() == s[i+1]):
                # one is upper and one is lower
                # remove them
                s = s[:i] + s[i+2:]
                i = 0

            else:
                i+= 1
        
        print("s: ", s)
        return s
                
