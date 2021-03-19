
class Solution:
    def bulbSwitch(self, n: int) -> int:
        
        
        return int(sqrt(n))
        
#         bulbs = ["off" for x in range(n)]
#         # print("initial bulbs: ", bulbs)
        
#         for i in range(n):
            
#             # first round - switch ON
#             if i == 0:
#                 for index in range(len(bulbs)):
#                     bulbs[index] = "on"
            
#             # last round
#             elif i == n-1:
#                 if bulbs[-1] == "off":
#                     bulbs[-1] = "on"
#                 else:
#                     bulbs[-1] = "off"
                    
#             else:
#                 # toggle every i-th bulb
#                 for index in range(i, len(bulbs), i+1):
#                     if bulbs[index] == "off":
#                         bulbs[index] = "on"
#                     else:
#                         bulbs[index] = "off"
            
#             # print("in between bulbs: ", i, "th: ", bulbs)
        
#         # print("bulbs: ", bulbs)
#         count_on = 0
#         for b in bulbs:
#             if b == "on":
#                 count_on += 1
                
#         return count_on
      
