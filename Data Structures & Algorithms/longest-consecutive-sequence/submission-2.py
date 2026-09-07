class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        largest_seq = 0
        start = set()
        for items in nums:
            start.add(items)

      # now find the starting cells
        for val in nums:
            if (val-1) not in start:
                length = 0
                cur_val = val

                while cur_val in start:
                    length += 1
                    cur_val += 1
                largest_seq = max(largest_seq, length)

        return largest_seq