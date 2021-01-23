class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        
        # diagonal sort
        rows = len(mat)
        cols = len(mat[0])
        
        
        # diagonals - keys 'and' array of [(r,c), val] as value
        
        #total diagonals can be find out
        # eg1 ---- row = 3, col = 4...... diagonal = row + col -1 = 6
        diag = 6
        
        diag_array = {}
        
        for d in range(diag):
            diag_array[d] = []
            
        # print("initialize diag_array: ", diag_array)
        
        # traverse and alot diagonals -- first row and first col (from second col)
        
        # first row
        d_counter = 0
        for c in range(cols):
            find_array = []
            header = mat[0][c]
            # find it's diagonal elements
            rr = 0
            cc = c
            while rr < rows and cc < cols:
                find_array.append([[rr,cc], mat[rr][cc]])
                rr += 1
                cc += 1
                
            diag_array[d_counter] = find_array
            d_counter += 1
            
            
        # first col -- from second row
        for r in range(1, rows):
            find_array = []
            header = mat[r][0]
            # find it's diagonal elements
            rr = r
            cc = 0
            while rr < rows and cc < cols:
                find_array.append([[rr,cc], mat[rr][cc]])
                rr += 1
                cc += 1
            
            diag_array[d_counter] = find_array
            d_counter += 1
            
        # print("diag_array: ", diag_array)
        
        for diag, array in diag_array.items():
            value_array = []
            index_array = []
            for arr in array:
                # second index is the value
                value_array.append(arr[1])
                index_array.append(arr[0])
                
            # sort the values
            value_array.sort()
            
            # place the values as per the index_array elements
            for ind in range(len(index_array)):
                mat[index_array[ind][0]][index_array[ind][1]] = value_array[ind]
                
        
        return mat
        
            
