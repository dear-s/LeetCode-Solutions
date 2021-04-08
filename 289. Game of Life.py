	
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        original_board = [["" for x in range(len(board[0]))] for y in range(len(board))]
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                original_board[i][j] = board[i][j]
                        
        # modify board
        for i in range(len(board)):
            for j in range(len(board[0])):
                # all 8 neighbors
                neighbors = []
                total_live = 0
                
                # upper-left
                a = self.call_indexes(i-1, j-1, original_board)
                if a == 1: total_live += 1
                # up
                b = self.call_indexes(i-1, j, original_board)
                if b == 1: total_live += 1
                # upper-right
                c = self.call_indexes(i-1, j+1, original_board)
                if c == 1: total_live += 1
                # left
                d = self.call_indexes(i, j-1, original_board)
                if d == 1: total_live += 1
                # right
                e = self.call_indexes(i, j+1, original_board)
                if e == 1: total_live += 1
                # botton-left
                f = self.call_indexes(i+1, j-1, original_board)
                if f == 1: total_live += 1
                # bottom
                g = self.call_indexes(i+1, j, original_board)
                if g == 1: total_live += 1
                # bottom-right
                h = self.call_indexes(i+1, j+1, original_board)
                if h == 1: total_live += 1
                
                neighbors.append(a)
                neighbors.append(b)
                neighbors.append(c)
                neighbors.append(d)
                neighbors.append(e)
                neighbors.append(f)
                neighbors.append(g)
                neighbors.append(h)
                                
                
                # 1. live to die [neighbors live -- if less than 2]
                if board[i][j] == 1 and total_live < 2:
                    board[i][j] = 0
                
                # 2. live to live [live -- 2 or 3]
                if board[i][j] == 1 and total_live == 2 or total_live == 3:
                    board[i][j] = 1
                
                # 3. live to die [live > 3]
                if board[i][j] == 1 and total_live > 3:
                    board[i][j] = 0
                    
                # 4. die to live [live = 3 times]
                if board[i][j] == 0 and total_live == 3:
                    board[i][j] = 1
                
                
    def call_indexes(self, row, col, board):
        if row<0 or col<0 or row>=len(board) or col>=len(board[0]):
            return
        
        return board[row][col]
    
    
