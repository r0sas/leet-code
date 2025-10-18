class Solution:
    def isValid(self, s: str) -> bool:
        open_close_map = {"(": ")", "[": "]", "{": "}"}
        close = [")", "]", "}"]
        i=1
        while i < len(s):
            if (s[i] not in close) or (s[i-1] not in open_close_map.keys()):
                i += 1
                continue
            elif open_close_map[s[i-1]] != s[i]:
                return False
            else:
                s = s[:i-1] + s[i+1:]
                i=1
        if len(s) == 0:
            return True
        else:
            return False

