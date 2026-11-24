class Solution:
    def isValid(self, s: str) -> bool:
        c=[]
        for i in s:
            if(i=='(' or i=='{' or i=='['):
                c.append(i)
            elif(i==')' or i=='}' or i==']'):
                if(not c):
                    return False
                top=c.pop()
                if(top!='(' and i==')'):
                    return False
                elif(top!='{' and i=='}'):
                    return False
                elif(top!='[' and i==']'):
                    return False
        return len(c)==0
                
        