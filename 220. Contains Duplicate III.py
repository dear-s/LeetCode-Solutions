
        
        
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        
        
        # at most t - values in the array
        # at most k - indices
        
        array = [] # [[index, value], [i,v], [i,v]]
        
        for i in range(len(nums)):
            array.append([i, nums[i]])
        
        array.sort(key = lambda x:x[1]) # sorted wrt values        
        
        i = 0
        while i < len(array):
            j = i+1
            # check with values
            while j < len(array) and abs(array[i][1] - array[j][1]) <= t:
                # check index
                if abs(array[i][0] - array[j][0]) <= k:
                    return True
                j+=1
            i+=1
            
        return False
        
        
        """
        # TLE
        if len(nums) in [0,1]:
            return False
        
        if len(nums) < k:
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    diff = abs(nums[i] - nums[j])
                    if diff <= t:
                        return True
        
        for i in range(len(nums)):
            for j in range(i+1, i+k+1):
                # abs diff in values
                if j < len(nums):
                    difference_in_vals = abs(nums[i] - nums[j])
                    if difference_in_vals <= t:
                        return True
        
        return False"""
    
  
