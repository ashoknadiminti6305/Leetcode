class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        k=sorted(heights)
        c=0
        for i in range(len(heights)):
            if(heights[i]!=k[i]):
                c+=1
        return c
        