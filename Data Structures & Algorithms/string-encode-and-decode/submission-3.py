class Solution:

    def encode(self, strs: List[str]) -> str:
        new_string = ""
        for string in strs:
            length = len(string)
            len_4 = "0000" + str(length)
            new_string += len_4[-4:] + string
        return new_string

    def decode(self, s: str) -> List[str]:
        i = 0
        newList = []
        while i<len(s):
            num = int(s[i:i+4])
            # print(num)
            newList.append(s[i+4:(i+num+4)])
            i = i + (num) + 4
        return newList