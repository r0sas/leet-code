class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = 0
        new = ""
        if len(a) > len(b):
            highest = a
            lowest = b
        else:
            highest = b
            lowest = a
        for i in range(1, len(lowest)+1):
            new = str( (int(highest[-i]) + int(lowest[-i]) + s) %2) + new
            s = int( (int(highest[-i]) + int(lowest[-i]) + s) /2)
        for i in range(len(lowest)+1, len(highest)+1):
            new = str( (int(highest[-i]) + s) %2) + new
            s = int( (int(highest[-i]) + s) /2)
        if s == 1:
            new = "1" + new
        return new