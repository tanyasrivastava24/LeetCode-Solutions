class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        d=Counter(s)
        for key,val in d.items():
            if val==1:
                return s.index(key)
            
        return -1