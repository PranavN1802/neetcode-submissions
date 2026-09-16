from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = Counter()
        for i in range(len(s)):
            count[s[i]] += 1
            count[t[i]] -= 1
        
        for values in count.values():
            if values != 0:
                return False
        
        return True

