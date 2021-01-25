
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        
        # use stacks - explanation - https://www.youtube.com/watch?v=1nbb_RhqpdY (best)
        
        stack = []
        times_pop = 0 # should be len(nums) - k
        
        for n in nums:
            while len(stack) > 0 and stack[-1] > n and times_pop < len(nums) - k:
                # pop and append
                stack.pop()
                times_pop += 1
            
            stack.append(n)
        
        # should be sorted
        
        # remove till we get the len of stack as k
        while len(stack) > k:
            stack.pop()
            
        return stack
