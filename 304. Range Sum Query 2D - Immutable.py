
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        
        if len(self.matrix) == 0:
            return None
        
        # dynamic array - approach
        # reference - https://www.youtube.com/watch?v=PwDqpOMwg6U
        self.dp = [[0 for c in range(len(self.matrix[0])+1)] for r in range(len(self.matrix)+1)]
            
        for i in range(1, len(self.dp)):
            for j in range(1, len(self.dp[0])):
                self.dp[i][j] = self.dp[i-1][j] + self.dp[i][j-1] - self.dp[i-1][j-1] + self.matrix[i-1][j-1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1
        
        answer = self.dp[row2][col2] - self.dp[row1-1][col2] - self.dp[row2][col1-1] + self.dp[row1-1][col1-1]
        return answer
        
        
        """
        TLE
        sum = 0
        
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                sum += self.matrix[i][j]
                
        return sum"""
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
		
