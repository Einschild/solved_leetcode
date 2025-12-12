class Solution:
    def toLowerCase(self, s: str) -> str:
        res = ''
        for char in s:
            if ord(char) >= ord('A') and ord(char) <= ord('Z'):
                res += chr(ord(char) + 32)
            else:
                res += char
        return res