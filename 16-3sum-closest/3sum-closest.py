class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = {}

        for i in range(len(nums) - 2):
            x = nums[i]
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = x + nums[j] + nums[k]
                diff = abs(total - target)
                res[diff] = total
                if total < target:
                    j += 1
                else:
                    k -= 1
        return res[min(res.keys())]