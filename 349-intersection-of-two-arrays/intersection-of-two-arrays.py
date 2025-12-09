class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Set = set(nums1)
        nums2Set = set(nums2)
        res = []

        for num in nums2Set:
            if num in nums1Set:
                res.append(num)
        
        return res