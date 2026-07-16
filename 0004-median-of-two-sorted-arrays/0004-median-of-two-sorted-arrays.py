class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x=sorted(nums1+nums2)
        low=0
        hi=len(x)-1
        
        mid=(low+hi)//2
        if(len(x)%2==0):
            return float((x[mid]+x[mid+1])/2)
        else:
            return float(x[mid])

        