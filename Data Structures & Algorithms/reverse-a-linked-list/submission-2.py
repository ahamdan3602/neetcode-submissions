# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
     
        prev = None
        curr = head
        nxt = curr.next

        while nxt != None:
            curr.next = prev
            prev = curr
            print(str(curr.val) + " | " + str(prev.val))
            curr = nxt
            nxt = nxt.next
        head = curr
        head.next = prev

        return head


        