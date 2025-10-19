class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        steps = [1, 2]
        comb = [1,1] +  [0] * (n-1)
        for i in range(2,n+1):
            for step in steps:
                comb[i] += comb[i-step]
        print(comb)
        return comb[-1]