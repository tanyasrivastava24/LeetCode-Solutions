class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res=int(b,2)+int(a,2)
        return bin(res)[2:]
        
        
            
            
            
            
        
        