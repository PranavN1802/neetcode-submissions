class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newset = set()
        for items in nums:
            if items in newset:
                return True
            newset.add(items)

        return False