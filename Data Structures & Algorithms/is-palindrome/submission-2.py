class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        s = s.lower()
        for char in s:
            if char.isalnum():
                clean += char
        
        return clean == clean[::-1]
            