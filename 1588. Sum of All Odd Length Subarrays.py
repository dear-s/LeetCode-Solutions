class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        
        s = 0
        
        i = 0
        while i < len(arr):
            j = i+1
            while j <= len(arr):
                
                # code
                array = arr[i:j]                
                s += sum(array)
                
                j+=2
                
            i+=1
            
            
        return s
        
