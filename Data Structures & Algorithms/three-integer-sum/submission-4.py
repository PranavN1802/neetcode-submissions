class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = []
        length = len(nums)

        nums.sort()

        for index, num in enumerate(nums):

            # Skip duplicate starting values
            if index > 0 and num == nums[index - 1]:
                continue

            if num > 0:
                break

            left = index + 1
            right = length - 1

            while left < right:
                sums = num + nums[left] + nums[right]

                if sums == 0:
                    l.append([num, nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Skip duplicate left values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                elif sums > 0:
                    right -= 1

                else:
                    left += 1

        return l