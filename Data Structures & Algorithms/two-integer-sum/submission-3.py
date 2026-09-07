class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newDict = {}
        for index, item in enumerate(nums):
            if (target-item) in newDict:
                return [newDict[target-item], index]
            newDict[item] = index