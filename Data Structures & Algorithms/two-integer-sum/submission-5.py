class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_dict = {}
        for index, val in enumerate(nums):
            if (target-val) in new_dict:
                return [new_dict[target-val],index]
            new_dict[val] = index
