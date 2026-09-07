class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict1 = []
        for item in nums:
            if item not in dict1:
                dict1.append(item)
            else:
                return True
        return False
