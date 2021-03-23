
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        
        max_prod = 0
        
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                # check for words[i] and words[j]
                
                # go for set - make list, then take set
                # to go ahead, len(set) --  should be null
                
                s1 = set(list(words[i]))
                s2 = set(list(words[j]))
                
                if len(s1.intersection(s2)) == 0:                    
                    max_prod = max(max_prod, len(words[i])*len(words[j]))
                    
        return max_prod
                	
		
	
