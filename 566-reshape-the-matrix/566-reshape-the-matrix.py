class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat) # rows
        n = len(mat[0]) # columns

        if r*c != m*n: 
            return mat

        mat = [num for l in mat for num in l] 

        reshape = [] 

        for i in range(r):
            row=[]

            for j in range(i*c, (c*i)+c): 
                row.append(mat[j])

            reshape.append(row)

        return reshape
        