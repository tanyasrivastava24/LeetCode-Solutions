class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix)):
                if i!=j:
                    matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
                    
                    
       # print(matrix)
        
        c=len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])//2):
                t=matrix[i][j]
                matrix[i][j]=matrix[i][c-j-1]
                matrix[i][c-j-1]=t
       # print(matrix)
            
        