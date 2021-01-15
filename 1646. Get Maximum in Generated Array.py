class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        
        # array - length - n+1
        
        # [0,1,...]
        
        # make an array
        array = ["" for x in range(n+1)]
        
        for i in range(n+1):
            # 0 to n
            if i == 0:
                array[0] = 0
            if i == 1:
                array[1] = 1
                
            if 2 * i <= n:
                if array[i] != "":
                    array[2*i] = array[i]
                
            if (2 * i) + 1 <= n:
                if array[i] != "" and array[i+1] != "":
                    array[(2*i)+1] = array[i] + array[i+1]
                
                
        return max(array)
                
                
        
