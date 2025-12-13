class Solution:
    def climbStairs(self, n: int) -> int:
        n1 = 2
        n2 = 1
        res = 0

        if n <= 2:
            return n
        
        for i in range(2, n):
            res = n1 + n2
            n2 = n1
            n1 = res

        return res