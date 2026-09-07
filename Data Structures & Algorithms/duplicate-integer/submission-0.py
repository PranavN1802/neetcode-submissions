class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_set = set()
        for item in nums:
            if item in new_set:
                return True
            new_set.add(item)
        return False 