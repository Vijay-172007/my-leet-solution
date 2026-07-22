class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nums[:]=[a for a in nums if a]+[0]*nums.count(0)
        """
        Do not return anything, modify nums in-place instead.
        """
        