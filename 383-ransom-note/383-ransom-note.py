class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        r=Counter(ransomNote)
        c=Counter(magazine)
        if r&c==r:
            return True
        return False
        