class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:


        n1_2 = {}
        count = 0
        
        for n in nums:
            if n < k:
                if k-n in n1_2:
                    # count and delete the key
                    count += 1
                    if len(n1_2[k-n])==0:
                        del n1_2[k-n]
                    else:
                        n1_2[k-n].pop()
                else:
                    if n not in n1_2:
                        n1_2[n] = []
                    else:
                        n1_2[n].append(n)
        
                
        return count

        
        
        """nums.sort()
    
        count = 0
    
        i = 0
        while i < len(nums) and nums[i] <= k:
            if k-nums[i] in nums[i+1:]:
                # remove
                get_index = nums[i+1:].index(k-nums[i])
                nums.pop(get_index+i+1)
                nums.pop(i)
                
                count += 1
                
            else:
                i+=1
         
        return count"""
