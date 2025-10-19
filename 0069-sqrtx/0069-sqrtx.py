class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        if x == 2:
            return 1
        for i in range(1,x):
            if i*i == x:
                return i
            elif i*i > x:
                return i-1