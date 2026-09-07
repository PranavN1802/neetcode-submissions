class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ln = len(nums)
        valid = []

        for i in range(ln-2):
            if nums[i]>0:
                break

            if i>0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1, ln-1
            while left<right:
                current_sum = nums[left] + nums[i] + nums[right]
                if current_sum > 0:
                    right -= 1
                elif current_sum < 0:
                    left += 1

                else:
                    valid.append([nums[left], nums[i], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return valid