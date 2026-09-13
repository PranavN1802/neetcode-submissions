class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        win_size = len(s1)
        
        if win_size > len(s2):
            return False

        count = Counter(s1)

        items_need_match = len(count)
   
        for index, r in enumerate(s2):
            count[r] -= 1

            if count[r] == 0:
                items_need_match -= 1

            if index >= win_size:
                left_char = s2[index - win_size]

                count[left_char] += 1

                if count[left_char] == 1:
                    items_need_match += 1

            if items_need_match == 0:
                return True
        
        return False





        