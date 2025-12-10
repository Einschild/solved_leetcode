class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1Map = defaultdict(int)
        n2Map = defaultdict(int)
        res = []

        for num in nums1:
            n1Map[num] += 1
        for num in nums2:
            n2Map[num] += 1

        for num, count in n1Map.items():
            if num in n2Map.keys():
                res += [num for _ in range(min(n1Map[num], n2Map[num]))]
        
        return res