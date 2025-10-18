class Solution:
    def isValid(self, s: str) -> bool:
        open = ["(", "[", "{"]
        oc_map = {"(": ")", "[": "]", "{": "}"}
        close = [")", "]", "}"]
        i=1
        while i < len(s):
            if s[i] not in oc_map.values():
                i += 1
                continue
            elif (s[i-1] not in oc_map.keys()) or (oc_map[s[i-1]] != s[i]):
                return False
            else:
                s = s[:i-1] + s[i+1:]
                i=1
        if len(s) == 0:
            return True
        else:
            return False

