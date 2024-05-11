# bestSum
# from dynamic programming video YT
# https://www.youtube.com/watch?v=oBt53YbR9Kk&t=11470s
# https://leetcode.com/playground/Ux7hUcVM
# Timestamp: 01:52:06


from typing import List

# in this we cannot return early because we have to check all combinations
def bestSumNoDP(target, arr):
    if target == 0:
        return []
    if target < 0:
        return None
    ans = None
    for num in arr:
        remainder = target - num
        result = bestSumNoDP(remainder, arr)
        if result is not None:
            combi = result + [num]
            if(ans == None or (len(combi) < len(ans))):
                ans = combi
                print(f'{combi} {ans} {target}')
    return ans


def bestSumDP(target, arr, memo = None):
    if(memo == None):
        memo = {}
    if(target in memo):
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None
    ans = None
    for num in arr:
        remainder = target - num
        result = bestSumDP(remainder, arr, memo)
        if(result is not None):
            combi = result + [num]
            if(ans == None or (len(combi) < len(ans))):
                ans = combi
    memo[target] = ans
    return ans

# , (7, [5, 3, 4, 7]), (7, [2, 4]), (8, [2, 3, 5])

testCases = [(8, [2, 3, 5])]

for test in testCases:
    targetSum, numbers = test
    print(f'bestSumNoDP({targetSum}, {numbers})={bestSumNoDP(targetSum, numbers)}')


# -------------------------------------------------------------------
# another method
from numpy import inf
class Solution:
    def __init__(self):
        self.ansFin = (inf, None)

    def howSum(self, target, numbers, currList = []):
        if target == 0:
            return []
        if target <= 0:
            return None
        for currEle in numbers:
            remainT = target - currEle
            currList.append(currEle)
            ans = self.howSum(remainT, numbers, currList)
            if ans is not None:
                res = ans + currList
                currLen = len(res)
                ansLen = self.ansFin[0]
                if(currLen < ansLen):
                    self.ansFin = (currLen, res)
                # print(res)
            currList.pop()
        return None


    def bestSum(self, candidates: List[int], target: int) -> List[List[int]]:

        self.howSum(target, candidates)
        print(self.ansFin)

        
obj = Solution()

obj.bestSum([2,4,3,7], 8)