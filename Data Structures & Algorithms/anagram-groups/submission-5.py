class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_dict = {}

        for string in strs:
            arr = [0] * 26

            for char in string:
                idx = ord(char) - ord("a")
                arr[idx] += 1

            tup = tuple(arr)

            if tup in new_dict:
                new_dict[tup].append(string)
            else:
                new_dict[tup] = [string]

        return (list(new_dict.values()))
