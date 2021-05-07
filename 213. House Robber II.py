
 class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # now they are arranged in circle
        
        # 1 - max(lastone, secondlastone + presentone)
        # 2 - break into two arrays and take the max out of it
        
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        
        first = self.houseRobber1(nums[1:])
        second = self.houseRobber1(nums[:-1])
        
        ans = max(first, second)
        return ans
    
    
    def houseRobber1(self, nums):
        
        dp = [0 for x in range(len(nums)+1)]
        
        dp[0] = 0
        dp[1] = nums[0]
        
        for i in range(1, len(nums)):
            dp[i+1] = max(dp[i], dp[i-1] + nums[i])
            
        return dp[-1]
        
        
