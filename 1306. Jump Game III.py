

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        
        # need to jump - right or left
        # stop when -- repeating pattern starts
        # or found 0 in the array
        
        # recursion
        
        self.found = False
        self.pattern = []
        self.rec(arr, start)
        
        if self.found == True:
            return True
        
        
    def rec(self, arr, index):
        
        # check for repeating pattern
        if index in self.pattern:
            return
        
        value = arr[index]
        
        if value == 0:
            self.found = True
            return
        
        self.pattern.append(index)
        
        # left
        if index - value >= 0:
            self.rec(arr, index-value)
            
            
        # right
        if index + value < len(arr):
            self.rec(arr, index+value)
