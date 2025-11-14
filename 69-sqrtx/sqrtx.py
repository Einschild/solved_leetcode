class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        low = 1
        high = x // 2
        res = 0

        while low <= high:
            mid = (low + high) // 2
            midSq = mid * mid
            if midSq < x:
                res = mid
                low = mid + 1
            elif midSq > x:
                high = mid - 1
            else:
                return mid
        
        return res