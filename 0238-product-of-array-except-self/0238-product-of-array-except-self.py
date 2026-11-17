class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        pre = []
        suf = [0] * len(nums)
        res = [0] * len(nums)
        p = 1
        s = 1
        for i in range(len(nums)):
            pre.append(p)
            p *= nums[i]
        for j in range(len(nums)-1, -1, -1):
            suf[j] = s
            s *= nums[j]
        for i in range(len(nums)):
            res[i] = pre[i] * suf[i]

        return res
                