class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l=len(s)
        t=['a','e','i','o','u','A','O','E','I','U']
        c1,c2=0,0
        for i in range(l):
            if i<l//2:
                if s[i] in t:
                    c1+=1
            else:
                if s[i] in t:
                    c2+=1
        if c1==c2:
            return True
        return False
        
        
        
        