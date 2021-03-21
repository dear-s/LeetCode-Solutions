class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        
        str_num = str(N)
        new_str_formed = ""
        
        # use itertools.permutations
        get_list = list(itertools.permutations(str_num))
                
        string_list = []
        
        for ll in get_list:
            make_str = ""
            for t in ll:
                make_str += t
            string_list.append(make_str)
            
        for sl in range(len(string_list)):
            if string_list[sl][0] != '0':
                # check power of 2
                get_decision = self.check_power(int(string_list[sl]))
                if get_decision == True:
                    return True
                
        return False
            
    def check_power(self, num):
        while num > 1 and not num % 2:
            num //= 2
        return num == 1
        
        
        
        
