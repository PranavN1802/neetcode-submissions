class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pt = 0
        right_pt = len(numbers) - 1
        sum = numbers[left_pt] + numbers[right_pt]
        while(sum != target):
            if sum<target:
                left_pt += 1
            else:
                right_pt -= 1
            sum = numbers[left_pt] + numbers[right_pt] 
        return [left_pt+1, right_pt+1]