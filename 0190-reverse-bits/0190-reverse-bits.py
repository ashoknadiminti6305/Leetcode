class Solution:
    def reverseBits(self, n: int) -> int:
        temp=n
        b=[]
        for i in range(32):
            b.append(n%2)
            n//=2
        
        sum=0
        for i in b:
            sum=sum*2+i
        return sum