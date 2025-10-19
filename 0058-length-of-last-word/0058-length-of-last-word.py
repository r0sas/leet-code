class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split(" ")
        return [len(l[-i]) for i in range(1,len(l)+1) if l[-i] != ""][0]

