import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = {}
        for currNum in nums:
            if currNum not in freqDict:
                freqDict[currNum] = 1
            else:
                freqDict[currNum] += 1
        heapAns = []
        for key,val in freqDict.items():
            if(k > 0):
                heapq.heappush(heapAns, (val,key))
            else:
                heapq.heappushpop(heapAns,(val,key))
            k -= 1
        ans = list(map(lambda x: x[1], heapAns))
        return ans

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        freqDict = {}
        for currNum in nums:
            if currNum not in freqDict:
                freqDict[currNum] = 1
            else:
                freqDict[currNum] += 1
        sortList = sorted(freqDict.items(), key = lambda x: x[1], reverse = True)
        return [element for element, _  in sortList[:k]]  # using list comprehension

        # another way:
        # return list(map(lambda x: x[0], sortList[:k]))  # using map func