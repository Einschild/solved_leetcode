class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        seen = defaultdict(int)
        for candy in candyType:
            seen[candy] += 1
        
        res = len(seen)
        if res > len(candyType) // 2:
            res = len(candyType) // 2
        
        return res