class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        
        # word1 and word2
        # represent same string - concatenated in order
        
        string1 = ""
        string2 = ""
        
        for w1 in word1:
            string1 += w1
            
        for w2 in word2:
            string2 += w2
        
        if string1 == string2:
            return True
        
        return False
    
    
