class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        n=len(nums)
        j=0
        max1=0
        while(j<n):
            if(nums[j]==1):
                c+=1
            else:
                max1=max(max1,c)
                c=0
            j+=1
        return max(max1,c)
