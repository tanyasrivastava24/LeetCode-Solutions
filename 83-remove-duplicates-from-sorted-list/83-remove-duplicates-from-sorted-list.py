# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:return None
        dummy=ListNode()
        dummy.next=head
        pre,cur=dummy,head
        while cur.next:
            if cur.val==cur.next.val:
                cur=cur.next
                pre.next=cur
            else:
                cur=cur.next
                pre=pre.next           
        
        return dummy.next