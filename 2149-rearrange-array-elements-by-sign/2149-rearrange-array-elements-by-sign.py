class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        arr=[0]*len(nums)
        p=0
        n=1
        for i in nums:
            if i>0:
                arr[p]=i
                p+=2
            else:
                arr[n]=i
                n+=2
        return arr        