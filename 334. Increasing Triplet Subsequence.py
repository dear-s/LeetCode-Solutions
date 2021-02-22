
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        temp = []
        self.check = False
        
        for i in range(len(nums)):
            a = self.rec(nums[i+1:], temp + [nums[i]])
            if a == True:
                return True
        
        return False
    
    
    def rec(self, nums, temp):
        
        if len(temp) == 3 and self.check == False:
            self.check = True
            return True
        
        if self.check == False:
            for i in range(len(nums)):
                if nums[i] > temp[-1]:
                    self.rec(nums[i+1:], temp + [nums[i]])
        else:
            return True
        
        return False
            
