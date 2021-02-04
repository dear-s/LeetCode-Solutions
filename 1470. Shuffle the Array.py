class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        
        length = len(nums)
        
        array1 = nums[:length//2]
        array2 = nums[length//2:]
        
        new_array = []
        
        i = 0
        while i < length//2:
            new_array.append(array1[i])
            new_array.append(array2[i])
            
            i+=1
            
        return new_array
    
