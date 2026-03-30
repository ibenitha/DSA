# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = head
        a = []
        while head != None:
            a.append(head.val)
            head = head.next
        
        a.sort()

        head = l
        i = 0
        while head != None:
            head.val = a[i]
            head = head.next
            i += 1
        head = l

        return head

        