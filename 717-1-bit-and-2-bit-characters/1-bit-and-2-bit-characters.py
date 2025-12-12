class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        ptr = 0
        while ptr < len(bits) - 1:
            if bits[ptr] == 1:
                ptr += 2
            else:
                ptr += 1
        
        return ptr == len(bits) - 1