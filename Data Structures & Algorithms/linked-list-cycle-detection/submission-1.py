# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dic = {}

        curr = head
        while curr != None:
            if curr not in dic:
                dic[curr] = "Visited"
                curr = curr.next
            else:
                return True
        
        return False
