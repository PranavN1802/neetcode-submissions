class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        best_val = right

        while left <= right:
            mid = (left + right) // 2
            total_time = 0
            for items in piles:
                total_time += math.ceil(items/mid)
            if total_time == h:
                best_val = mid
            if total_time > h:
                left = mid + 1
            else:
                right = mid - 1
                best_val = min(best_val, mid)
            
        return best_val