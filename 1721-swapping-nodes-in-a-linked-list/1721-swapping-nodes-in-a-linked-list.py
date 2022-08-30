# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow=head
        fast=head
        i=1
        while i<k:
            fast=fast.next
            i+=1
        t=fast
        while fast.next:
            slow=slow.next
            fast=fast.next
        slow.val,t.val=t.val,slow.val
        return head
            