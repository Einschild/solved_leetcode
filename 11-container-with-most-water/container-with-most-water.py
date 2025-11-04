class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left = 0
        right = len(height) - 1

        while left < right:
            leftVal = height[left]
            rightVal = height[right]

            length = 0
            width = right - left

            if leftVal < rightVal:
                length = leftVal
                left += 1
            else:
                length = rightVal
                right -= 1

            area = length * width

            if area > res:
                res = area
        
        return res