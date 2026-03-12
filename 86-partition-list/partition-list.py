# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        beforex = ListNode(0)
        afterx = ListNode(0)

        cur_beforex = beforex
        cur_afterx = afterx

        curr = head

        while curr:
            if curr.val < x:
                cur_beforex.next = curr
                cur_beforex = cur_beforex.next
            else:
                cur_afterx.next = curr
                cur_afterx = cur_afterx.next
                

            curr = curr.next

        cur_afterx.next = None
        cur_beforex.next = afterx.next

        return beforex.next


     




                

