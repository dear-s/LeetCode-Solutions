
        
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        
        N = len(gas) # total stations
        
        index = 0
        while index < len(gas):
            travels = [index] # track the movement and check if it retruns back to the same station
            gas_present = gas[index] # currently present
            cost_to_next = cost[index] # subtract this after moving to next station
            
            j = (index + 1) % N
            while gas_present >= cost_to_next:
                if j not in travels:
                    # move to next
                    gas_present -= cost_to_next
                    gas_present += gas[j]
                    cost_to_next = cost[j]

                    j+=1
                    j = j % N
                else:
                    return index
            
            index += 1
        
        return -1
            
     
