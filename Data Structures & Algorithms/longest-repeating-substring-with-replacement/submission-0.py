from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0

        count = Counter()

        max_freq = 0

        for r, index in enumerate(s):
            count[index] += 1

            max_freq = max(max_freq, count[index])

            if (r - l + 1 - max_freq) > k:
                count[s[l]] -= 1
                l += 1

        return len(s) - l
