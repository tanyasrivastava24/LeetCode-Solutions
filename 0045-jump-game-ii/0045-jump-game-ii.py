class Solution:
    def jump(self, nums: List[int]) -> int:
        begin=0
        end=0
        jump=0
        while(end<len(nums)-1):
            e=0
            for i in range(begin,end+1):
                e=max(e,i+nums[i])
            begin=end+1
            end=e
            jump+=1
        return jump