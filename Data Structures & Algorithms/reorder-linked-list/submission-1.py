# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        

        arr = []

        temp = head
        while temp != None:
            arr.append(temp.val)
            temp = temp.next
        


        flip = False
        res = []
        l, r = 0, len(arr) - 1
        while l <= r:
            if flip:
                res.append(arr[r])
                flip = False
                r -= 1 
            else:
                res.append(arr[l])
                flip = True
                l += 1
        print(res)
        temp = head

        i = 0
        while temp != None:
            temp.val = res[i]
            temp = temp.next
            i += 1


