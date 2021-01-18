class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        
        # dp - make a matrix
        #          a  e  i  o  u
        #   n = 1  1  1  1  1  1
        #   n = 2  5  4  3  2  1
        #   n = 3  15 10 6  3  1
        #   n = 4  35 20 10 4  1
        
        # explanation - https://www.youtube.com/watch?v=gdt7HQF56OI
        
        
        mat = [[1,1,1,1,1] for x in range(n)]
        
        # print("initializing matrix: ", mat)
        
        for r in range(1, n):
            for i in range(5):
                # above row -- sum up all - from that index to the last
                mat[r][i] = 0
                for column in range(i, 5):
                    mat[r][i] += mat[r-1][column]
                
                
        # print("final matrix: ", mat)
        last_row = mat[-1]
        
        return sum(last_row)
        
