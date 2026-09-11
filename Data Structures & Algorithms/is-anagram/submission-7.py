from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = Counter()
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            count[s[i]] += 1
            count[t[i]] -= 1

        for items in count.values():
            if items != 0:
                return False

        return True        