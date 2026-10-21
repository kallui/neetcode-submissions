# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # get half point

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        
        # reverse second half
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge
        while prev:
            t1 = head.next
            t2 = prev.next
            
            head.next = prev
            prev.next = t1
            
            head = t1
            prev = t2
            



