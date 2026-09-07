from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        newDict = {}
        for item in strs:
            count = [0] * 26
            for s in item:
                index = ord(s) - ord("a")
                count[index] += 1
            
            if tuple(count) not in newDict:
                newDict[tuple(count)] = []
            newDict[tuple(count)].append(item)

        return (list(newDict.values()))