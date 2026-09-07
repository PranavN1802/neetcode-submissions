class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for item in nums:
            dic[item] = dic.get(item,0) + 1
        
        sortedlist = sorted(dic, key = dic.get, reverse = True)
        return sortedlist[:k]