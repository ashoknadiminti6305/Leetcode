class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        a1=[]
        a2=[]
        a3=[0]*len(nums)
        for i in nums:
            if(i>0):
                a1.append(i)
            else:
                a2.append(i)
        s=0
        k=0
        for i in range(len(a3)):
            if(i%2==0):
                a3[i]=a1[s]
                s+=1
            else:
                a3[i]=a2[k]
                k+=1
        return a3
        