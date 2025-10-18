class Solution:
    def isValid(self, s: str) -> bool:
        open_close_map = {"(": ")", "[": "]", "{": "}"}
        close = [")", "]", "}"]
        i=1
        while i < len(s):
            if s[i] not in close:
                i += 1
                continue
            if s[i-1] not in open_close_map.keys():
                return False
            elif open_close_map[s[i-1]] != s[i]:
                return False
            else:
                s = s[:i-1] + s[i+1:]
                i=1
        print(s)
        if len(s) == 0:
            return True
        else:
            return False

