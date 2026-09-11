from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        newDict = Counter()
        for items in nums:
            newDict[items] += 1
        
        sortedlist = sorted(newDict, key = newDict.get, reverse = True)
        return sortedlist[:k]