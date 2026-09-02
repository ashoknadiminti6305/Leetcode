class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        j=len(numbers)-1
        
        while(l<j):
            sum=numbers[l]+numbers[j]
            if(sum==target):
                return [l+1,j+1]
            elif(target<sum):
                j-=1
            else:
                l+=1
        