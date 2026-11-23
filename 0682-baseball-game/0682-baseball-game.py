class Solution:
    def calPoints(self, operations: list[str]) -> int:
        c=[]
        for i in operations:
            if(i=="C"):
                c.pop()
            elif(i=="D"):
                c.append((c[-1])*2)
            elif(i=="+"):
                c.append(c[-1]+c[-2])
            else:
                c.append(int(i))
        return sum(c)
        