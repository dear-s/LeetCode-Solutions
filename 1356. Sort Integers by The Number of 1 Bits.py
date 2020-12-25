class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        
        # number -> count of 1's
        count_num = {}
        
        for a in arr:
            # get_binary = self.dec_to_bin(a)
            get_count = self.dec_to_bin(a)
            
            if get_count in count_num:
                count_num[get_count].append(a)
            else:
                count_num[get_count] = [a]
                
        
        # sort
        count_array = []
        
        for k,v in count_num.items():
            v.sort()
            count_array.append([k,v])
            
        count_array.sort(key = lambda x:x[0])
        
        output = []
            
        for listt in count_array:
            output.append(listt[1])
            
        answer = []
        
        for o in output:
            for oo in o:
                answer.append(oo)
                
        return answer
        
        
    def dec_to_bin(self, number):
        
        # convert decimal to binary
        binary = []
        count_1 = 0
        
        while number > 0:
            rem = number %2
            number = number // 2
            
            if rem == 1:
                count_1 += 1
            
            binary.append(rem)
            
        # reverse binary
        binary = binary[::-1]
        
        # return binary
        return count_1
        
        
        
