class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        new_dict = {}
        for num in nums:
            if num in new_dict:
                new_dict[num] += 1
            else:
                new_dict[num] = 1
        
        sort_list = sorted(new_dict, key = new_dict.get, reverse = True)
        return sort_list[:k]