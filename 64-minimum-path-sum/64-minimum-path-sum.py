class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        s=len(grid)
        t=len(grid[0])
        dp=[[0 for i in range(t)] for j in range(s)]
        #print(dp)
        for i in range(s):
            for j in range(t):
                dp[i][j]=grid[i][j]
        for i in range(s):
            for j in range(t):
                if i==0 and j>0:
                    dp[0][j]+=dp[0][j-1]
                if j==0 and i>0:
                    dp[i][0]+=dp[i-1][0]
                if j>0 and i>0:
                    dp[i][j]+=min(dp[i-1][j],dp[i][j-1])
        return dp[s-1][t-1]