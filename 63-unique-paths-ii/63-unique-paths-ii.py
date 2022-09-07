class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        s=len(obstacleGrid)
        t=len(obstacleGrid[0])
        dp=[[1 for i in range(t)] for j in range(s)]
        #print(dp)
        flag=False
        for i in range(s):
            if obstacleGrid[i][0]==1 or flag==True:
                dp[i][0]=0
                flag= True
        flag=False
        for j in range(t):
            if obstacleGrid[0][j]==1 or flag==True:
                dp[0][j]=0
                flag=True
    
        for i in range(1,s):
            for j in range(1,t):
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[s-1][t-1]
                
                    
                
                
                
        
        