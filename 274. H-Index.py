class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        
        # h-index
        
        # sort the citations array
        # trace back from the front and find a position h index such that after that value will only increase
        # and length will the that number - h index only
        
        if len(citations) == 0:
            return 0
        
        h = 0
        
        citations.sort()
        
        for i in range(len(citations)):
            get_value = citations[i]
            right_side_array_length = len(citations[i:])
            if get_value >= right_side_array_length:
                h = max(h, right_side_array_length)
                
        
        return h
          
