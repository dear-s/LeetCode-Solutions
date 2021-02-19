    
class Solution:
    def integerBreak(self, n: int) -> int:
        
                
        n_ans = {}
        n_ans[2] = 1
        n_ans[3] = 2
        n_ans[4] = 4
        
        # can apply dp - since answer can only have 2's and 3's
        
        if n in n_ans:
            return n_ans[n]
        
        dp = ["" for x in range(n+1)]
        # index will be the number
        
        dp[0] = 1 # for 0
        dp[1] = 1 # for 1
        dp[2] = 1 # for 2 = 1+1 and 1*1
        
        for i in range(3, n+1):
            dp[i] = max(dp[i-2] * 2, dp[i-3] * 3)
            
        return dp[n]
            
        
#         # recursion approach 
        
#         nums = [] # potential multiples
#         for i in range(1,n):
#             nums.append(i)
        
#         temp = []        
#         self.combs = [] # store all combs and then maximize product from them
#         self.rec(nums, temp, n)
        
#         max_prod = 1
        
#         for comb in self.combs:
#             prod = 1
#             for a in comb:
#                 prod *= a
#             max_prod = max(max_prod, prod)
            
#         return max_prod
        
        
#     def rec(self, nums, temp, n):
        
#         if len(temp) > 0 and sum(temp) == n:
#             self.combs.append(temp)
#             return
        
#         if sum(temp) > n:
#             return
        
#         for i in range(len(nums)):
#             if nums[i] + sum(temp) <= n:
#                 self.rec(nums, temp + [nums[i]], n)
            
