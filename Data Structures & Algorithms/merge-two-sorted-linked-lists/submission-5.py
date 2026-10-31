# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        l = list1
        r = list2
        temp = dummy
        while l and r:
            if l.val <= r.val:
                temp.next = l
                l = l.next
                temp = temp.next
            else:
                temp.next = r
                r = r.next
                temp = temp.next
        if l:
            temp.next = l
        else:
            temp.next =r 
        return dummy.next
