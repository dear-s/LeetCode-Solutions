
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        # length of the array = k (length)
        # sum of the array = n (target)
        
        numbers = []
        for i in range(1,10):
            numbers.append(i)
        
        self.output = [] # unique set of numbers
        
        # no duplicate combinations
        temp = []
        self.recursion(k, n, numbers, temp)

        return self.output
        
        
    def recursion(self, k, n, numbers, temp):
        
        if len(temp) == k and sum(temp) == n and temp not in self.output:
            self.output.append(temp)
            return
        
        for i in range(len(numbers)):
            self.recursion(k, n, numbers[i+1:], temp + [numbers[i]])
          
