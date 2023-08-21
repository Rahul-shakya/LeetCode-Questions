class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        helperStack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1,-1):
            currTemp = temperatures[i]

            while helperStack and temperatures[helperStack[-1]] <= currTemp:
                helperStack.pop()

            if helperStack:
                res[i] = helperStack[-1] - i
            
            helperStack.append(i)

        return res




        