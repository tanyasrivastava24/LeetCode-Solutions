class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        res=[]
        intervals=sorted(intervals)
        print(intervals)
        for inter in intervals:
            if res and inter[0]<=res[-1][1]:
                res[-1][1]=max(res[-1][1],inter[1])
            else:
                res+=[inter]
        return res