class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [0] * n
        
        for i in range(n):
            if i < 2:
                arr[i] += i + 1
            else:
                arr[i] += arr[i - 1] + arr[i - 2]

        return arr[n - 1]