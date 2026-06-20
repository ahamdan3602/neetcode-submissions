# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:


        cnt = 0

        curr = head
        while curr != None:
            if cnt == 1000:
                return True
            cnt += 1
            curr = curr.next

        return False
        