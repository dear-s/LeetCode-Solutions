
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        
        
        # traverse linearly
        
        if len(nums) in [0,1]:
            return len(nums)
        
        arr = list(nums)
        count = 0
        
        positive = False
        negative = False
        
        # check first two - and determine increasing or decreasing sign of the array
        if arr[1] - arr[0] > 0:
            positive = True
            count += 2
        if arr[1] - arr[0] < 0:
            negative = True
            count += 2
            
        if arr[1] == arr[0]:
            count += 1
            positive = True
            negative = True
            
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] > 0 and negative == True: # positive
                count += 1
                positive = True
                negative = False
                
            elif nums[i] - nums[i-1] < 0 and positive == True: # negative
                count += 1
                positive = False
                negative = True
                
            
        # print("count: ", count)
        return count
        
        """
        
        # length of wiggle subsequence -- 
        o_nums = []
        for n in nums:
            o_nums.append(n)
        
        self.max_length = 0 # maximize this
        
        array = [] # will form the sequence in this
        
        up = True
        down = True # will decide after first try
        
        # first try
        for i in range(len(nums)):
            
            # give out two directions - true and false both
            self.recursion(nums[i+1:], o_nums, array + [nums[i]], True, False)
            self.recursion(nums[i+1:], o_nums, array + [nums[i]], False, True)
        
        # self.recursion(nums, o_nums, array, up, down)
        print("self.max_length: ", self.max_length)
        return self.max_length
        
        
    def recursion(self, nums, o_nums, array, up, down):
        
        self.max_length = max(self.max_length, len(array))
        
        if len(nums) == 0:
            return
        
        # if self.max_length > len(nums) + len(array):
        #     return
        
        for i in range(len(nums)):
            if up == True and down == False:
                if nums[i] > array[-1]:
                    self.recursion(nums[i+1:], o_nums, array + [nums[i]], False, True)
            elif down == True and up == False:
                if nums[i] < array[-1]:
                    self.recursion(nums[i+1:], o_nums, array + [nums[i]], True, False)
        
        
        """
		
