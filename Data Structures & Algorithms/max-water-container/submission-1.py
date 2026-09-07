class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        left = 0
        right = len(heights) - 1

        while left<right:
            LH = heights[left]
            RH = heights[right]
            area = (right-left)*(min(LH,RH))
            maxA = max(area, maxA)
            if LH<RH:
                left += 1
            elif LH>RH:
                right -= 1
            else:
                left+=1
                right-=1
            
        return maxA
