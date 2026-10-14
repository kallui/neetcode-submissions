# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        # head=[1, 2, 3, 4, 5]

        while curr:
            temp = curr.next    # 2, 3, 4, 5
            curr.next = prev    # curr = 1, Null
            prev = curr         # prev = 1, Null
            curr = temp         # curr = 2,3,4,5
        
        return prev


        