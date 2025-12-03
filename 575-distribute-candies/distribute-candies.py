class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        seen = set(candyType)
        
        res = len(seen)
        if res > len(candyType) // 2:
            res = len(candyType) // 2
        
        return res