class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = [1]*length
        postfix = [1]*length
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
          postfix[i] = postfix[i+1] * nums[i+1]
        result = [a * b for a, b in zip(prefix, postfix)]
        return(result)
