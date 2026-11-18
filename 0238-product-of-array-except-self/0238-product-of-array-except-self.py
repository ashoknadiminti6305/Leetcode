class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        pre = [0]*len(nums)
        p=1
        s=1
        for i in range(len(nums)):
            pre[i]=p
            p*=nums[i]
        for j in range(len(nums)-1,-1,-1):
            pre[j]=s*pre[j]
            s*=nums[j]
        return pre            