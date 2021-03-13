class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
        set_string=set()
        
        # possible k length substrings from s
        # no need to calculate all the substrings possible
        
        for i in range(len(s)-k+1):
            set_string.add(s[i:i+k])
        
        if len(set_string) == 2**k:
            return True
            
        return False
        
        """# generate all the codes - binary - of length 'k'
        # make sure if each one of them is a substring of string 's'
        
        self.all_codes = []

        self.rec(k, "")

        print("self.all_codes: ", self.all_codes)

        # check substrings
        all_possible = {}
        for i in range(len(s)-k+1):
            all_possible[s[i:i+k]] = 1

        print("all_possible: ", all_possible)

        # check
        for code in self.all_codes:
            if code not in all_possible:
                return False

        return True



    def rec(self, k, first):

        if len(first) == k:
            if first not in self.all_codes:
                self.all_codes.append(first)
            return

        self.rec(k, first + "0")
        self.rec(k, first + "1")
        """
        
