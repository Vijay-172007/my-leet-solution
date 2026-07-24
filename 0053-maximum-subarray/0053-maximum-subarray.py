class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = maxi = nums[0]
        for i in range(1, len(nums)):
            cur = max(nums[i], cur + nums[i])
            maxi = max(maxi, cur)
        return maxi
        