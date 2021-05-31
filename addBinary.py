class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n1 = int(a,2)
        n2 = int(b,2)
        numSum = n1 + n2
        return bin(numSum)[2:]
        
s = Solution()
print(s.addBinary("010101001","0100100101"))