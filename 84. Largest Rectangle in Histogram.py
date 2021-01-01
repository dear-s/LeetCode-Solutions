class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/995253/python3-short-simple-increasing-stack-one-pass
        
        answer = 0
        
        stack=[]
        
        heights.append(0) # end the loop
        
        for i in range(len(heights)):
            # index and value
            s = [i, heights[i]]
            
            while stack and stack[-1][1] >= heights[i]:
                # print("stack: ", stack)
                # print("Answer updated: ", answer)
                s = stack.pop()
                answer = max(answer, s[1]*(i-s[0]))
            
            stack.append([s[0], heights[i]])
            
        return answer
        
        
        """
        TIME LIMIT
        # traverse left and right -- greater or equal
        # calculate area from each index point
        
        if len(heights) == 0:
            return 0
        
        total_area = []
        
        for i in range(len(heights)):
            
            cur_height = heights[i]
            
            # left
            count_left = 0
            index = i-1
            while index >= 0 and heights[index] >= cur_height:
                count_left += 1
                index -= 1
                
            # right
            count_right = 0
            index = i+1
            while index < len(heights) and heights[index] >= cur_height:
                count_right += 1
                index += 1
                
            area = cur_height
            
            c = 0
            while c < count_left:
                area += cur_height
                c+=1
                
            cc = 0
            while cc < count_right:
                area += cur_height
                cc += 1
                
            total_area.append(area)
        
        # return max area
        # print("total_area: ", total_area)
        return max(total_area)"""
    
    
