class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        newDict = {}

        for item in strs:
            test_array = [0] * 26

            for s in item:
                val = ord(s) - ord("a")
                test_array[val] += 1

            new_tuple = tuple(test_array)

            if new_tuple in newDict:
                newDict[new_tuple].append(item)
            else:
                newDict[new_tuple] = [item]

        return list(newDict.values())