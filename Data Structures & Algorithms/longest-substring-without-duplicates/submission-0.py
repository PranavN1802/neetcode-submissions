class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import Counter
        char_count = Counter()
        max_size = 0
        l = 0
        
        for r, char in enumerate(s):
            char_count[char] += 1

            while char_count[char] > 1:
                char_count[s[l]] -= 1
                l += 1
            max_size = max(max_size, r - l + 1)

        return max_size
