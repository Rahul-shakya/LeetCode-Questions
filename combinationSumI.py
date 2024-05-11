# https://leetcode.com/problems/combination-sum/
from typing import List


class Solution:
    def __init__(self):
        self.ansFin = []

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
                res.sort()
                if(res not in self.ansFin):
                    self.ansFin.append(res)
                # print(res)
            currList.pop()
        return None


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        self.howSum(target, candidates)
        return(self.ansFin)

        