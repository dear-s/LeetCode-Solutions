class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        
        # obtain string
        # 1. swap any two chars [reorder]
        # 2. transform and swap - every other char [letter frequencies] - get it from the 2 hints
        
        # check the frequencies
        # it should be same - for each
        # look for the cases where you cannot form it - False cases
        
        w_f1 = {}
        for w in word1:
            if w in w_f1:
                w_f1[w] += 1
            else:
                w_f1[w] = 1
                
        freq1 = []
        keys1 = []
        for k,v in w_f1.items():
            freq1.append(v)
            keys1.append(k)
            
        
        w_f2 = {}
        for w in word2:
            if w in w_f2:
                w_f2[w] +=1
            else:
                w_f2[w] = 1
                
        freq2 = []
        keys2 = []
        for k,v in w_f2.items():
            freq2.append(v)
            keys2.append(k)
            
        # sort both freq arrays
        freq1.sort()
        freq2.sort()
        
        # keys should also be same
        keys1.sort()
        keys2.sort()
        
        # check lengths
        if len(freq1) != len(freq2):
            return False
        
        if len(keys1) != len(keys2):
            return False
        
        # any difference - return False
        for a in range(len(freq2)):
            if freq1[a] != freq2[a]:
                return False
        
        for k in range(len(keys1)):
            if keys1[k] != keys2[k]:
                return False
            
        return True
            
            
        
        
        
        
