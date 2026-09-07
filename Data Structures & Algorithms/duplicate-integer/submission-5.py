class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for items in nums:
            if items in s: 
                return True
            s.add(items)

        return False