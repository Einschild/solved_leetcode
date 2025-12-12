class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        ptr = 0
        n = len(bits) - 1
        while ptr < n:
            if bits[ptr] == 1:
                ptr += 2
            else:
                ptr += 1
        
        return ptr == n