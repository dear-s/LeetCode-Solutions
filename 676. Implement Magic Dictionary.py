
   
class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = []
        

    def buildDict(self, dictionary: List[str]) -> None:
        
        for d in dictionary:
            self.dict.append(d)
            
        # print("dictionary: ", self.dict)
        

    def search(self, searchWord: str) -> bool:
        
        same_lens = []
        for d in self.dict:
            if len(d) == len(searchWord):
                same_lens.append(d)
                
        # print("to choose from, same_lens: ", same_lens)
        
        
        if len(same_lens) == 0:
            return False
        
        # find if any
        
        for word in same_lens:
            # only one
            count = 0
            for i in range(len(searchWord)):
                if searchWord[i] != word[i]:
                    count += 1
                    
            if count == 1:
                return True
            
        return False
        
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)    

