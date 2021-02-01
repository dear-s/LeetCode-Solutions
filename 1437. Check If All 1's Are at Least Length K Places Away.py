
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        
        # check the length of 1s in the array
        # distance should be more than or equal 'k'
        
        loc = float('inf') # store first instance of 1
        
        index = 0
        found_first = False
        while index < len(nums) and found_first == False:
            if nums[index] == 1:
                loc = index
                found_first = True
            index += 1
                
        if found_first == False:
            return True
        
        i = loc +1
        while i < len(nums):
            if nums[i] == 1:
                # calculate distance
                if abs(i - loc) <= k:
                    return False
                loc = i
            i+=1
                    
        return True
