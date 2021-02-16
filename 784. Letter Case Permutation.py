class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        
        self.ans = []
        string = ""
        
        for s in S:
            if s.isalpha():
                string += s.lower()
            else:
                string += s
                
        index = len(string)-1
        self.rec(string, index)
        return self.ans
        
        
    def rec(self, string, index):
        
        if index < 0:
            if string not in self.ans:
                self.ans.append(string)
            return
        
        if string[index].isalpha():
            # 2 ways -- 
            # make upper
            self.rec(string[:index] + string[index].upper() + string[index+1:], index-1)
            
            # keep it lower
            self.rec(string, index-1)
            
        else:
            # decrement simply
            self.rec(string, index-1)
