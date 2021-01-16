
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        
        
        # basically need to insert at index position -- and form a new target array
        
        target = []
        
        for i in range(len(index)):
            target.insert(index[i], nums[i])
            
        # insert operation only
        
        return target
        
       
