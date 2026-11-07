class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        nums.sort()
        return ((nums[len(nums)-1]-1) *(nums[len(nums)-2] - 1))
        