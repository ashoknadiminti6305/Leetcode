class Solution:
    def mirrorDistance(self, n: int) -> int:
        if(n>=10):

            rev=int(str(n)[::-1])
            return abs(n-rev)
        else:
            return 0
        
            
        