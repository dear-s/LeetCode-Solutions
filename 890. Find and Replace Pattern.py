
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        
        # make a dictionary first
        # check the mapping
        
        # if pattern is same - check for keys
        
        ans = []
        
        for word in words:
            # check for the word
            if self.checking(word, pattern) == True:
                ans.append(word)
        
        return ans
            
            
    def checking(self, word, pattern):
        
        # make mappings and compare
        if len(word) != len(pattern):
            return False
        
        w_p = {}
        p_w = {}
        
        i = 0
        while i < len(word):
            # compare each letter
            if word[i] in w_p:
                # check for the pattern letter
                if w_p[word[i]] != pattern[i]:
                    return False
            else:
                # check if pattern has been given to any word letter
                if pattern[i] in p_w:
                    return False
                else:
                    w_p[word[i]] = pattern[i]
                    p_w[pattern[i]] = word[i]
            
            i+=1
            
        return True
