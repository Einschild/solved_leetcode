class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        left = 0
        right = len(s) - 1
        res = list(s)

        while left < right:
            if res[left] in vowels and res[right] in vowels:
                res[left], res[right] = res[right], res[left]
                left += 1
                right -= 1
            elif res[left] not in vowels and res[right] in vowels:
                left += 1
            elif res[right] not in vowels and res[left] in vowels:
                right -= 1
            else:
                left += 1
                right -= 1
        
        return ''.join(res)