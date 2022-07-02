class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums3=[]
        for value in nums1:
            if value in nums2:
                nums3.append(value)
                nums2.remove(value)
        return nums3