class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newset = {}
        for index, items in enumerate(nums):
            if (target-items) in newset:
                return [newset[target-items], index]
            newset[items] = index
        
