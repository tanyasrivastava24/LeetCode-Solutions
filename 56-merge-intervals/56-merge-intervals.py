class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res=[]
        intervals=sorted(intervals)
        for interval in intervals:
            if res and interval[0]<=res[-1][1]:
                res[-1][1]=max(res[-1][1],interval[1])
            else:
                res+=[interval]
        return res
        