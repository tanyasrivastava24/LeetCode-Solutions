class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        s=[]
        for i in range(1,numRows+1):
            s.append([0 for j in range(i)])
        s[0][0]=1
        k=0
        for i in range(1,len(s)):
            j=i+1
            k=0
            while(k<j):
                u=k-1
                try:
                    if(u<0):
                        s[i][k]=0+s[i-1][k]
                    else:
                        s[i][k]=s[i-1][k-1]+s[i-1][k]
                except:
                    s[i][k]=s[i-1][k-1]+0
                k+=1
        print(s)
        return s
        
                
                
            