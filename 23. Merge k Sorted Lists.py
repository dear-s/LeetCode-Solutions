

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        # base cases
        if len(lists) == 0: return None
        if len(lists) == 1: return lists[0]
        
        # convert into list, then linked list
        arr =[]
        
        for head in lists:
            # head is a linked list
            while head:
                arr.append(head.val)
                head = head.next
                        
        # sort arr
        arr.sort()
        
        # make linked list from this
        if len(arr) == 0: return None
        
        new_node = ListNode()
        new_node.val = arr[0]
        return_node = new_node
        
        for i in range(1, len(arr)):
            next_node = ListNode()
            next_node.val = arr[i]
            new_node.next = next_node
            new_node = next_node
            
        return return_node
        
