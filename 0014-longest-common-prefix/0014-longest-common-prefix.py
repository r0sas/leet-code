class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""

        for i in range(len(min(strs, key=len))):
            for x in strs:
                if x[i] != strs[0][i]:
                    return common
            common += x[i]
        return common