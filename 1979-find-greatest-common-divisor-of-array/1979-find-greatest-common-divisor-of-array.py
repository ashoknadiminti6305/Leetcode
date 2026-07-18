class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min1=min(nums)
        max1=max(nums)
        while(max1!=0):
            min1,max1=max1,min1%max1
        return min1
        