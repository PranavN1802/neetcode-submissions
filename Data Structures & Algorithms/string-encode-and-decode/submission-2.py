class Solution:

    def encode(self, strs: List[str]) -> str:
        new_string = ""
        for items in strs:
            x = len(items)
            if x<10:
                x = "000" + str(x)
            elif x<100:
                x = "00" + str(x)
            else:
                x = "0" + str(x)

            new_string += (x + items)
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