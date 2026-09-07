class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        clean = ""
        for char in s:
          if char.isalnum():
            clean += char

        return clean == clean[::-1]