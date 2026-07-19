class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if(num==1):
            return True
        left=1
        ri=num
        while(left<=ri):
            mid=left+(ri-left)//2
            sq=mid*mid
            if(sq==num):
                return True
            elif(sq>num):
                ri=mid-1
            else:
                left=mid+1
        return False

        