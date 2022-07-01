class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #for i in range(len(nums)):
            #for j in range(i+1,len(nums)):
                #sum=nums[i]+nums[j]
                #if sum==target:
                    #return [i,j]
        d={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in d:
                return [d[diff],i]
            d[n]=i
        return
            
        
        