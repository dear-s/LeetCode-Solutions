
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        
        
        # kth from first, kth from second ---- swap
        array = []
        
        h1 = head
        while h1:
            array.append(h1.val)
            h1 = h1.next
            
        # print("array: ", array)
        
        first_value = array[k-1]
        last_value = array[-k]
        
        array[k-1] = last_value
        array[-k] = first_value
        
        # make linked list from it
        new_head = ListNode(array[0])
        h2 = new_head
        
        for i in range(1, len(array)):
            new_node = ListNode(array[i])
            h2.next = new_node
            h2 = h2.next
            
        return new_head
        
        
