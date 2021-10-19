class Solution:
    def numWays(self, n: int) -> int:
        if n == 0:
            return 1
        if n < 3:
            return n
        p = 0
        q = 1
        r = 2
        for i in range(3,n+1):
            p = q 
            q = r
            r = p+q
        return r%1000000007