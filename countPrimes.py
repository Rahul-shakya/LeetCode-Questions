class Solution:
    def countPrimes(self, n: int) -> int:
    
        if n == 0:
            return 0
        l = [1] * (n)
        p = 2
        while( p * p <= n ):
            if( l[p] == 1 ):
                for i in range( p * 2, n, p ):
                    l[i] = 0
            p += 1

        l[0] = 0    
        if( len(l) > 1 ):
            l[1] = 0
        prime = sum(l) 

        return prime
s = Solution()
print(s.countPrimes(10))

