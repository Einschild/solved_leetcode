class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        newPlants = 0
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 1:
                i += 2
            elif i == len(flowerbed) - 1 or flowerbed[i + 1] == 0 :
                newPlants += 1
                i += 2
            else:
                i += 3
        return newPlants >= n