class Solution:
    def trailingZeroes(self, n: int) -> int:
        res=0
        i=5
        while(i<=n):
            
            res=res+n//i
            i=i*5
        return res
            
        
        
        
                
            
        