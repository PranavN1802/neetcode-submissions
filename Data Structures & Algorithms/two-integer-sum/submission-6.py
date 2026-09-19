class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hSet = {}
        for index, num in enumerate(nums):
            if (target - num) in hSet:
                return ([hSet[target-num], index])
            hSet[num] = index