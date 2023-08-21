class Solution:
    def nextLargerElement(self,arr,n):
        #code here
        helperStack = []
        res = [-1] * n
        
        for i in range(n-1, -1, -1):
            currTemp = arr[i]
            while helperStack and currTemp >= helperStack[-1]:
                helperStack.pop()
            if helperStack:
                res[i] = helperStack[-1]
            helperStack.append(currTemp)
        return res