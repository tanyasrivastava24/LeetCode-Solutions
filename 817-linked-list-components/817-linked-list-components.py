# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        result=len(nums)
        while head.next:
            if head.val in nums:
                if head.next.val in nums:
                    result-=1
            head = head.next
        return result
        