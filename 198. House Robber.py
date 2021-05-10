
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # dynamic approach
        
        # use basic template for the dp array
        
        if len(nums) == 0: return 0
        
        dp = [" " for x in range(len(nums)+1)]
                
        dp[0] = 0
        dp[1] = nums[0] # only 1 house yet -- covered only 0th index from nums
        
        # start the loop as per dp template
        for i in range(1, len(nums)):
            dp[i+1] = max(dp[i], dp[i-1] + nums[i])
            
        # print("new dp: ", dp)
        
        return dp[-1]
        
        
