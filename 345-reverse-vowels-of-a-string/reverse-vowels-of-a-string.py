class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        res = list(s)
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] in vowels and s[right] in vowels:
                res[left], res[right] = res[right], res[left]
                left += 1
                right -= 1
            elif res[left] not in vowels:
                left += 1
            else:
                right -= 1
        
        return ''.join(res)