
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        
        # dynamic approach - https://www.youtube.com/watch?v=CE2b_-XfVDk
        
        if len(nums) == 0: return 0
        
        dp = [1 for x in range(len(nums))] # least can be 1
        
        # start dp from index-1
        
        for i in range(1, len(dp)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    # update dp array
                    dp[i] = max(dp[i], dp[j]+1)
                    
        # print("dp: ", dp)
        return max(dp)
        
        
        """
        # TLE
        self.length = 0 # has to be longest/maximum
        
        for i in range(len(nums)):
            temp = [nums[i]]
            self.make_temp_arrays(nums[i], nums[i+1:], temp)
            
        return self.length
    
    
    def make_temp_arrays(self, first_number, nums, temp):
        
        # print("temp: ", temp)
        
        if len(nums) == 0:
            return
        
        self.length = max(self.length, len(temp))
        n = 0
        while n < len(nums):
            if nums[n] > first_number:
                self.make_temp_arrays(nums[n], nums[n+1:], temp + [nums[n]])
            else:
                n+=1"""
        
        
        
        
        """
        # continuous subsequence - for subarrays
        if len(nums) in [0,1]:
            return len(nums)
        
        length = 1 # should be maximum
        
        
        # len(nums) is more than 1
        i = 0
        while i < len(nums):
            j = i+2
            while j < len(nums):
                arr = nums[i:j]
                # check 'arr' to be increasing sequence
                last = arr[-1]
                second_last = arr[-2]
                
                if last > second_last:
                    print("potential array: ", arr)
                    length = max(length, len(arr))
                    j+=1
                else:
                    break
            
            i+=1
                
                
        return length"""
             
