class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_set = set(nums)
        for index, items in enumerate(nums):
            comp = target - items
            if (comp) in new_set:
                for i in range(len(nums)):
                    if nums[i] == (comp):
                        compIndex = i
                if compIndex != index:        
                    return [index, compIndex]