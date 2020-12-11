class Solution:

    def __init__(self, nums: List[int]):
        
        self.nums = nums
        

    def pick(self, target: int) -> int:
        
        # get all indexes first
        indexes = []
        
        for n in range(len(self.nums)):
            if self.nums[n] == target:
                indexes.append(n)
                
        
        a = random.choice(indexes)
        
        return a


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
   
