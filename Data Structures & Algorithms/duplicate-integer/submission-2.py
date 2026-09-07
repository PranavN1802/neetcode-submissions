class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_set = set()
        for item in nums:
            if item not in new_set:
                new_set.add(item)
            else:
                return True
        return False

