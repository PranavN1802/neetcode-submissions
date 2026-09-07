from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap1 = defaultdict(list)
        for word in strs:

            count_arr = [0] * 26

            for c in word:
                count = ord(c) - ord("a")
                count_arr[count] += 1

            hashmap1[tuple(count_arr)].append(word)

        return list(hashmap1.values()) 