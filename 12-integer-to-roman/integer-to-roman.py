class Solution:
    def intToRoman(self, num: int) -> str:
        numerals = {
            1000: 'M', 900: 'CM', 
            500: 'D', 400: 'CD', 
            100: 'C', 90: 'XC', 
            50: 'L', 40: 'XL', 
            10: 'X', 9: 'IX', 
            5: 'V', 4: 'IV', 
            1: 'I'}
        res = ''

        for val in numerals:
            if num == 0:
                break
            count = num // val

            for i in range(count):
                res += numerals[val]
            num -= val * count
        
        return res