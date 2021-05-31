class Solution:
    def judgeCircle(self, moves: str) -> bool:
        path = [0,0]
        
        for i in moves:
            if(i == 'U'):
                path[0]+=1
            elif(i == 'D'):
                path[0]-=1
            elif(i == 'L'):
                path[1]+=1
            elif(i == 'R'):
                path[1]-=1
        
        if(path[0] == 0 and path[1] == 0):
            return True
        else:
            return False


s = Solution()
print(s.judgeCircle("UDUDLRLR"))