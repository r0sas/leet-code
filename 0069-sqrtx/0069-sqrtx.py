class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        for i in range(2,x):
            if i*i > x:
                return i-1